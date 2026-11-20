# Position paper in Word

For reviewing the position paper with track changes and comments, in Word or in Collabora on
Nextcloud (SURF Works). [`position-paper.md`](../../position-paper.md) stays the source: the Word
file is made from it, and after the review the edited Word file is turned back into Markdown.
The website renders the Markdown, so the HTML follows by itself.

## Who does what

- **Editors (final editing):** Maurice Vanderfeesten and Simone Kortekaas. They put the Word file
  on Nextcloud, accept or reject the changes, answer the comments and bring the result back.
- **Contributors:** everyone who signed up through the survey. They edit with track changes on
  and add comments.

## The workflow

1. **Export** (editor):

       python3 tools/word/durf_word.py export position-paper.md -o position-paper-YYYY-MM-DD.docx

   Note the commit the export was made from (`git rev-parse --short HEAD`): put it in the file
   name or on the Nextcloud folder. Avoid editing `position-paper.md` on GitHub while the review
   runs; if that cannot be avoided, see *Changes on both sides* below.
2. **Review** on Nextcloud: share the file with the contributors. Track changes is switched on
   in the file. The appendices are included.
3. **Resolve** (editors): accept or reject all tracked changes and handle the comments. What is
   left open is taken as accepted and listed in the report.
4. **Import** (editor), against the Markdown of the export commit:

       git show <commit>:position-paper.md > /tmp/base.md
       python3 tools/word/durf_word.py import reviewed.docx --base /tmp/base.md -o position-paper.md

   This writes `position-paper.md` and `position-paper.import-report.md` with open changes,
   remaining comments (with the paragraph they are on) and notes about the special parts. Do not
   commit the report; use it for the pull request description.
5. **Check and publish:** open a pull request. Its diff shows exactly the edited paragraphs:
   unchanged paragraphs keep their original Markdown. Check the preview with
   `python3 -m http.server`, then merge.

## What Word cannot hold

The page has parts that are HTML, not text: the Corpus pop-up, buttons, fold-out panels with
interactive charts, the roles matrix in Appendix B, and the reference numbers. In the Word file
they appear as shaded markers like `⟦B3 · …⟧`. **Leave the markers in place.**

- **The Corpus pop-up** sits between a BEGIN and an END marker and may be edited. Changed
  paragraphs get new HTML; the rest of the pop-up is kept as it was. If paragraphs were added or
  removed, the pop-up is rebuilt and the report asks for a check on the website.
- **The roles matrix (Appendix B)** is read-only: changes to it are not taken over but listed in
  the report, so the editors can apply them by hand. Comments on it are welcome.
- **Reference numbers** are superscript links; the reference list keeps its anchors.
- **The information chain picture** is a PNG copy in Word; the website keeps the SVG.

## Changes on both sides

If `position-paper.md` changed on GitHub during the review, import against the export commit on a
branch made from that commit, and merge `main` into it: git then merges both sets of changes
paragraph by paragraph.

## Requirements

pandoc 3.x and Python 3. For the picture: `rsvg-convert`, or Node with Playwright
(`svg2png.mjs`). LibreOffice is only needed for testing (`soffice --headless --convert-to docx`
re-saves a file like Collabora does).

## Tested

- Export and import without edits gives back `position-paper.md` byte for byte, also after a
  re-save in LibreOffice (as Collabora does).
- With edits in the body and in the pop-up, a tracked change left open and a comment: the edits
  arrive, the open change is reported and accepted, the comment is listed with its paragraph,
  and the rest of the file is unchanged.
