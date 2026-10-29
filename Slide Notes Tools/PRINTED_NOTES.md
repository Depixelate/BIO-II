# Printed exam notes: how to build them for any chapter

The exams allow printed notes but no pictures (professor, video call, Oct 2026). For each chapter we print two Word files that teach the material and make lookups fast. `AGENTS.md` has the short version; this file has the details. Ch 23 is the worked example.

## Files and tools
- `build_print_docx.py` builds the Word files; `build_print_notes.py` supplies the shared content functions and the legacy PDF builder.
- `print_notes_data.py` holds everything that isn't slide text, keyed by `(chapter, slide)`, except the glossary and term index, which are in `index_data.py`.
- `fonts/HandwritingFinal.otf`: the user's handwriting font, used for everything in the whole-unit Printed Notes and Index files (`UNIT_FILE_FONT`). Install it on the Mac (double-click it, then Install) before building or printing; on Linux the script installs it for LibreOffice itself.
- Setup:
  - `python3 -m venv /tmp/printnotes-venv && /tmp/printnotes-venv/bin/pip install python-pptx pymupdf python-docx defusedxml`;
  - LibreOffice at `/Applications/LibreOffice.app` (install with `brew install --cask libreoffice`).
- Run: `cd "Slide Notes Tools" && PYTHONDONTWRITEBYTECODE=1 /tmp/printnotes-venv/bin/python build_print_docx.py --only NN`. It must end with `checks passed`; any problem is printed and the script exits with an error. The body font size is `FONT_SIZE` in `print_notes_data.py` (Unit 2: 11.5 pt); `--fit` finds the largest that fits the budget instead, and `--font PT` tries another size. For the final files run it without `--only`, which also writes the whole-unit files. `--guides` rebuilds only the reading copy of the quick guides.
- Headless LibreOffice must run with `SAL_USE_VCLPLUGIN=osx` (the script does this). Otherwise it can't see the Mac's fonts and silently substitutes its own.
- Off the Mac (a Linux cloud session): `apt-get install fonts-liberation-sans-narrow` and use `soffice` from the PATH (the script does both automatically). Liberation Sans Narrow has Arial Narrow's letter widths, so page counts are close to the Mac's, but another program (or LibreOffice version) can break a page a line or two later: that's why the budget keeps a page to spare, and why Word needs select all + F9 to update the stored page numbers.
- Slide text for review: `build_print_notes.py --only NN --dump file.txt` (the chapter must be in `CHAPTERS`).

## What goes in the two files
Every chapter's title is `Ch. NN: <chapter name>` (from `CHAPTER_NAMES`), for example `Ch. 24: Flowering Plants: Structure and Organization`; the index file's adds ` (index)`. The title is also each page's header label. No other title or repeated chapter heading.

**`Printed Exam Notes/Ch NN Printed Notes.docx` (main):**
1. **Title.** Only the unit's first chapter (`CHAPTERS[0]`, Ch 23 for Unit 2) then has the "how to use these notes in the exam" box (`HOW_TO` in `build_print_docx.py`): find the key term or clue → that chapter's Index file (contents, term index, glossary, clue index) → the slide → the look-alike table → rule out absolute words. It is printed once per unit, not in any other chapter.
2. **Every content slide in deck order,** headed by its code: chapter.section.slide (23.2.17 = chapter 23, section 2, slide 17). The index files print the same slide as chapter.page.slide (below). All text, in the slide's wording.
3. **Lookup tables:** comparison tables, look-alikes, sequences, n/2n/3n, uses (`TABLES`, `SEQUENCES`, `PLOIDY`, `USES`). Every row cites slides.

No quick guide and no contents in the main files.

**`Printed Exam Notes/Ch NN Index.docx`:**
1. **Contents** of the chapter, first thing after the title: the main notes' sections, slide groups (with their codes) and lookup tables, each with its page in the main notes, then this file's parts (clue index, glossary, term index) with their pages here.

