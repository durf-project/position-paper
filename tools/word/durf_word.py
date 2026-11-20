#!/usr/bin/env python3
"""Round trip for the position paper: Markdown -> Word (for track changes and comments on
Nextcloud) -> Markdown again.

    python3 tools/word/durf_word.py export position-paper.md -o position-paper.docx
    python3 tools/word/durf_word.py import edited.docx --base position-paper.md -o position-paper.md

Needs pandoc (3.x). For the picture of the information chain (SVG) the export makes a PNG with
Chromium through Playwright (tools/word/svg2png.mjs); without it the picture is left out.

The Markdown contains HTML that Word cannot hold: the Corpus pop-up, two buttons, two fold-out
panels with interactive charts, the roles matrix of Appendix B, reference numbers (<sup>) and
their anchors (<a id>). The export turns each into something Word can show:

- an HTML block becomes a shaded marker paragraph "⟦B3 · ...⟧"; the pop-up and the matrix get a
  BEGIN and an END marker with their text in between, so it can be read and commented on;
- an inline button becomes a small marker "⟦I1 · ...⟧";
- <sup><a href="#ref-1">1</a></sup> becomes a superscript link, <a id="ref-1"></a> a bookmark.

The import reads the markers back and puts the original HTML in place. The text of the pop-up
may be edited: only the paragraphs that changed get new HTML, and the report says so.
The matrix is read-only: if its text changed, the original stays and the report lists the
changes, for the editors to apply by hand. The markers are found again by analysing --base, the
Markdown the Word file was exported from (same numbering), so nothing has to be kept in between.
Paragraphs that read the same as before keep their original Markdown, so a pull request shows
only the real edits. Tracked changes that were left open and all comments go into a report.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile, zipfile, copy

HERE = os.path.dirname(os.path.abspath(__file__))
MARK = "DURF Marker"          # paragraph style of the block markers
IMARK = "DURF Inline Marker"  # character style of the inline markers
INFO = ("⟦INFO · How to work in this document: keep Track changes on and use comments. Edit the text freely, "
        "but leave the shaded ⟦…⟧ markers in place: they stand for parts of the web page that Word cannot show "
        "(a pop-up window, buttons, interactive charts). The text of the pop-up between its BEGIN and END markers may be edited. "
        "The roles matrix in Appendix B is read-only here: please comment, the editors will apply the changes. "
        "This note disappears when the document goes back to the website.⟧")


# ---------------------------------------------------------------- pandoc helpers
def pandoc(args, data=None):
    r = subprocess.run(["pandoc"] + args, input=data, capture_output=True, text=True)
    if r.returncode:
        sys.exit("pandoc failed: " + r.stderr)
    for line in r.stderr.splitlines():
        if line.strip():
            print("  pandoc: " + line, file=sys.stderr)
    return r.stdout


def to_ast(text, fmt):
    return json.loads(pandoc(["-f", fmt, "-t", "json"], text))


def blocks_to(blocks, fmt, api, extra=()):
    doc = {"pandoc-api-version": api, "meta": {}, "blocks": blocks}
    return pandoc(["-f", "json", "-t", fmt, "--wrap=none"] + list(extra), json.dumps(doc))


def text_of(v):
    """All words in a piece of the document, without list numbers, table borders or styles."""
    out = []
    def walk(x):
        if isinstance(x, dict):
            t = x.get("t")
            if t == "Str":
                out.append(x["c"])
            elif t in ("Space", "SoftBreak", "LineBreak"):
                out.append(" ")
            elif t in ("Para", "Plain", "Header"):
                walk(x.get("c")); out.append(" ")
            else:
                walk(x.get("c"))
        elif isinstance(x, list):
            for y in x:
                walk(y)
    walk(v)
    t = "".join(out)
    t = t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return words_only(t)


def words_only(t):
    """For comparing: only the words, whatever the table borders or spacing."""
    return re.sub(r"[^\w→↓–—%&']+", " ", t).strip()


def plain(blocks, api):
    t = blocks_to(blocks, "plain", api)
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t).strip()


def words(text):
    out = []
    for i, w in enumerate(text.split(" ")):
        if i:
            out.append({"t": "Space"})
        if w:
            out.append({"t": "Str", "c": w})
    return out


def marker_block(text):
    return {"t": "Div", "c": [["", [], [["custom-style", MARK]]], [{"t": "Para", "c": words(text)}]]}


def marker_inline(text):
    return {"t": "Span", "c": [["", [], [["custom-style", IMARK]]], [{"t": "Str", "c": text}]]}


def strip_tags(html):
    t = re.sub(r"<[^>]+>", " ", html)
    for a, b in (("&amp;", "&"), ("&ndash;", "–"), ("&mdash;", "—"), ("&rarr;", "→"), ("&darr;", "↓"), ("&nbsp;", " ")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()


# ---------------------------------------------------------------- analysis (shared by export and import)
def analyse(md):
    """Parse the Markdown as GitHub Markdown (like the site does) and describe every HTML part."""
    doc = to_ast(md, "gfm")
    api = doc["pandoc-api-version"]
    blocks, inlines = [], []

    def describe(raw):
        r = raw.lstrip()
        if r.startswith("<dialog"):
            title = strip_tags((re.search(r"<h3[^>]*>(.*?)</h3>", r, re.S) or [None, "pop-up"])[1])
            return "dialog", "Pop-up window “%s” (it opens from the ⓘ button and the ‘Read more’ button)" % title
        if "durf-matrix" in r:
            return "readonly", "Appendix B, the roles and responsibilities matrix (read-only here: please comment, the editors apply the changes)"
        if r.startswith("<details"):
            s = re.search(r"<summary>(.*?)</summary>", r, re.S)
            return "single", "Start of a fold-out panel: %s" % (strip_tags(s.group(1)) if s else "")
        if r.startswith("</details"):
            return "single", "End of the fold-out panel"
        if r.startswith("<figure"):
            t = re.search(r'title="([^"]*)"', r)
            c = re.search(r"<figcaption>(.*?)</figcaption>", r, re.S)
            return "single", "Interactive chart%s, not shown in Word. Caption: %s" % (
                (": " + t.group(1)) if t else "", strip_tags(c.group(1)) if c else "")
        if r.startswith('<p class="durf-more"'):
            return "single", "Button: %s" % strip_tags(r)
        return "single", "Part of the web page that Word cannot show"

    def walk_blocks(bl):
        for b in bl:
            if b["t"] == "RawBlock" and b["c"][0] == "html":
                kind, label = describe(b["c"][1])
                blocks.append({"id": "B%d" % (len(blocks) + 1), "raw": b["c"][1], "kind": kind, "label": label})
            for v in children(b):
                walk_any(v)

    def walk_any(v):
        if isinstance(v, list):
            if v and isinstance(v[0], dict) and "t" in v[0]:
                if is_block(v[0]):
                    walk_blocks(v)
                else:
                    walk_inlines(v)
            else:
                for x in v:
                    walk_any(x)
        elif isinstance(v, dict) and "t" in v:
            walk_blocks([v]) if is_block(v) else walk_inlines([v])

    def walk_inlines(il):
        i = 0
        while i < len(il):
            x = il[i]
            if x["t"] == "RawInline" and x["c"][0] == "html":
                kind, n = inline_kind(il, i)
                if kind == "other":
                    raw, label = inline_raw(il, i, n)
                    inlines.append({"id": "I%d" % (len(inlines) + 1), "raw": raw, "label": label})
                i += n
                continue
            for v in children(x):
                walk_any(v)
            i += 1

    walk_blocks(doc["blocks"])
    return doc, api, blocks, inlines


BLOCK_TYPES = {"Plain", "Para", "LineBlock", "CodeBlock", "RawBlock", "BlockQuote", "OrderedList", "BulletList",
               "DefinitionList", "Header", "HorizontalRule", "Table", "Figure", "Div", "Null"}


def is_block(x):
    return x.get("t") in BLOCK_TYPES


def is_nodes(v):
    return isinstance(v, list) and bool(v) and isinstance(v[0], dict) and "t" in v[0]


def children(x):
    """The parts of a node; a list of blocks or inlines stays together (patterns span several inlines)."""
    c = x.get("c")
    if is_nodes(c):
        return [c]
    if isinstance(c, list):
        return c
    return []


TAG = re.compile(r"^<(/?)([a-zA-Z][a-zA-Z0-9]*)")


def inline_kind(il, i):
    """What starts at il[i]: a reference number, an anchor, or another inline HTML element."""
    s = lambda k: il[k]["c"][1] if k < len(il) and il[k]["t"] == "RawInline" else None
    if s(i) == "<sup>" and s(i + 1) and re.match(r'<a href="#ref-\d+">$', s(i + 1)) and il[i + 2]["t"] == "Str" \
            and s(i + 3) == "</a>" and s(i + 4) == "</sup>":
        return "ref", 5
    m = re.match(r'<a id="([^"]+)">(</a>)?$', s(i) or "")
    if m:
        return "anchor", 1 if m.group(2) else 2
    # another element: up to its closing tag
    t = TAG.match(s(i) or "")
    if not t or t.group(1):
        return "other", 1
    name, depth = t.group(2), 0
    for k in range(i, len(il)):
        r = s(k)
        if r is None:
            continue
        tm = TAG.match(r)
        if tm and tm.group(2) == name:
            depth += -1 if tm.group(1) else 1
            if depth == 0:
                return "other", k - i + 1
    return "other", 1


def inline_raw(il, i, n):
    parts, text = [], []
    for x in il[i:i + n]:
        if x["t"] == "RawInline":
            parts.append(x["c"][1])
        elif x["t"] == "Str":
            parts.append(x["c"]); text.append(x["c"])
        elif x["t"] == "Space":
            parts.append(" "); text.append(" ")
    raw = "".join(parts)
    lab = re.search(r'aria-label="([^"]*)"', raw)
    return raw, (lab.group(1) if lab else "".join(text) or "HTML")


# ---------------------------------------------------------------- export
def export(args):
    md = open(args.markdown, encoding="utf-8").read()
    doc, api, blocks, inlines = analyse(md)
    base = os.path.dirname(os.path.abspath(args.markdown))
    tmp = tempfile.mkdtemp(prefix="durf-word-")
    bi = iter(blocks); ii = iter(inlines)

    def conv_blocks(bl):
        out = []
        for b in bl:
            if b["t"] == "RawBlock" and b["c"][0] == "html":
                d = next(bi)
                if d["kind"] == "dialog":
                    out += [marker_block("⟦%s BEGIN · %s⟧" % (d["id"], d["label"]))] + dialog_body(d["raw"]) + \
                           [marker_block("⟦%s END · end of the pop-up window⟧" % d["id"])]
                elif d["kind"] == "readonly":
                    out += [marker_block("⟦%s BEGIN · %s⟧" % (d["id"], d["label"]))] + to_ast(d["raw"], "html")["blocks"] + \
                           [marker_block("⟦%s END⟧" % d["id"])]
                else:
                    out.append(marker_block("⟦%s · %s⟧" % (d["id"], d["label"])))
                continue
            out.append(conv_children(b))
        return out

    def conv_children(x):
        x = copy.copy(x)
        if is_nodes(x.get("c")):
            x["c"] = conv_any(x["c"])
        elif isinstance(x.get("c"), list):
            x["c"] = [conv_any(v) for v in x["c"]]
        return x

    def conv_any(v):
        if isinstance(v, list):
            if v and isinstance(v[0], dict) and "t" in v[0]:
                return conv_blocks(v) if is_block(v[0]) else conv_inlines(v)
            return [conv_any(x) for x in v]
        if isinstance(v, dict) and "t" in v:
            return conv_blocks([v])[0] if is_block(v) else conv_inlines([v])[0]
        return v

    def conv_inlines(il):
        out, i = [], 0
        while i < len(il):
            x = il[i]
            if x["t"] == "RawInline" and x["c"][0] == "html":
                kind, n = inline_kind(il, i)
                if kind == "ref":
                    href = re.search(r'href="([^"]+)"', il[i + 1]["c"][1]).group(1)
                    out.append({"t": "Superscript", "c": [{"t": "Link", "c": [["", [], []], [il[i + 2]], [href, ""]]}]})
                elif kind == "anchor":
                    aid = re.match(r'<a id="([^"]+)"', x["c"][1]).group(1)
                    out.append({"t": "Span", "c": [[aid, [], []], []]})
                else:
                    d = next(ii)
                    out.append(marker_inline("⟦%s · %s⟧" % (d["id"], "ⓘ" if "durf-info" in d["raw"] else d["label"])))
                i += n
                continue
            if x["t"] == "Image":
                x = copy.deepcopy(x)
                src = x["c"][2][0]
                if src.lower().endswith(".svg"):
                    png = svg_to_png(os.path.join(base, src), tmp)
                    if png:
                        x["c"][2][0] = png
                    else:
                        print("  could not make a PNG of %s: left out" % src, file=sys.stderr)
                        x = {"t": "Str", "c": "[picture: %s]" % src}
                else:
                    x["c"][2][0] = os.path.join(base, src)
                out.append(x)
            else:
                out.append(conv_children(x))
            i += 1
        return out

    doc["blocks"] = [marker_block(INFO)] + conv_blocks(doc["blocks"])
    js = os.path.join(tmp, "doc.json")
    json.dump(doc, open(js, "w"))
    ref = reference_docx(tmp)
    pandoc(["-f", "json", js, "-o", args.output, "--reference-doc", ref])
    track_changes_on(args.output)
    shutil.rmtree(tmp, ignore_errors=True)
    print("Wrote %s: %d HTML blocks, %d inline elements as markers; track changes on." % (args.output, len(blocks), len(inlines)))


def dialog_body(raw):
    m = re.search(r'<div class="durf-dialog-body">(.*)</div>\s*<footer>', raw, re.S)
    return to_ast(m.group(1) if m else raw, "html")["blocks"]


def svg_to_png(svg, tmp):
    out = os.path.join(tmp, os.path.basename(svg)[:-4] + ".png")
    for cmd in (["rsvg-convert", "-z", "2", "-o", out, svg], ["node", os.path.join(HERE, "svg2png.mjs"), svg, out]):
        try:
            if subprocess.run(cmd, capture_output=True).returncode == 0 and os.path.exists(out):
                return out
        except FileNotFoundError:
            pass
    return None


def reference_docx(tmp):
    """pandoc's default reference document with the DURF look and the two marker styles."""
    ref = os.path.join(tmp, "reference.docx")
    data = subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"], capture_output=True).stdout
    open(ref, "wb").write(data)
    src = zipfile.ZipFile(ref)
    files = {n: src.read(n) for n in src.namelist()}
    src.close()
    st = files["word/styles.xml"].decode("utf-8")
    blue = "1A7CC1"
    # headings in DURF blue
    st = re.sub(r'(<w:style w:type="paragraph"[^>]*w:styleId="Heading\d"[^>]*>.*?<w:rPr>)(.*?)(</w:rPr>)',
                lambda m: m.group(1) + re.sub(r'<w:color [^>]*/>', '', m.group(2)) + '<w:color w:val="%s"/>' % blue + m.group(3), st, flags=re.S)
    st = st.replace("</w:styles>",
        '<w:style w:type="paragraph" w:customStyle="1" w:styleId="DURFMarker"><w:name w:val="%s"/><w:basedOn w:val="Normal"/>'
        '<w:pPr><w:pBdr><w:left w:val="single" w:sz="24" w:space="6" w:color="EE7628"/></w:pBdr>'
        '<w:shd w:val="clear" w:color="auto" w:fill="FDEBDD"/><w:spacing w:before="120" w:after="120"/><w:ind w:left="170"/></w:pPr>'
        '<w:rPr><w:i/><w:color w:val="7A3A10"/><w:sz w:val="18"/></w:rPr></w:style>'
        '<w:style w:type="character" w:customStyle="1" w:styleId="DURFInlineMarker"><w:name w:val="%s"/>'
        '<w:rPr><w:color w:val="7A3A10"/><w:sz w:val="16"/><w:shd w:val="clear" w:color="auto" w:fill="FDEBDD"/></w:rPr></w:style>'
        "</w:styles>" % (MARK, IMARK))
    files["word/styles.xml"] = st.encode("utf-8")
    with zipfile.ZipFile(ref, "w", zipfile.ZIP_DEFLATED) as z:
        for n, d in files.items():
            z.writestr(n, d)
    return ref


