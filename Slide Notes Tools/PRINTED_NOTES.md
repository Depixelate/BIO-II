# Printed exam notes: how to build them for any chapter

The exams allow printed notes but no pictures (professor, video call, Oct 2026). For each chapter we print two Word files that teach the material and make lookups fast. `AGENTS.md` has the short version; this file has the details. Ch 23 is the worked example.

## Files and tools
- `build_print_docx.py` builds the Word files; `build_print_notes.py` supplies the shared content functions and the legacy PDF builder.
- `print_notes_data.py` holds everything that isn't slide text, keyed by `(chapter, slide)`.
- Setup:
  - `python3 -m venv /tmp/printnotes-venv && /tmp/printnotes-venv/bin/pip install python-pptx pymupdf python-docx defusedxml`;
  - LibreOffice at `/Applications/LibreOffice.app` (install with `brew install --cask libreoffice`).
- Run: `cd "Slide Notes Tools" && PYTHONDONTWRITEBYTECODE=1 /tmp/printnotes-venv/bin/python build_print_docx.py --only NN`. It must end with `checks passed`; any problem is printed and the script exits with an error. The body font size is `FONT_SIZE` in `print_notes_data.py` (Unit 2: 11.5 pt); `--fit` finds the largest that fits the budget instead, and `--font PT` tries another size. For the final files run it without `--only`, which also writes the whole-unit files. `--guides` rebuilds only the reading copy of the quick guides.
- Headless LibreOffice must run with `SAL_USE_VCLPLUGIN=osx` (the script does this). Otherwise it can't see the Mac's fonts and silently substitutes its own.
- Off the Mac (a Linux cloud session): `apt-get install fonts-liberation-sans-narrow` and use `soffice` from the PATH (the script does both automatically). Liberation Sans Narrow has Arial Narrow's letter widths, so page counts are close to the Mac's, but another program (or LibreOffice version) can break a page a line or two later: that's why the budget keeps a page to spare, and why Word needs select all + F9 to update the stored page numbers.
- Slide text for review: `build_print_notes.py --only NN --dump file.txt` (the chapter must be in `CHAPTERS`).

## What goes in the two files
**`Printed Exam Notes/Ch NN Printed Notes.docx` (main):**
1. **Page 1:**
   - a "how to use these notes in the exam" box: find the key term or clue → this chapter's Index file → the slide → the look-alike table → rule out absolute words;
   - then the contents with page numbers: quick guide parts, sections, lookup pages, and "Indexes: see Ch NN Index".
2. **Quick guide** (`QUICK_GUIDE` in `quick_guides.py`), for someone who has never seen the material, so they aren't lost on an exam question. Its length follows from a deep review of the chapter, not a target: explain every high-priority concept (definitions, processes, comparisons, "which structure or group" facts) and how the pieces connect; one line per item for organism-by-organism lists; leave numbers, extra examples, uses and textbook-only extras to the tables. Same depth for every chapter. Plain text, no border box. Writing rules:
   - short sentences in plain words; explain every term where it first appears (a few words in parentheses is enough);
   - say what each organism is: living or extinct, and which group (Cooksonia: extinct early vascular plant, not a lycophyte);
   - no repetition (the intro doesn't repeat the first section; a later chapter doesn't re-explain an earlier one);
   - never make a slide's claim stronger, and no absolute words ("only", "all", "always", "every") unless the slide uses them;
   - when a slide is wrong, give the correct version in a few words (the full note is on the slide).

   Parts:
   - big picture;
   - one part per section in order: key ideas in plain words with examples and slide codes, how the pieces connect, look-alike traps;
   - a "look up, don't memorize" list.

   Each section heading in the slide pages gets one pointer line to its guide part (a PAGEREF field).
3. **Every content slide in deck order,** headed by its code (23.2.17 = chapter 23, section 2, slide 17). All text, in the slide's wording.
4. **Lookup tables:** comparison tables, look-alikes, sequences, n/2n/3n, uses (`TABLES`, `SEQUENCES`, `PLOIDY`, `USES`). Every row cites slides.