**Slide codes in the index files are chapter.page.slide** (the user's choice, Oct 29): the page is the main-notes page with that slide's heading, so 23.2.17 on page 5 prints as 23.5.17. That covers the contents, clue index, glossary, term index and codes typed inside definitions. A run of slides on one page is 23.5.17–18; across pages, 23.5.17–23.6.18. The data files keep chapter and slide numbers (and typed codes as chapter.section.slide); `Builder.page_codes` converts every code in an index file as it's written.
2. **Clue index** (`CLUES` in `print_notes_data.py`): a scenario's clue → answer + slide.
3. **Glossary: key terms** (`GLOSSARY` in `index_data.py`): the terms needed to understand the chapter and to answer its exam questions. That means the key terms (look-alikes as "A / B" pairs), plus the few words the slides use without explaining that are needed to follow them. Not a list of everything the slides don't define. Each entry: `Term: short plain definition` + the slide code where it's defined or explained. A definition only the textbook gives ends with "(textbook)". Sources: the study guide's key-term tables (§9), the quick guides' wording, past exam questions.
4. **Term index** (`TERM_INDEX` in `index_data.py`), alphabetical. Each term lists its **main place**, then **2–3 other places**, each with a **very short keyword** (1–4 words, usually 1–2) saying what the term is about there, e.g. `Rhizoids 23.2.17 (def.), 23.2.22 (mosses), 23.4.52 (fern prothallus)`.
   - The main place comes first: where the term is defined or explained, marked `(def.)`; if no slide defines it, its main use with a keyword.
   - The other places are the ones that matter for the exam, spread out. None is within 2 slides of a place already listed, because you see those anyway while you're there: for rhizoids, 23.1.15 and 23.2.18 are left out. Prefer the farthest, unless a nearer one is more important.
   - List a 3rd extra place only if it is still worth asking about. Fewer places when the term has no such places.
   - Organisms get a short note saying what they are, e.g. `Marchantia (liverwort)`.
   - Cover every chapter alike: its key terms, every glossary term that appears on a slide (the build fails otherwise), and every named organism or example on the slides (cocklebur, celery, Jatropha...), so a question that names one can be looked up.
   - The builder writes the cross-references: each other term in an entry's name gets a `see` line (`Petiole see Blade, petiole`; text in parentheses doesn't count, so name an entry "Pollination, self-pollination, cross-pollination", not "Pollination (self, cross)"). A glossary term that is on no slide gets `see Glossary`.

**Whole-unit files** (written by every full build, i.e. without `--only`): `Unit N Printed Notes.docx` and `Unit N Index.docx`, all chapters in one file each, for printing in one go. Each chapter starts on a new right-hand page (an odd-page section break), so after double-sided printing the chapters come apart.

**One continuous page numbering per unit** (the user's choice, Oct 29). The main notes run from page 1 (the first page of the first chapter) to N (the last page of the last chapter); the index files have their own 1 to M the same way. The chapter files only serve the unit files: each is an exact slice of its unit file, with the same font, page breaks and page numbers (`Ch 24 Printed Notes.docx` starts at page 13 if that's where Ch 24 starts in `Unit 2 Printed Notes.docx`). So the build lays out the unit files first, then gives each chapter file its first page number (`first_page`). Every chapter's first section is a right-hand-page section and its first page has no running header, in every file. LibreOffice lays out such pages alike, so the slices match (a document's first page otherwise starts 4 pt lower), and Word and LibreOffice agree on them. Also `Unit N Quick Guides.docx`, every chapter's quick guide at 11 pt, for reading: the quick guides are only in this file. Superseded outputs go in `Printed Exam Notes/Old/`.

**Quick guides** (`QUICK_GUIDE` in `quick_guides.py`), written for someone who has never seen the material, so they aren't lost on an exam question. Their length follows from a deep review of the chapter, not a target: explain every high-priority concept (definitions, processes, comparisons, "which structure or group" facts) and how the pieces connect; one line per item for organism-by-organism lists; leave numbers, extra examples, uses and textbook-only extras to the tables. Same depth for every chapter. Plain text, no border box. Writing rules:
- short sentences in plain words; explain every term where it first appears (a few words in parentheses is enough);
- say what each organism is: living or extinct, and which group (Cooksonia: extinct early vascular plant, not a lycophyte);
- no repetition (the intro doesn't repeat the first section; a later chapter doesn't re-explain an earlier one);
- never make a slide's claim stronger, and no absolute words ("only", "all", "always", "every") unless the slide uses them;
- when a slide is wrong, give the correct version in a few words (the full note is on the slide).

Parts:
- big picture;
- one part per section in order: key ideas in plain words with examples and slide codes, how the pieces connect, look-alike traps;
- a "look up, don't memorize" list.