def track_changes_on(path):
    src = zipfile.ZipFile(path)
    files = {n: src.read(n) for n in src.namelist()}
    src.close()
    s = files["word/settings.xml"].decode("utf-8")
    if "<w:trackRevisions" not in s:
        s = re.sub(r"(<w:settings[^>]*>)", r"\1<w:trackRevisions/>", s, count=1)
    files["word/settings.xml"] = s.encode("utf-8")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for n, d in files.items():
            z.writestr(n, d)


# ---------------------------------------------------------------- import
def do_import(args):
    md = open(args.base, encoding="utf-8").read()
    _, api, blocks, inlines = analyse(md)
    B = {b["id"]: b for b in blocks}
    I = {x["id"]: x for x in inlines}
    report, seen = [], set()
    tmp = tempfile.mkdtemp(prefix="durf-word-")

    # what was left unresolved: tracked changes and comments, read from the Word XML itself
    open_changes, comments = docx_open_items(args.docx)
    if open_changes:
        report.append("- **%d tracked changes were not accepted or rejected.** They are taken as accepted (insertions kept, deletions applied)." % len(open_changes))

    internal = {}     # link text -> "#target" in the original, for links Word renamed
    def find_links(v):
        if isinstance(v, dict):
            if v.get("t") == "Link" and v["c"][2][0].startswith("#"):
                internal.setdefault(text_of(v["c"][1]), v["c"][2][0])
            for x in v.values():
                find_links(x)
        elif isinstance(v, list):
            for x in v:
                find_links(x)
    find_links(to_ast(md, "gfm")["blocks"])
    targets = set(internal.values())

    doc = json.loads(pandoc(["-f", "docx+styles", "-t", "json", "--track-changes=accept", "--extract-media=" + tmp, args.docx]))
    imgs = []
    def find_imgs(v):
        if isinstance(v, dict):
            if v.get("t") == "Image":
                imgs.append(v)
            for x in v.values():
                find_imgs(x)
        elif isinstance(v, list):
            for x in v:
                find_imgs(x)
    orig_imgs = []
    find_imgs(to_ast(md, "gfm")["blocks"])
    orig_imgs, imgs = imgs, []
    find_imgs(doc["blocks"])

    def marker_text(b):
        if b["t"] == "Div" and dict(b["c"][0][2]).get("custom-style") == MARK:
            return plain(b["c"][1], api)
        return None

    def back_blocks(bl):
        out, i = [], 0
        while i < len(bl):
            b = bl[i]
            t = marker_text(b)
            if t is not None:
                m = re.match(r"⟦(B\d+|INFO)( BEGIN| END)?", t)
                if not m:
                    report.append("- A marker paragraph was changed and not recognised: “%s”. It was left out." % t[:80])
                    i += 1; continue
                bid, part = m.group(1), (m.group(2) or "").strip()
                if bid == "INFO":
                    i += 1; continue
                d = B.get(bid)
                if not d:
                    report.append("- Unknown marker %s, left out." % bid); i += 1; continue
                seen.add(bid)
                if part == "BEGIN":
                    j = i + 1
                    while j < len(bl) and not (marker_text(bl[j]) or "").startswith("⟦%s END" % bid):
                        j += 1
                    inner = back_blocks(bl[i + 1:j])
                    out.append({"t": "RawBlock", "c": ["html", rebuild(d, inner, api, report)]})
                    i = j + 1
                    continue
                out.append({"t": "RawBlock", "c": ["html", d["raw"]]})
                i += 1
                continue
            if b["t"] == "Div" and not b["c"][0][0] and dict(b["c"][0][2]).get("custom-style"):
                out += back_blocks(b["c"][1])     # a Word paragraph style: keep the content only
                i += 1
                continue
            out.append(back_children(b))
            i += 1
        return out

    def back_children(x):
        x = copy.copy(x)
        if is_nodes(x.get("c")):
            x["c"] = back_any(x["c"])
        elif isinstance(x.get("c"), list):
            x["c"] = [back_any(v) for v in x["c"]]
        return x

    def back_any(v):
        if isinstance(v, list):
            if v and isinstance(v[0], dict) and "t" in v[0]:
                return back_blocks(v) if is_block(v[0]) else back_inlines(v)
            return [back_any(x) for x in v]
        if isinstance(v, dict) and "t" in v:
            r = back_blocks([v]) if is_block(v) else back_inlines([v])
            return r[0] if r else {"t": "Str", "c": ""}
        return v

    def unwrap_styles(il):
        """Word wraps text in character-style spans (Hyperlink and the like): keep the text only."""
        res = []
        for x in il:
            if x["t"] == "Span" and not x["c"][0][0] and not x["c"][0][1] and dict(x["c"][0][2]).get("custom-style") not in (None, IMARK):
                res += unwrap_styles(x["c"][1])
            else:
                if x["t"] in ("Link", "Superscript", "Emph", "Strong", "Subscript", "Strikeout", "Underline", "SmallCaps", "Quoted", "Cite", "Span"):
                    x = copy.deepcopy(x)
                    if x["t"] in ("Link", "Span", "Quoted", "Cite"):
                        k = 1
                        x["c"][k] = unwrap_styles(x["c"][k])
                    else:
                        x["c"] = unwrap_styles(x["c"])
                res.append(x)
        return res

    def back_inlines(il):
        out = []
        il = unwrap_styles(il)
        for x in il:
            if x["t"] == "Span":
                attr = x["c"][0]; kv = dict(attr[2])
                if kv.get("custom-style") == IMARK:
                    t = plain([{"t": "Plain", "c": x["c"][1]}], api)
                    m = re.match(r"⟦(I\d+)", t)
                    if m and m.group(1) in I:
                        seen.add(m.group(1)); out.append({"t": "RawInline", "c": ["html", I[m.group(1)]["raw"]]})
                    else:
                        report.append("- An inline marker was changed and not recognised: “%s”." % t)
                    continue
                if re.match(r"ref-\d+$", attr[0]):
                    out.append({"t": "RawInline", "c": ["html", '<a id="%s"></a>' % attr[0]]})
                    out += back_inlines(x["c"][1])
                    continue
                if not attr[0] and not attr[1] and not kv:
                    out += back_inlines(x["c"][1]); continue
                out += back_inlines(x["c"][1])   # other spans (bookmarks of headings, styles): keep the text only
                continue
            if x["t"] == "Link" and x["c"][2][0].startswith("#ref-") and len(x["c"][1]) == 1 and x["c"][1][0]["t"] == "Superscript":
                href = x["c"][2][0]; n = plain([{"t": "Plain", "c": x["c"][1][0]["c"]}], api)
                out.append({"t": "RawInline", "c": ["html", '<sup><a href="%s">%s</a></sup>' % (href, n)]})
                continue
            if x["t"] == "Superscript" and len(x["c"]) == 1 and x["c"][0]["t"] == "Link" and x["c"][0]["c"][2][0].startswith("#ref-"):
                href = x["c"][0]["c"][2][0]; n = plain([{"t": "Plain", "c": x["c"][0]["c"][1]}], api)
                out.append({"t": "RawInline", "c": ["html", '<sup><a href="%s">%s</a></sup>' % (href, n)]})
                continue
            if x["t"] == "Link" and x["c"][2][0].startswith("#") and x["c"][2][0] not in targets:
                t = internal.get(text_of(x["c"][1]))
                if t:
                    x = copy.deepcopy(x); x["c"][2][0] = t
            if x["t"] == "Image":
                x = copy.deepcopy(x)
                k = imgs.index(next(im for im in imgs if im["c"][2][0] == x["c"][2][0]))
                if k < len(orig_imgs):
                    x["c"][2][0] = orig_imgs[k]["c"][2][0]
                    x["c"][0] = ["", [], []]
                else:
                    report.append("- A new picture was added (%s): put it in assets/ and fix its path." % x["c"][2][0])
                out.append(x)
                continue
            out.append(back_children(x))
        return out

    doc["blocks"] = merge_lists(back_blocks(doc["blocks"]))
    for k in list(B) + list(I):
        if k not in seen:
            report.append("- Marker %s (%s) was deleted in Word: the part is missing now. Put it back by hand if that was not intended." %
                          (k, (B.get(k) or I.get(k))["label"]))
    md_out = blocks_to(doc["blocks"], "gfm", api)
    md_out = house_style(md_out)
    md_out = restore_ref_anchors(md_out, md)
    md_out = keep_source(md_out, md)
    open(args.output, "w", encoding="utf-8").write(md_out)
    rep = args.report or os.path.splitext(args.output)[0] + ".import-report.md"
    lines = ["# Import report for %s" % os.path.basename(args.docx), ""]
    lines += report or ["- Nothing to report: every marker came back unchanged."]
    if comments:
        lines += ["", "## Comments still in the document (%d)" % len(comments), ""]
        lines += ["- **%s:** %s%s" % (a, t, ("  \n  _on:_ \u201c%s\u201d" % (w[:160] + ("…" if len(w) > 160 else ""))) if w else "") for a, t, w in comments]
    open(rep, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    shutil.rmtree(tmp, ignore_errors=True)
    print("Wrote %s and %s (%d notes, %d comments)." % (args.output, rep, len(report), len(comments)))


def docx_open_items(path):
    """Tracked changes not yet accepted or rejected, and comments with the paragraph they are on."""
    z = zipfile.ZipFile(path)
    names = z.namelist()
    docxml = z.read("word/document.xml").decode("utf-8")
    changes = re.findall(r"<w:(?:ins|del) [^>]*w:id=", docxml)
    comments = []
    if "word/comments.xml" in names:
        cx = z.read("word/comments.xml").decode("utf-8")
        paras = re.findall(r"<w:p[ >].*?</w:p>", docxml, re.S)
        def para_text(px):
            return re.sub(r"\s+", " ", "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", px))).strip()
        for m in re.finditer(r'<w:comment ([^>]*)>(.*?)</w:comment>', cx, re.S):
            attrs = dict(re.findall(r'w:(\w+)="([^"]*)"', m.group(1)))
            text = para_text(m.group(2))
            where = next((para_text(px) for px in paras if re.search(r'<w:comment(?:RangeStart|Reference) w:id="%s"' % attrs.get("id"), px)), "")
            comments.append((attrs.get("author", "?"), text, where))
    for a, b in (("&apos;", "'"), ("&quot;", '"'), ("&lt;", "<"), ("&gt;", ">"), ("&amp;", "&")):
        comments = [tuple(x.replace(a, b) for x in c) for c in comments]
    return changes, comments


