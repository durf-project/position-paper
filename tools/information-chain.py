"""Draw assets/durf-information-chain.svg, the DURF information chain, in the style of the
DURF design system: Nunito for titles, Source Sans for the rest (both as outlines, so the
picture looks the same everywhere as an <img>), theme numbers as the DURF puzzle pieces.

Run:  pip install fonttools
      python3 tools/information-chain.py NUNITO.ttf SOURCESANS-REGULAR.ttf SOURCESANS-SEMIBOLD.ttf
NUNITO.ttf is the variable Nunito font; the Source Sans files are Source Sans Pro / 3 (static).
All fonts: SIL Open Font License. Change boxes, texts and arrows in the lists below.
"""
import sys
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = Path(__file__).resolve().parent.parent / "assets" / "durf-information-chain.svg"
NUNITO, SANS, SANS_SEMI = sys.argv[1:4]

INK, MUTED, LINE, ACCENT, CARD, BORDER = "#050E1D", "#5E6873", "#9AA2AC", "#177ABF", "#FFFFFF", "#B8C4D0"
THEME = {1: "#EE7628", 2: "#F6DA44", 3: "#177ABF", 4: "#17A95D", 5: "#5C1B61", 6: "#83201B"}

_fonts = {}
GLYPHS, DEFS = {}, {}   # every glyph is drawn once in <defs> and reused
def font(path, wght=None):
    key = (path, wght)
    if key not in _fonts:
        f = TTFont(path)
        if wght and "fvar" in f:
            f = instantiateVariableFont(f, {"wght": wght})
        _fonts[key] = f
    return _fonts[key]

def text(txt, x, y, size, kind="title", anchor="middle", fill=INK):
    """Text as outlines. kind: title (Nunito 800), number (Nunito 900), body, semi."""
    f = {"title": lambda: font(NUNITO, 800), "number": lambda: font(NUNITO, 900),
         "body": lambda: font(SANS), "semi": lambda: font(SANS_SEMI)}[kind]()
    gs, cmap, upm = f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm
    s = size / upm
    names = [cmap.get(ord(c), cmap[ord("?")]) for c in txt]
    width = sum(gs[n].width for n in names) * s
    x0 = x - width / 2 if anchor == "middle" else x - width if anchor == "end" else x
    cap = f["OS/2"].sCapHeight * s if getattr(f["OS/2"], "sCapHeight", 0) else size * .7
    base = y + cap / 2          # y is the vertical middle of capitals
    uses = []
    for n in names:
        gid = GLYPHS.setdefault((kind, n), f"g{len(GLYPHS)}")
        if gid not in DEFS:
            pen = SVGPathPen(gs); gs[n].draw(pen); DEFS[gid] = pen.getCommands()
        if DEFS[gid]:
            uses.append(f'<use href="#{gid}" transform="translate({x0:.1f} {base:.1f}) scale({s:.5f} {-s:.5f})"/>')
        x0 += gs[n].width * s
    return f'<g fill="{fill}">' + "".join(uses) + "</g>"

# ---- the DURF puzzle piece (design system: tools/puzzle-set.py), SURF puzzle style ----
R, D, CORNER = 16, 9, 4
C = round((R * R - D * D) ** .5, 2)
SIDES = {1: "+++-", 2: "----", 3: "--++", 4: "---+", 5: "++++", 6: "-++-"}   # top, right, bottom, left

def edge(p0, p1, kind):
    (x0, y0), (x1, y1) = p0, p1
    L = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** .5
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    a = (round(mx - ux * C, 2), round(my - uy * C, 2)); b = (round(mx + ux * C, 2), round(my + uy * C, 2))
    return [f"L{a[0]},{a[1]}", f"A{R},{R} 0 1 {1 if kind > 0 else 0} {b[0]},{b[1]}", f"L{x1},{y1}"]

def piece_path(n):
    t, r, b, l = [1 if c == "+" else -1 for c in SIDES[n]]
    k = CORNER
    d = [f"M{k},0"] + edge((k, 0), (100 - k, 0), t) + [f"A{k},{k} 0 0 1 100,{k}"]
    d += edge((100, k), (100, 100 - k), r) + [f"A{k},{k} 0 0 1 {100 - k},100"]
    d += edge((100 - k, 100), (k, 100), b) + [f"A{k},{k} 0 0 1 0,{100 - k}"]
    d += edge((0, 100 - k), (0, k), l) + [f"A{k},{k} 0 0 1 {k},0"]
    return " ".join(d) + " Z"

def piece(n, cx, cy, size=60, label=None, colour=None):
    s = size / 100
    num = text(label or str(n), cx, cy, size * .46, "number", fill=INK if n == 2 and not colour else "#FFFFFF")
    return (f'<path fill="{colour or THEME[n]}" transform="translate({cx - size / 2} {cy - size / 2}) scale({s})" d="{piece_path(n)}"/>' + num)