## Rules
- **Page budget:** at most 10 double-sided sheets per chapter (`SHEETS_PER_CHAPTER`), counting the main and index files as printed separately: each rounds up to whole sheets (15 + 5 pages = 8 + 3 = 11 sheets). `--fit` also keeps a page to spare in the main file.
- **Font:** one body size for all chapter and unit files (`FONT_SIZE`; Unit 2: 11.5 pt, the user's choice), in whole or half points, since Word stores sizes in half points. Headings and the page header are fixed steps above or below it (`SIZE_STEP` in `build_print_docx.py`). The quick-guides copy is 11 pt (`GUIDES_FONT`).
- **Typeface:** every chapter and unit file (main notes and index) uses `UNIT_FILE_FONT` (the user's Handwriting Final) for every bit of text; the chapter files must, to be slices of the unit files. Only the quick-guides copy uses `FONT_NAME` (Arial Narrow). The build checks the sheet budget per chapter in the unit files too. It has no bold or italic face, so Word and LibreOffice draw bold and italic by thickening and slanting it.
- **Missing characters:** every build lists, as warnings, any character a file prints that its font has no glyph for, with an example of where (it would print in some other font). With the handwriting font, ask the user for an updated font rather than changing the text.
- **Layout:**
  - two columns everywhere; wide tables are printed as one small table per group;
  - a column line; borders on all table cells; no other boxes (only the how-to box, once per unit);
  - no pictures, no shaded fills;
  - bold only for slide codes, titles and table headings.
- **Page numbers:** the index files' contents pages and slide codes are fixed numbers taken from LibreOffice's layout of the unit main notes. A check reads every one of them back from each index file and confirms, in the main notes' PDF, that the slide's heading (or the lookup table) is on that page; another confirms each chapter file is page for page its slice of the unit file. The index's own parts are PAGEREF fields to bookmarks: LibreOffice updates them itself; Word does on select all + F9. The stored values come from LibreOffice's PDF, which must keep inserted blank pages (`IsSkipEmptyPages` false); the layout check compares every printed page number with the real page.
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
2. Fill the data: `QUICK_GUIDE`, `CAPTIONS`, `PROCESS`, `CORRECTIONS`, `TEXT_ALT_MATCH`, `TA_SKIP`, `CYCLES`/`FRAMES`, `FIG_SKIP`, `TYPO_FIX`, `FIG_FIX`, `SLIDE_TEXT`, `TABLES`, `SEQUENCES`, `PLOIDY`, `USES`, `CLUES` in `print_notes_data.py` (Ch 24–27 each have one block at the end; copy that layout), and `GLOSSARY` and `TERM_INDEX` in `index_data.py` (its docstring has the format and rules). For the term index, list every slide that mentions each term (the term's regex over the printed slide text), then pick the places by hand by the rules above. Glossary definitions: the textbook's glossary is at PDF pages 921–946.
3. Build, then verify (below), fix, rebuild.

## Verification (before telling the user it's done)
Do every step for every chapter at the same depth, working from the text actually printed in the packets (not an older dump).
- The script's checks pass (it exits with an error otherwise):
  - all slide text, figure text and corrections are present, and no quick-guide text is in the main files;
  - glossary and term index follow the rules: every place is a printed slide that mentions the term, main place first, at most 3 others, none within 2 slides of another, keywords of at most 4 words, `(def.)` only on the main place, no absolute words that the slide doesn't use, glossary slides mention their term (unless marked textbook);
  - every cited slide exists and mentions a key word of what it's cited for (a sanity check only: it can't judge meaning);
  - LibreOffice's layout: sheet budget met (chapter files and, per chapter, the whole-unit files); every index code and contents page right; each chapter file the exact slice of its unit file, printing the unit page numbers; page fields and headers correct; no pictures; every bit of text in the file's font;
  - no missing-character warnings.
- Slides vs textbook: compare every slide bullet with the textbook text (a fuzzy match flags the ones to read), and read every figure description for garbled or wrong statements; each disagreement gets a correction (or, if the textbook contradicts itself, follows the slide).
- Word-format validation passes: the docx skill's `validate.py`, at `~/.claude/skills/synced/*/docx/scripts/office/validate.py`. If it's missing, at least confirm LibreOffice converts the file.
- Convert to PDF with headless LibreOffice and look at every page.
- Read the printed term index entry by entry against the slide text: is the main place the definition, are the other places the important ones, is each keyword right and as short as it can be? Watch for regex false matches (e.g. "ground pines" under Pines, "nonflagellated" under Flagellated sperm, "prothallus" under Thallus).
- Check quick-guide statements and glossary definitions against the slides and textbook, and that the glossary has every key term of the chapter (study guide §9) and nothing minor.
- Read the rendered quick guides start to finish as someone new to the chapter: every term explained where it first appears, every organism placed in its group, no repetition, no absolute words the slide doesn't use, nothing important missing (compare with the study guide's key terms and learning objectives).
- `shasum` of the decks, `Speaker Notes/` and `Textbook Links/` is unchanged.
- **Tell the user the print steps:** LibreOffice (or Word), US Letter (the Mac's printer queue defaults to A4), 100%; odd pages, stack back in, even pages. Install the handwriting font first. The index files' page numbers and codes match LibreOffice's layout of the main notes; Word can break a page a line or two differently, so if printing the main notes from Word, check a few index codes against the pages (Word's select all + F9 updates only the index's own page fields). If they make a PDF from LibreOffice, "Export automatically inserted blank pages" must stay on, or the page numbers shift and chapters stop starting on right-hand pages.
- LibreOffice drops the running header on the first page after a right-hand-page break. That's why every chapter's first page (its title) has no header in every file, which Word then does the same way.