def merge_lists(bl):
    """LibreOffice saves every item as a list of its own: put consecutive lists together again."""
    out = []
    for b in bl:
        b = merge_inside(b)
        if out and b["t"] == "BulletList" and out[-1]["t"] == "BulletList":
            out[-1] = {"t": "BulletList", "c": out[-1]["c"] + b["c"]}
            continue
        if out and b["t"] == "OrderedList" and out[-1]["t"] == "OrderedList":
            prev = out[-1]
            # two numbered lists in a row are one list whose numbering LibreOffice restarted
            out[-1] = {"t": "OrderedList", "c": [prev["c"][0], prev["c"][1] + b["c"][1]]}
            continue
        out.append(b)
    return out


def merge_inside(b):
    if b["t"] in ("BulletList",):
        return {"t": b["t"], "c": [merge_lists(item) for item in b["c"]]}
    if b["t"] == "OrderedList":
        return {"t": b["t"], "c": [b["c"][0], [merge_lists(item) for item in b["c"][1]]]}
    if b["t"] in ("BlockQuote",):
        return {"t": b["t"], "c": merge_lists(b["c"])}
    if b["t"] == "Div":
        return {"t": "Div", "c": [b["c"][0], merge_lists(b["c"][1])]}
    return b


def rebuild(d, inner, api, report):
    """The HTML of a BEGIN/END part: the original if its text did not change."""
    if d["kind"] == "readonly":
        before = text_of(to_ast(d["raw"], "html")["blocks"])
        after = text_of(inner)
        if before != after:
            report.append("- **%s (%s) changed in Word.** The original was kept; apply the change by hand. Text in Word:\n\n  > %s" % (d["id"], d["label"], after[:1500]))
        return d["raw"]
    before = text_of(dialog_body(d["raw"]))
    after = text_of(inner)
    if before == after:
        return d["raw"]
    patched = patch_body(d["raw"], inner, api)
    if patched:
        new_raw, n = patched
        report.append("- **%s (%s) was edited in Word:** %d paragraph%s changed and %s put in the pop-up; the rest is unchanged." %
                      (d["id"], d["label"], n, "" if n == 1 else "s", "was" if n == 1 else "were"))
        return new_raw
    body = blocks_to(inner, "html", api)
    body = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', body)
    body = body.replace("&#10;", "")
    body = re.sub(r'<ol type="1">', "<ol>", body)
    body = re.sub(r"</ol>\s*<ol>", "", body)                      # a list Word split in two
    # headings keep their original ids (the "Read more" button points at #corpus-commons)
    for hid, text in re.findall(r'<h\d id="([^"]+)">(.*?)</h\d>', d["raw"]):
        body = re.sub(r'(<h\d) id="[^"]*">(%s)</h' % re.escape(text), r'\1 id="%s">\2</h' % hid, body)
    # the reference list of the pop-up
    if 'class="durf-dialog-refs"' in d["raw"]:
        body = re.sub(r"(<p><strong>References</strong></p>.*)$", r'<div class="durf-dialog-refs">\n\1\n</div>', body.strip(), flags=re.S)
    m = re.search(r'(<div class="durf-dialog-body">)(.*)(</div>\s*<footer>)', d["raw"], re.S)
    report.append("- **%s (%s) was edited in Word, with paragraphs added or removed.** It was rebuilt from the edited text: "
                  "check it on the website (formatting inside the pop-up may need a touch)." % (d["id"], d["label"]))
    return d["raw"][:m.start(2)] + "\n" + body.strip() + "\n" + d["raw"][m.end(2):]