**`Printed Exam Notes/Ch NN Index.docx`:** page-1 contents, then the clue index (`CLUES`: a scenario's clue → answer + slide), the glossary (terms no slide explains) and the term index (`INDEX`).

**Whole-unit files** (written by every full build, i.e. without `--only`): `Unit N Printed Notes.docx` and `Unit N Index.docx`, all chapters in one file each, for printing in one go. Each chapter starts on a new right-hand page (an odd-page section break), so after double-sided printing the chapters come apart; page numbers run through the whole file. Also `Unit N Quick Guides.docx`, every chapter's quick guide at 11 pt, for reading. Superseded outputs go in `Printed Exam Notes/Old/`.

## Rules
- **Page budget:** at most 10 double-sided sheets per chapter (`SHEETS_PER_CHAPTER`), counting the main and index files as printed separately: each rounds up to whole sheets (15 + 5 pages = 8 + 3 = 11 sheets). `--fit` also keeps a page to spare in the main file.
- **Font:** one body size for all chapter and unit files (`FONT_SIZE`; Unit 2: 11.5 pt, the user's choice), in whole or half points, since Word stores sizes in half points. Headings and the page header are fixed steps above or below it (`SIZE_STEP` in `build_print_docx.py`). The quick-guides copy is 11 pt (`GUIDES_FONT`).
- **Layout:**
  - two columns everywhere; wide tables are printed as one small table per group;
  - a column line; borders on all table cells; no other boxes (only the page-1 how-to box);
  - no pictures, no shaded fills;
  - bold only for slide codes, titles and table headings.
- **Page numbers** in contents and pointers are PAGEREF fields to bookmarks: LibreOffice updates them itself; Word does on select all + F9. The stored values come from LibreOffice's PDF, which must keep inserted blank pages (`IsSkipEmptyPages` false); the layout check compares every printed page number with the real page.
- **One font setting:** the Normal style. Change `FONT_NAME`/`FONT_FILE` in `build_print_notes.py` for the typeface and `FONT_SIZE` for the size (see `Change the printed-notes font.md`).
- **Figures** (no pictures allowed):
  - print the deck's full text alternative;
  - if there's none, the short alt text plus the textbook caption when it adds something (`CAPTIONS`);
  - when neither explains a process diagram well enough, the textbook's description (`PROCESS`).
  - Text alternatives not hyperlinked to their slide: match them in `TEXT_ALT_MATCH` (a value of `None` unlinks a mislabeled one; 26.3.41's describes Mimosa and is printed with 26.2.35).
  - Typos inside a text alternative: `FIG_FIX` (e.g. "drape" → "drupe").
  - Life-cycle figures built up over several slides (`CYCLES`/`FRAMES`): the full description once on the last frame, one line on each earlier frame, plus anything an earlier frame says that the last doesn't (`FRAME_EXTRA`).
- **Slide errors and open questions:** the textbook wins, including on points that might be worth asking the professor about (the user's decision). Exception: where the textbook contradicts itself, follow the slide (24.3.30, monocot roots). Print the correct version on the slide, marked "Textbook:" (`CORRECTIONS`; this includes garbled or wrong figure descriptions, e.g. 27.1.13), and list it in the study guide's slide-errors section. Scanned-table typos are restored from the textbook (`TYPO_FIX`).
- **Slide text the reader can't get whole:** text in equation boxes and in `mc:AlternateContent` text boxes is read automatically; text split around pictures of symbols (MathType objects such as "H+") is rebuilt in `SLIDE_TEXT`, keeping every original fragment. Photo credits and labels like "Figure 25B" are dropped (`JUNK` in build_print_notes.py).
- **Sources:** every fact traces to a slide (or its text alternative) or the textbook (`Official Textbook/`, PDF page = book page + 19). The textbook wins over a slide. Never use Ch 20–22. `Unit 2 Study Guide.md` §2/§8/§9/§11 is already-checked source material for the guides and tables.

## Workflow for a new chapter
1. Add the chapter to `CHAPTERS` and dump its slides.
2. Fill the data: `QUICK_GUIDE`, `CAPTIONS`, `PROCESS`, `CORRECTIONS`, `TEXT_ALT_MATCH`, `TA_SKIP`, `CYCLES`/`FRAMES`, `FIG_SKIP`, `TYPO_FIX`, `FIG_FIX`, `SLIDE_TEXT`, `TABLES`, `SEQUENCES`, `PLOIDY`, `USES`, `CLUES`, `INDEX`, `GLOSSARY`. Ch 24–27 each have one block at the end of `print_notes_data.py`; copy that layout. Term-index entries apply only to their main slides' chapter. Glossary definitions: the textbook's glossary is at PDF pages 921–946.
3. Build, then verify (below), fix, rebuild.

## Verification (before telling the user it's done)
Do every step for every chapter at the same depth, working from the text actually printed in the packets (not an older dump).
- The script's checks pass (it exits with an error otherwise):
  - all slide text, figure text, corrections and guide text are present;
  - every cited slide exists and mentions a key word of what it's cited for (a sanity check only: it can't judge meaning);
  - LibreOffice's layout: sheet budget met, contents page numbers and headers correct, no pictures, the chosen font.
- Slides vs textbook: compare every slide bullet with the textbook text (a fuzzy match flags the ones to read), and read every figure description for garbled or wrong statements; each disagreement gets a correction (or, if the textbook contradicts itself, follows the slide).
- Word-format validation passes: the docx skill's `validate.py`, at `~/.claude/skills/synced/*/docx/scripts/office/validate.py`. If it's missing, at least confirm LibreOffice converts the file.
- Convert to PDF with headless LibreOffice and look at every page.
- Audit the term index's hits in context for false matches (e.g. "ground pines" under Pines, "nonflagellated" under Flagellated sperm, "prothallus" under Thallus).
- Check quick-guide statements and glossary definitions against the slides and textbook.
- Read the rendered quick guides start to finish as someone new to the chapter: every term explained where it first appears, every organism placed in its group, no repetition, no absolute words the slide doesn't use, nothing important missing (compare with the study guide's key terms and learning objectives).
- `shasum` of the decks, `Speaker Notes/` and `Textbook Links/` is unchanged.
- **Tell the user the print steps:** LibreOffice or Word, US Letter (the Mac's printer queue defaults to A4), 100%; odd pages, stack back in, even pages.
