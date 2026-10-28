# How to change the font of the printed notes

These instructions are for an AI assistant working in the `BIO II` folder. Read all of them before changing anything.

## What you're changing

The printed exam notes (the Word files in `Printed Exam Notes/`) are made by `Slide Notes Tools/build_print_docx.py`. The files the user prints, `Unit 2 Printed Notes.docx` and `Unit 2 Index.docx`, use the user's handwriting font, set by `UNIT_FILE_FONT` in `print_notes_data.py` (its name and the file in `Slide Notes Tools/fonts/`); to change or update that font, replace the file (or the setting), install it, rebuild, and check the build prints no missing-character warnings. The chapter files and the quick-guides copy take their typeface from **two lines** in `Slide Notes Tools/build_print_notes.py`. Change those two lines and rebuild. The size is `FONT_SIZE` in `print_notes_data.py` (Unit 2: 11.5 pt, the user's choice); a new typeface may be wider or narrower, so check that every chapter still fits 10 double-sided sheets (the build's last lines say so), or let `--fit` pick the largest size that fits.

**Never edit the .docx files by hand for this**; rebuild them.

## Rules

- In the script, change only the two lines in step 2 (and `FONT_SIZE`, if the user picks a size). Don't change any other code or file, except the note in `PLANS.md` (step 6).
- Never modify, rename, move or delete the PowerPoint files, and don't delete any file without asking the user.
- Don't open the PowerPoint app.

## Steps

**1. Pick an installed font.** On the Mac, list the fonts:

```
ls /System/Library/Fonts /System/Library/Fonts/Supplemental /Library/Fonts ~/Library/Fonts
```

You need the font's name as apps show it (e.g. `Georgia`) and the full path to its file. Prefer a `.ttf` or `.otf` file.

**2. Edit the two lines** near the top of `Slide Notes Tools/build_print_notes.py`. They currently read:

```python
FONT_NAME = "Arial Narrow"
FONT_FILE = "/System/Library/Fonts/Supplemental/Arial Narrow.ttf"
```

(Off the Mac, the script swaps in Liberation Sans Narrow for Arial Narrow automatically, through `METRIC_TWIN`; another font needs its own file path.)

**3. Set up Python and LibreOffice** if needed: see `PRINTED_NOTES.md`, "Files and tools".

**4. Build a test copy** into another folder, so the current files stay as they are:

```
cd "Slide Notes Tools"
PYTHONDONTWRITEBYTECODE=1 /tmp/printnotes-venv/bin/python build_print_docx.py --outdir "<test folder>"
```

The first output line gives the size, e.g. `11.5 pt, 2 columns:`; the last must start with `checks passed`. If a chapter is over its 10 sheets, add `--fit` to find the largest size that fits. The most likely problem is `the text isn't in <font>`: the name is misspelled or the font isn't installed, and LibreOffice silently used another font. If anything fails, put the two lines back and tell the user what it said.

**5. Show the user the test files** and the size. Only when they like it, run the same command without `--outdir` to replace the real files.

**6. Note the new font and size** in the Progress section of `PLANS.md`.

## Going back to the original font

Set the two lines back to the values in step 2 and run the step 5 command.

## Good to know

- A different size: set `FONT_SIZE` in `print_notes_data.py` (whole or half points; Word can't store finer sizes), or try one with `--font 11`. The output shows the sheets per chapter, which may exceed the budget.
- The font can also be changed by hand in one file: Word, Styles pane, modify **Normal**; LibreOffice, Styles (F11), modify **Default Paragraph Style**. Then select all and press F9 in Word to update the page numbers.
- The legacy PDF builder (`build_print_notes.py` run directly) uses the same two lines.