def restore_ref_anchors(md_out, base):
    """Word drops bookmarks nothing links to: put <a id="ref-N"> back at the start of reference N."""
    ids = dict(re.findall(r'(?m)^(\d+)\. <a id="(ref-\d+)"></a>', base))
    if not ids:
        return md_out
    lines, inside = md_out.split("\n"), False
    for k, line in enumerate(lines):
        m = re.match(r"^(\d+)\. (.*)$", line)
        if '<a id="ref-' in line and m:
            inside = True
        if inside and m:
            rest = re.sub(r'<a id="ref-\d+"></a>', "", m.group(2))      # wherever Word put it
            lines[k] = '%s. <a id="ref-%s"></a>%s' % (m.group(1), m.group(1), rest)   # reference N has anchor ref-N
        elif inside and line.startswith("#"):
            inside = False
    return "\n".join(lines)


UNIT = re.compile(r"^(\s*)<(p|li|h\d)((?: [^>]*)?)>(.*)</\2>\s*$")


def patch_body(raw, inner, api):
    """Put only the changed paragraphs of the pop-up back, keeping the HTML of all others.
    Works when the number of paragraphs, list items and headings stayed the same."""
    m = re.search(r'(<div class="durf-dialog-body">)(.*)(</div>\s*<footer>)', raw, re.S)
    if not m:
        return None
    lines = m.group(2).split("\n")
    units = [(k, UNIT.match(l)) for k, l in enumerate(lines) if UNIT.match(l)]
    new = []
    def walk(bl):
        for b in bl:
            if b["t"] in ("Para", "Plain", "Header"):
                new.append(b["c"] if b["t"] != "Header" else b["c"][2])
            elif b["t"] == "BulletList":
                for item in b["c"]:
                    walk(item)
            elif b["t"] == "OrderedList":
                for item in b["c"][1]:
                    walk(item)
            elif b["t"] in ("Div",):
                walk(b["c"][1])
            elif b["t"] == "BlockQuote":
                walk(b["c"])
    walk(inner)
    if len(new) != len(units):
        return None
    changed = 0
    for (k, um), il in zip(units, new):
        if text_of(to_ast("<p>%s</p>" % um.group(4), "html")["blocks"]) == text_of(il):
            continue
        html = blocks_to([{"t": "Plain", "c": il}], "html", api).strip()
        html = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', html)
        lines[k] = "%s<%s%s>%s</%s>" % (um.group(1), um.group(2), um.group(3), html, um.group(2))
        changed += 1
    return raw[:m.start(2)] + "\n".join(lines) + raw[m.end(2):], changed


