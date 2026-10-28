# Printed exam notes: how to build them for any chapter

The exams allow printed notes but no pictures (professor, video call, Oct 2026). For each chapter we print two Word files that teach the material and make lookups fast. `AGENTS.md` has the short version; this file has the details. Ch 23 is the worked example.

## Files and tools
- `build_print_docx.py` builds the Word files; `build_print_notes.py` supplies the shared content functions and the legacy PDF builder.
- `print_notes_data.py` holds everything that isn't slide text, keyed by `(chapter, slide)`.
- Setup:
  - `python3 -m venv /tmp/printnotes-venv && /tmp/printnotes-venv/bin/pip install python-pptx pymupdf python-docx defusedxml`;
  - LibreOffice at `/Applications/LibreOffice.app` (install with `brew install --cask libreoffice`).
- Run: `cd "Slide Notes Tools" && PYTHONDONTWRITEBYTECODE=1 /tmp/printnotes-venv/bin/python build_print_docx.py --only NN`. It must end with `checks passed`.
- Headless LibreOffice must run with `SAL_USE_VCLPLUGIN=osx` (the script does this). Otherwise it can't see the Mac's fonts and silently substitutes its own.
- Slide text for review: `build_print_notes.py --only NN --dump file.txt` (the chapter must be in `CHAPTERS`).

## What goes in the two files
**`Printed Exam Notes/Ch NN Printed Notes.docx` (main):**
1. **Page 1:**
   - a "how to use these notes in the exam" box: find the key term or clue → this chapter's Index file → the slide → the look-alike table → rule out absolute words;
   - then the contents with page numbers: quick guide parts, sections, lookup pages, and "Indexes: see Ch NN Index".
2. **Quick guide** (`QUICK_GUIDE`), about 2–4 pages, for someone who has never seen the material:
   - big picture;
   - one part per section in order: key ideas in plain words with examples and slide codes, how the pieces connect, look-alike traps;
   - a "look up, don't memorize" list.

   Each section heading in the slide pages gets one pointer line to its guide part (a PAGEREF field).
3. **Every content slide in deck order,** headed by its code (23.2.17 = chapter 23, section 2, slide 17). All text, in the slide's wording.
4. **Lookup tables:** comparison tables, look-alikes, sequences, n/2n/3n, uses (`TABLES`, `SEQUENCES`, `PLOIDY`, `USES`). Every row cites slides.

**`Printed Exam Notes/Ch NN Index.docx`:** page-1 contents, then the clue index (`CLUES`: a scenario's clue → answer + slide), the glossary (terms no slide explains) and the term index (`INDEX`).

## Rules
- **Page budget:** main plus index at most 20 pages (10 double-sided sheets) per chapter (`SHEETS_PER_CHAPTER`). One font size for all files: the largest that fits (`--fit`, the default).
- **Layout:**
  - two columns everywhere; wide tables are printed as one small table per group;
  - a column line; borders on all table cells;
  - no pictures, no shaded fills;
  - bold only for slide codes, titles and table headings.
- **Page numbers** in contents and pointers are PAGEREF fields to bookmarks: LibreOffice updates them itself; Word does on select all + F9.
- **One font setting:** the Normal style. Change `FONT_NAME`/`FONT_FILE` in `build_print_notes.py` (see `Change the printed-notes font.md`).
- **Figures** (no pictures allowed):
  - print the deck's full text alternative;
  - if there's none, the short alt text plus the textbook caption when it adds something (`CAPTIONS`);
  - when neither explains a process diagram well enough, the textbook's description (`PROCESS`).
  - Text alternatives not hyperlinked to their slide: match them in `TEXT_ALT_MATCH`.
  - Life-cycle figures built up over several slides (`CYCLES`/`FRAMES`): the full description once on the last frame, one line on each earlier frame, plus anything an earlier frame says that the last doesn't (`FRAME_EXTRA`).
- **Slide errors:** print the correct version on the slide, marked "Textbook:" (`CORRECTIONS`), and list it in the study guide's slide-errors section. Scanned-table typos are restored from the textbook (`TYPO_FIX`).
- **Sources:** every fact traces to a slide (or its text alternative) or the textbook (`Official Textbook/`, PDF page = book page + 19). The textbook wins over a slide. Never use Ch 20–22. `Unit 2 Study Guide.md` §2/§8/§9/§11 is already-checked source material for the guides and tables.

## Workflow for a new chapter
1. Add the chapter to `CHAPTERS` and dump its slides.
2. Fill the data: `QUICK_GUIDE`, `CAPTIONS`, `PROCESS`, `CORRECTIONS`, `TEXT_ALT_MATCH`, `TA_SKIP`, `CYCLES`/`FRAMES`, `FIG_SKIP`, `TYPO_FIX`, `TABLES`, `SEQUENCES`, `PLOIDY`, `USES`, `CLUES`, `INDEX`, `GLOSSARY`.
3. Build, then verify (below), fix, rebuild.

## Verification (before telling the user it's done)
- The script's checks pass:
  - all slide text, figure text and corrections are present;
  - cited slides mention what they're cited for;
  - LibreOffice's layout: budget met, contents page numbers and headers correct, no pictures, the chosen font.
- Word-format validation passes: the docx skill's `validate.py`, at `~/.claude/skills/synced/*/docx/scripts/office/validate.py`. If it's missing, at least confirm LibreOffice converts the file.
- Convert to PDF with headless LibreOffice and look at every page.
- Audit the term index's hits in context for false matches (e.g. "ground pines" under Pines, "nonflagellated" under Flagellated sperm, "prothallus" under Thallus).
- Check quick-guide statements and glossary definitions against the slides and textbook.
- `shasum` of the decks, `Speaker Notes/` and `Textbook Links/` is unchanged.
- **Tell the user the print steps:** LibreOffice or Word, US Letter (the Mac's printer queue defaults to A4), 100%; odd pages, stack back in, even pages.