# ---- boxes and arrows ----
def box(x, y, w, h, title, sub=None, stack=False):
    out = ""
    if stack:
        for dx in (12, 6):
            out += f'<rect x="{x + dx}" y="{y - dx}" width="{w}" height="{h}" rx="14" fill="{CARD}" stroke="{BORDER}" stroke-width="2"/>'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{CARD}" stroke="{BORDER}" stroke-width="2.5"/>'
    lines = title.split("\n")
    total = len(lines) * 34 + (30 if sub else 0)
    ty = y + h / 2 - total / 2 + 17
    for ln in lines:
        out += text(ln, x + w / 2, ty, 26, "title"); ty += 34
    if sub:
        out += text(sub, x + w / 2, ty + 4, 20, "body", fill=MUTED)
    return out

def arrow(points, colour=ACCENT):
    """Straight segments through the points, arrow head at the last point."""
    d = "M" + " L".join(f"{x},{y}" for x, y in points[:-1])
    (x1, y1), (x2, y2) = points[-2], points[-1]
    L = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5; ux, uy = (x2 - x1) / L, (y2 - y1) / L
    hl, hw = 20, 11
    bx, by = x2 - ux * hl, y2 - uy * hl
    d += f" L{round(bx, 1)},{round(by, 1)}"
    head = f"M{x2},{y2} L{round(bx - uy * hw, 1)},{round(by + ux * hw, 1)} L{round(bx + uy * hw, 1)},{round(by - ux * hw, 1)} Z"
    return (f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="{head}" fill="{colour}"/>')

W, H = 1900, 1000
parts = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
# the federation
parts.append(f'<rect x="30" y="200" width="1840" height="620" rx="28" fill="#F5F7FA" stroke="{LINE}" stroke-width="3" stroke-dasharray="14 12"/>')
parts.append(piece(1, 632, 262))
parts.append(text("DURF: Dutch Repository Federation", 680, 248, 38, "title", "start"))
parts.append(text("Information ecosystem governance", 680, 292, 25, "body", "start", MUTED))
# repositories and CRIS, as one group
parts.append(f'<rect x="50" y="225" width="400" height="400" rx="22" fill="none" stroke="{ACCENT}" stroke-width="3" stroke-dasharray="10 9"/>')
parts.append(box(72, 262, 340, 135, "Research\nInformation Systems", stack=True))
parts.append(box(72, 440, 340, 160, "Institutional\nRepositories", "Literature, data, software", stack=True))
# outside the federation
parts.append(box(72, 28, 340, 130, "Other research indexes,\ncatalogues and graphs", stack=True))
parts.append(box(72, 860, 340, 125, "Publishing platforms", "Full texts and CC0 metadata", stack=True))
# OpenAIRE services
parts.append(box(560, 340, 330, 140, "Metadata harvester\nand validator", "OpenAIRE PROVIDE"))
parts.append(box(1010, 340, 300, 140, "OpenAIRE Graph"))
parts.append(box(1010, 545, 300, 130, "Enriched metadata", "OpenAIRE BROKER"))
parts.append(box(1480, 340, 360, 140, "Netherlands\nResearch Portal", "OpenAIRE CONNECT"))
parts.append(box(1480, 545, 360, 130, "Preservation", "KB e-Depot"))
parts.append(box(1480, 715, 360, 85, "KB URN resolver"))
# arrows, all straight
parts.append(arrow([(450, 410), (556, 410)]))                     # repositories -> harvester
parts.append(arrow([(890, 410), (1006, 410)]))                    # harvester -> graph
parts.append(arrow([(1160, 480), (1160, 541)]))                   # graph -> enriched metadata
parts.append(arrow([(1010, 610), (454, 610)]))                    # broker -> back to the repositories
parts.append(arrow([(1310, 410), (1476, 410)]))                   # graph -> portal
parts.append(arrow([(1395, 410), (1395, 610), (1476, 610)]))      # graph -> preservation
parts.append(arrow([(1660, 675), (1660, 711)]))                   # e-Depot -> resolver
parts.append(arrow([(242, 856), (242, 629)]))                     # publishing platforms -> repositories
parts.append(arrow([(242, 221), (242, 162)]))                     # repositories -> other indexes
# theme numbers on the arrows
parts.append(piece(2, 730, 556))
parts.append(piece(3, 305, 742))
parts.append(piece(5, 305, 188))
parts.append(piece(6, 1428, 352))
parts.append(piece(4, 1437, 658))
# legend
parts.append(piece(5, 1500, 905, 50, "#", MUTED))
parts.append(text("= DURF theme (1 to 6)", 1545, 905, 24, "body", "start", MUTED))

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">\n'
       f'<title id="t">The DURF information chain</title>\n<defs>' + "".join(f'<path id="{k}" d="{v}"/>' for k, v in DEFS.items() if v) + '</defs>\n' + "\n".join(parts) + "\n</svg>\n")
OUT.write_text(svg)
print("wrote", OUT, len(svg) // 1024, "KB")
