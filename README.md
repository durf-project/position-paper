# DURF Position Paper

A standalone, single-page presentation of the DURF position paper — published as
[`index.html`](index.html) via GitHub Pages at
**https://durf-project.github.io/position-paper/**, in the same [SURF Design
System](https://surfnet.github.io/DesignSystem/) look used by the
[DURF roadmap](https://github.com/durf-project/durf-gantt).

```
index.html            the page -- self-contained, ready to publish
position-paper.md      the source of truth for the text; edit this
assets/                logo, favicon and the vendored markdown renderer
LICENSE                CC BY 4.0 (Alastair Dunning and Maurice Vanderfeesten)
```

## Editing the text

Edit [`position-paper.md`](position-paper.md) — it's plain Markdown. `index.html`
fetches and renders it in the browser (via a locally vendored copy of
[marked](https://github.com/markedjs/marked)), so there is no build step: save
the file, push, and the published page picks it up automatically.

A few conventions used in the source:

- The first `#` heading and the italic byline line under it are the page
  title/byline — `index.html` shows those in its own header, so they are
  stripped from the rendered body to avoid repeating them.
- Blockquotes (`>`) are used for the draft's placeholder notes and citations,
  and render as highlighted "draft note" callouts.

## Previewing locally

Opening `index.html` directly (`file://`) will not load `position-paper.md` —
browsers block that fetch for local files. Run a local server instead:

```
python3 -m http.server
```

then open `http://localhost:8000`.

## The logo

`assets/durf-logo.svg` is a fresh, hand-built recreation of the DURF logo
(circular text over the five-piece puzzle mark), not a conversion of the
supplied `.eps`. Two things drove that:

1. The supplied vector file was a lossy auto-trace ("Vectorized from supplied
   PNG") with real bugs — two stray full-canvas rectangles that painted over
   the whole image, and a duplicated text layer in the wrong draw order that
   hid the blue ring text and three of the five puzzle pieces behind it. It
   did not reproduce the source PNG faithfully.
2. The word **"SECURE"** in the bottom arc needed to become **"RESILIENT"** —
   but the text in that EPS is traced outlines, not live type, so there was
   no text string to edit.

Instead, `assets/durf-icon.png` is a pixel-accurate crop of the central
puzzle mark straight from the supplied PNG (colours untouched), and the
circular text around it is real, editable SVG `<textPath>` text — so the
wording, font or colour can be changed directly in `durf-logo.svg` going
forward, no re-tracing required.

## License

[CC BY 4.0](LICENSE) — Alastair Dunning and Maurice Vanderfeesten. Third-party assets (the vendored
`marked` library) keep their own license; see `assets/marked.LICENSE.md`.

## Publishing

GitHub Pages needs to be enabled once by a repo admin: **Settings → Pages →
Source: "Deploy from a branch" → Branch: `main` → folder `/ (root)`**.