def keep_source(md_out, base):
    """Where a paragraph or block renders exactly as before, keep its original Markdown text
    (line breaks, * or _), so the pull request only shows what really changed."""
    import difflib
    def split(t):
        parts = re.split(r"(\n[ \t]*\n\s*)", t.strip("\n"))
        return parts[0::2], parts[1::2] + ["\n"]
    (old, osep), (new, nsep) = split(base), split(md_out)
    cache = {}
    def render(cs):
        for c in cs:
            if c not in cache:
                cache[c] = pandoc(["-f", "gfm", "-t", "html", "--wrap=none"], c)
        return [cache[c] for c in cs]
    ro, rn = render(old), render(new)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ro, rn, autojunk=False).get_opcodes():
        if op == "equal":
            out += [c + sp for c, sp in zip(old[i1:i2], osep[i1:i2])]
        else:
            out += [c + sp for c, sp in zip(new[j1:j2], nsep[j1:j2])]
    return "".join(out).rstrip("\n") + "\n"


def house_style(md):
    """Small things pandoc writes differently from the hand-written Markdown."""
    md = re.sub(r"(?m)^\*([^*\n]+)\*$", r"_\1_", md)    # an italic line (the authors line) as _..._
    md = re.sub(r"(?m)^\\\((\d+)\\\)", r"(\1)", md)
    md = re.sub(r"(?m)^(\d+)\.\s{2,}(?=\S)", r"\1. ", md)       # "1.  item" -> "1. item"   # "\(1\)" at the start of a paragraph
    out = []
    for line in md.split("\n"):
        if line.startswith("|") and line.rstrip().endswith("|"):
            if re.match(r"^\|[-:| ]+\|$", line.strip()):      # the separator row
                line = "|" + "|".join(" --- " for _ in line.strip().strip("|").split("|")) + "|"
            else:                                              # no padding to line up the columns
                line = re.sub(r" {2,}\|", " |", line)
        out.append(line)
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("export"); e.add_argument("markdown"); e.add_argument("-o", "--output", default="position-paper.docx")
    i = sub.add_parser("import"); i.add_argument("docx"); i.add_argument("--base", required=True)
    i.add_argument("-o", "--output", required=True); i.add_argument("--report")
    a = ap.parse_args()
    export(a) if a.cmd == "export" else do_import(a)


if __name__ == "__main__":
    main()
