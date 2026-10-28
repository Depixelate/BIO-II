# How to change the font of the printed notes

These instructions are for an AI assistant working in the `BIO II` folder. Read all of them before changing anything.

## What you're changing

The printed exam notes (`Printed Exam Notes/Ch 23 Printed Notes.pdf`) are made by a script, `Slide Notes Tools/build_print_notes.py`. To change the font, change **two lines** in that script and run it again. The script rebuilds the whole PDF and picks the largest font size that still fits 8 double-sided sheets (16 pages).

**Never edit the PDF itself.**

## Rules

- In the script, change only the two lines in step 2. Don't change any other code or file, except one line in `AGENTS.md` (step 7).
- Never modify, rename, move or delete the PowerPoint files, and don't delete any file without asking the user.
- Don't open the PowerPoint app.

## Steps

**1. Pick an installed font.** List the fonts on this Mac:

```
ls /System/Library/Fonts /System/Library/Fonts/Supplemental /Library/Fonts ~/Library/Fonts
```

You need two things: the font's name as apps show it (e.g. `Georgia`) and the full path to its file. Prefer a `.ttf` or `.otf` file. A `.ttc` file also works, but the page header will use the first style inside it.

**2. Edit the two lines** near the top of `Slide Notes Tools/build_print_notes.py`. They currently read:

```python
FONT_NAME = "Arial Narrow"
FONT_FILE = "/System/Library/Fonts/Supplemental/Arial Narrow.ttf"
```

For example, for Georgia:

```python
FONT_NAME = "Georgia"
FONT_FILE = "/System/Library/Fonts/Supplemental/Georgia.ttf"
```

**3. Set up Python** (only if `/tmp/printnotes-venv` doesn't exist yet):

```
python3 -m venv /tmp/printnotes-venv
/tmp/printnotes-venv/bin/pip install python-pptx pymupdf
```

Google Chrome must be installed at `/Applications/Google Chrome.app`. It is; the script uses it to make the PDF.

**4. Build a test copy.** This doesn't replace the current PDF:

```
cd "/Users/velusamykaruppagounder/Documents/BIO II/Slide Notes Tools"
PYTHONDONTWRITEBYTECODE=1 /tmp/printnotes-venv/bin/python build_print_notes.py --only 23 --out "../Printed Exam Notes/Ch 23 Printed Notes (Georgia test).pdf"
```

Use the new font's name in the file name. It takes about 20 seconds.

**5. Read the output.**
- The first line gives the size, e.g. `10.5 pt, 2 columns: 16 pages (8 sheets double-sided)`. Wider fonts come out at smaller sizes.
- The last line must start with `checks passed`.
- If it lists problems instead, don't try to fix the code. Put the two lines back the way they were (see "Going back" below) and tell the user what it said.
- The most likely problem is `the text isn't in <font>`. That means the name in `FONT_NAME` is misspelled or the font isn't installed, and Chrome silently used a different font.

**6. Show the user the test PDF** and tell them the size. Only when they say they like it, build the real one. This replaces `Ch 23 Printed Notes.pdf`:

```
PYTHONDONTWRITEBYTECODE=1 /tmp/printnotes-venv/bin/python build_print_notes.py --only 23
```

Again, the last line must start with `checks passed`.

**7. Update one line in `AGENTS.md`.** In the section "Printed exam notes", the "Size" bullet names the font and the size, e.g. "Ch 23 came out at 11.25 pt in 2 columns, Arial Narrow, Letter." Change it to the new font and size.

**8. Ask the user** whether to delete the test copy from step 4. Don't delete it without their OK.

## Going back to the original font

Set the two lines back to:

```python
FONT_NAME = "Arial Narrow"
FONT_FILE = "/System/Library/Fonts/Supplemental/Arial Narrow.ttf"
```

Then run the command in step 6.

## The Word version (`Ch 23 Printed Notes.docx`)

There's also an editable Word version, made by `build_print_docx.py`. It uses the same two font lines.

- **To rebuild it with the new font:** after step 2, run this instead of the step 4 and 6 commands:

  ```
  PYTHONDONTWRITEBYTECODE=1 /tmp/printnotes-venv/bin/python build_print_docx.py --only 23
  ```

  It needs LibreOffice (installed at `/Applications/LibreOffice.app`), takes about a minute, and must also end with `checks passed`. Add `--out "<path>"` for a test copy, as in step 4.
- **Or change the font by hand in the .docx itself:** one change covers everything.
  - **Word:** in the Styles pane, modify the font of the **Normal** style.
  - **LibreOffice:** in Styles (F11), modify the font of **Default Paragraph Style**.

  Then select all and press F9 (Word) to update the map's page numbers. LibreOffice updates them by itself.

## Good to know

- A size the user picks instead of "largest that fits": add `--font 10` to the command (2 columns by default). The output then shows how many pages that makes, which may be more than 16.
- Only Ch 23 exists so far. For later chapters, use `--only 24` and so on, once they've been added.
- Printing: open the PDF in Preview, choose File → Print, and set Paper Size to US Letter (this Mac defaults to A4) and Scale to 100%.
