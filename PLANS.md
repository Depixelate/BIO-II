# PLANS.md: Exam-ready Word notes for BIO II Unit 2 (Ch 23–27)

For: a Codex agent (GPT-6.1 Sol) running in `/Users/velusamykaruppagounder/Documents/BIO II`.

Save this file in the project as `PLANS.md`; OpenAI's Codex guide recommends a `PLANS.md` / execution plan for long, multi-step work.
- Work through the stages in order.
- Keep the **Progress** section at the end of this file updated (done, next, decisions, problems), so work can resume if interrupted.
- Reasoning effort: OpenAI's GPT-6 guide says to start with the default `medium` and increase it if the quality gain is worth the time. Use `high` for the writing stages (quick guides, clue indexes) if `medium` output misses facts.

**How to work** (from OpenAI's GPT-6 guide):
- This plan is the user's authorization to do all of it. Infer intent and scope from it.
- Finish each stage before asking; the user's review comes at the end of each stage, on a concrete result.
- Read-only actions and reversible edits to the files named here don't need approval.
- Don't stop at acknowledgments or a restated plan.
- The user's instructions here take precedence over any other guidance file. If `AGENTS.md` or anything else seems to conflict, name the exact file and line when you raise it.

## Goal
The user is a BIO II student taking **Exam 2 (Ch 23–27)**, which closes **Fri Oct 30, 2026**.
- The exam is open-book: printed notes allowed, **no pictures**, no computer.
- They haven't studied fully, so they need printed Word documents that **teach the material** (plain-language quick guides) and let them **look things up fast** (all slide text in order, figures in words, indexes).

**Done when:**
- every chapter, Ch 23–27, has two finished, checked Word files (§3, decision 2);
- `AGENTS.md` records this setup as the standard for later units.

Deliver in stages (§4–§7) and tell the user after each stage what's ready to print.

## Constraints (also in `AGENTS.md`; read that whole file first)
- Never modify, rename, move or delete the PowerPoint decks in `Chapter PPTs and Other Study Materials/`. Never delete any file without asking the user. Don't open or script the PowerPoint app.
- Every fact in the notes must trace to a slide (or its text alternative) or the textbook; cite slide codes.
  - When a slide and the textbook disagree, the textbook wins.
  - Never mention Ch 20–22 content.
- Don't weaken or skip the build script's checks to make a build pass. Fix the content or the code instead.

## When to ask the user
Ask only when the answer would change what the user gets and nothing here decides it. Examples:
- the page budget can't be met above about 9 pt;
- a check still fails after two real attempts at a fix;
- something would need deleting or overwriting beyond the build outputs named here.

For anything else, choose sensibly, note it in Progress, and continue.

## 1. Context: what exists now
- **History:** the previous conversation's transcript (built by a Claude Code session) is at `/Users/velusamykaruppagounder/.claude/projects/-Users-velusamykaruppagounder-Documents-BIO-II/2261b77e-6003-4937-a85d-565a58f2b2e5.jsonl`. It's about 72 MB of JSON lines; `grep`/`jq` it for specific details rather than reading it whole.
- **Builder:** `Slide Notes Tools/build_print_docx.py` builds the notes as a **Word document (.docx)**, the format the user chose.
  - It reads the untouched decks plus `Slide Notes Tools/print_notes_data.py`, which holds everything that isn't slide text.
  - It reuses content functions from `Slide Notes Tools/build_print_notes.py` (`Chapter`, `glossary`, `term_index`, `fmt_refs`, `groups`, `check_citations`, `FONT_NAME`/`FONT_FILE`). That file also builds an older PDF version; leave the PDF part alone.
- **Run it:** `cd "Slide Notes Tools" && PYTHONDONTWRITEBYTECODE=1 /tmp/printnotes-venv/bin/python build_print_docx.py --only 23`.
  - Create the venv once: `python3 -m venv /tmp/printnotes-venv && /tmp/printnotes-venv/bin/pip install python-pptx pymupdf python-docx defusedxml`.
  - LibreOffice is installed at `/Applications/LibreOffice.app`. The script runs it headless with the environment variable `SAL_USE_VCLPLUGIN=osx`; without it, headless LibreOffice can't see the Mac's fonts and silently substitutes others.
  - A successful run ends with `checks passed`.
- **Done so far:** `Printed Exam Notes/Ch 23 Printed Notes.docx`. Arial Narrow 11.25 pt, 2 columns, 15 pages in LibreOffice. Contents:
  - page 1: five reminders for ruling out answers, then a contents map with page numbers;
  - all Ch 23 slides headed by their codes (23.2.17 = chapter 23, section 2, slide 17), with figures as words and "Textbook:" corrections;
  - lookup pages (comparison tables, sequences, n/2n/3n, uses, clue index, glossary, term index).
- **Page numbers** in the contents are **PAGEREF fields**:
  - each slide heading has a Word bookmark, and the contents line holds a field showing that bookmark's page number;
  - LibreOffice updates them automatically; Word does when you select all and press F9.

  Use the same mechanism for every new "see page X" pointer.
- **Only Ch 23 has data** in `print_notes_data.py`. Ch 24–27 have none yet.
- **Content sources:**
  - `Unit 2 Study Guide.md`, already checked: §2 "Unit 2 in plain English" and its "Six ideas"; §8 cross-chapter tables; §9 per-chapter "What this chapter is about", key terms, "Understand" bullets, look-up tables; §11 slide errors.
  - `Exam Pattern Analysis.md`: how the professor writes questions.
  - The textbook PDF in `Official Textbook/` (PDF page = book page + 19).
- **Slide text for review:** `build_print_notes.py --only CH --dump file.txt`. The chapter must be listed in `print_notes_data.CHAPTERS`.

## 2. The user's decisions (all confirmed; follow exactly)
1. **Word documents only.** Keep building with `build_print_docx.py`.
2. **Each chapter separately, like Ch 23, as two files per chapter:**
   - `Printed Exam Notes/Ch NN Printed Notes.docx`: the main file, with the quick guide, all slides and the chapter's lookup tables;
   - `Printed Exam Notes/Ch NN Index.docx`: that chapter's **clue index, glossary and term index**, and nothing else.

   The three indexes appear only in the index file. Split Ch 23's existing file the same way.
3. **Page budget: at most 10 double-sided sheets (20 pages) per chapter, counting that chapter's main file plus its index file together.**
   - Use **one font size for all files**: the largest at which every chapter fits.
   - The existing `--fit` logic searches font sizes in 0.25 pt steps using LibreOffice's page count; extend it to the combined budget.
   - Set `SHEETS_PER_CHAPTER = 10` in `print_notes_data.py`.
4. **One quick guide at the front of each main file,** about 3–4 pages:
   - big picture first;
   - **one part per section, in order**;
   - **no separate section intros** in the slide pages. Each section heading gets only a one-line pointer: "Quick guide for this section: page N" (a PAGEREF field to a bookmark on that guide part).
5. **Two columns everywhere.** The user found mixed layouts confusing (some pages with one table across both columns, others with two tables side by side).
   - The two wide Ch 23 tables ("Plant groups", "Life cycles compared" in `print_notes_data.TABLES`, marked `"wide": True`) become one small table or block per group or life cycle inside a column.
6. **A thin vertical line between the two columns, and borders on all table cells.** Black is fine.
   - Use Word's column separator (`w:sep="1"` on each section's `w:cols`).
   - Use thin (about 0.5 pt) table borders (`w:tblBorders`, including inside borders).
   - No shaded fills (toner).
7. **Page 1 of each main file:**
   - a short "how to use these notes in the exam" box: find the key term or clue in the question → look it up in this chapter's Index file (clue index or term index) → go to the slide → check the look-alike table → rule out answers with absolute words ("only", "all", "always", "must", "every"; always wrong on Unit 1);
   - then the contents: quick guide parts, sections, lookup pages, and "Indexes: see Ch NN Index".
8. **Page 1 of each index file:** its own contents (clue index, glossary, term index, with page numbers).
9. **This is the standard for later units too** (Units 3–5), so record it in `AGENTS.md` (§3).

## 3. Step 0: update `AGENTS.md` (do first, quickly)
Rewrite its section "Printed exam notes" so a future agent can repeat this for any unit. It must say:
- **Format:** Word only (`build_print_docx.py`). The PDF builder is legacy.
- **Files:** two files per chapter, main and index (decision 2); the contents of each.
- **Budget:** 10 double-sided sheets per chapter, main plus index; one font size for all files; the largest that fits (`--fit`).
- **Quick guide** rules (decision 4, §4), and that guide statements cite slides.
- **Layout:** decisions 5–8.
- **Figures, corrections, lookup tables and indexes:** keep the existing rules already in that section.
- **The verification checklist** in §8.
- **The per-chapter workflow** in §5, as "how to do a new chapter", with Ch 23 as the worked example.

Keep the rest of `AGENTS.md` unchanged. OpenAI's Codex guide: "A short, accurate `AGENTS.md` is more useful than a long file full of vague rules"; when it grows large, keep it concise and reference task-specific markdown files.
- Put the full how-to (the per-chapter workflow, the data fields and the verification checklist) in a new `Slide Notes Tools/PRINTED_NOTES.md`.
- Make the `AGENTS.md` section a short summary of the decisions plus "follow `Slide Notes Tools/PRINTED_NOTES.md`".

## 4. Stage 1: quick guides for all five chapters (deliver first)
- **Write one quick guide per chapter** for someone who has **never seen the material**, as one continuous story:
  1. the big picture for the whole chapter in 3–4 sentences;
  2. one part per section, in order, headed like the section ("24.3 Roots, slides 26–34"). Each part gives:
     - the key ideas in plain words, each with a concrete example and its slide codes;
     - how the pieces connect (what does what, in what order, n vs 2n where it matters);
     - the look-alike pairs behind the believable wrong answers;
  3. a closing "look these up, don't memorize" list.
- **Sources:** the chapter's slides (dump them), study guide §2, §8 and §9 for that chapter, and the textbook to explain.
- **Data:** a new `QUICK_GUIDE` in `print_notes_data.py`, e.g. `{ch: {"intro": [paragraphs], "sections": {section_number: [paragraphs or (subheading, [bullets])]}, "look_up": [items]}}`.
- **Rendering** (`build_print_docx.py`), right after the chapter heading:
  - its own paragraph styles, inheriting the font from Normal so one font change still covers everything;
  - no border box (the user's decision, Oct 28: in two columns it drew a box around each column); the guide is set apart by its own headings and position;
  - a bookmark on each section part for the pointers.
- **Section numbers** (confirm against `Deck.section` in `Slide Notes Tools/build_slide_notes.py`):
  - Ch 23: 23.1 = slides 3–15, 23.2 = 16–30, 23.3 = 31–35, 23.4 = 36–53, 23.5 = 54–91.
  - Ch 24: 24.1 = 3–17, 24.2 = 18–25, 24.3 = 26–34, 24.4 = 35–49, 24.5 = 50–55.
  - Ch 25: 25.1 = 3–18, 25.2 = 19–27, 25.3 = 28–48.
  - Ch 26: 26.1 = 3–23, 26.2 = 24–35, 26.3 = 36–46.
  - Ch 27: 27.1 = 3–19, 27.2 = 20–26, 27.3 = 27–35, 27.4 = 36–41.
- **Done when:**
  - all five guides are written and checked against the slides and textbook;
  - Ch 23's main file is rebuilt with its guide;
  - `Printed Exam Notes/Unit 2 Quick Guides.docx` (all five guides together) exists as a temporary reading copy while Ch 24–27 are built. Tell the user it's temporary; the final guides live in each main file.

## 5. Stage 2: Ch 24–27 main and index files (in exam order 24 → 25 → 26 → 27; deliver each when done)
For each chapter:
- **Add it to `print_notes_data.CHAPTERS`** and fill the same fields Ch 23 uses: `CAPTIONS`, `PROCESS`, `CORRECTIONS`, `TEXT_ALT_MATCH`, `TA_SKIP`, `CYCLES`/`FRAMES` (figures built up over several slides), `FIG_SKIP`, `TYPO_FIX`, `INDEX`, `GLOSSARY`, `CLUES`, `TABLES`, `SEQUENCES`, `PLOIDY`, `USES`.
- **Figures** (pictures aren't allowed): print the deck's full text alternative (hidden slides at the end of each deck).
  - Text alternatives not hyperlinked to their slide: match them by title in `TEXT_ALT_MATCH`.
  - Slides with only a short alt text (about 33: Ch 24: 8, Ch 25: 6, Ch 26: 13, Ch 27: 6) get the textbook caption where it adds something.
  - Use the textbook's own process description (`PROCESS`) for: root specializations (Ch 24 slide 33), leaf diversity (24/55), the auxin–cytokinin ratio (26/15), how ABA closes stomata (26/19), etiolation (26/43), insect pollinators (27/18).
  - Ch 24, 26 and 27 decks are 14th edition, so their figure numbers may differ from the 2024 Release textbook; match by content. Ch 25 matches.
- **Corrections** (study guide §11):
  - Ch 24 slides 42 (woody stems do have vascular tissue) and 27 (lignin isn't a protein);
  - Ch 25 slides 4 (N missing from the macronutrients) and 19 (confusing wording);
  - Ch 26 slide 29 (roots, not stems, have root caps) and the slide 56 text alternative (mislabeled);
  - Ch 27 slide 5 (a microspore *becomes* the male gametophyte).
- **Main file lookup tables:** comparison tables, sequences, n/2n/3n, uses, look-alikes, from study guide §8/§9. Rows cite slides as `(chapter, slide)` tuples; `check_citations` verifies them.
- **Index file:**
  - term index (`INDEX`: start from the study guide §9 key terms);
  - glossary (terms no slide explains);
  - clue index (`CLUES`: a scenario's clue → answer + slide, grouped by organisms, structures, processes).
  - Audit each index pattern's hits in context for false matches (e.g. "ground pines" under Pines, "nonflagellated" under Flagellated sperm).
- **Done when:** both files exist and pass §8.

## 6. Stage 3: final layout and build
- Apply decisions 5–8 to all ten files.
- Rebuild everything at the single largest font size where every chapter's main plus index pages are at most 20.
- **Done when:** all files pass §8 at that size.

## 7. Stage 4: wrap-up
- Make sure `AGENTS.md` matches what was actually built.
- Update `PROGRESS.md`.
- Ask the user whether to delete the leftovers: `Printed Exam Notes/Ch 23 Printed Notes (large print).pdf` and the temporary `Unit 2 Quick Guides.docx`. Don't delete without their OK.

## 8. Verification (before every delivery)
- The script's checks pass:
  - all slide text, figure text and corrections are in the main file;
  - every cited slide mentions what it's cited for;
  - LibreOffice's layout: budget met, contents page numbers and headers correct, no pictures, the chosen font.
- Word-format validation passes:
  - run `/tmp/printnotes-venv/bin/python /Users/velusamykaruppagounder/.claude/skills/synced/ab055352-cf2f-45fe-8803-a8ad83e0e208_dc4ee915-8171-4bdf-b702-eb59eff3b83a/docx/scripts/office/validate.py <file>.docx`; it must print "All validations PASSED";
  - if that path is missing, at least confirm LibreOffice converts the file without errors.
- Convert each file to PDF with headless LibreOffice (as the script does) and **look at every page**: gaps, cut-off tables, column line and table borders present, no boxes around the columns.
- Check every quick-guide statement and glossary definition against the slides and textbook. Report anything you couldn't verify rather than guessing.
- `shasum` of the decks, `Chapter PPTs and Other Study Materials/Speaker Notes/` and `Textbook Links/` is unchanged before and after.
- **Tell the user each time:**
  - what's done and each file's page count;
  - anything not verified;
  - print steps: LibreOffice or Word, paper size US Letter (this Mac's printer queue defaults to A4), scale 100%; print odd pages, put the stack back in, then print even pages.

## Progress
(Update as you work: date, what was done, what's next, decisions, problems.)
- 2026-10-28 (Claude Code): PLANS.md created. Step 0 done: AGENTS.md section rewritten (short summary), full how-to in `Slide Notes Tools/PRINTED_NOTES.md`. venv at /tmp/printnotes-venv. Note: `Printed Exam Notes/~$ 23 Printed Notes.docx` is a stale Word lock file from Oct 25 (Word isn't running); left in place.
- Stage 1: guide text lives in `Slide Notes Tools/quick_guides.py` (`QUICK_GUIDE`, imported by print_notes_data.py once rendering is added). Ch 23 guide WRITTEN.
- All five guides WRITTEN in quick_guides.py (Ch 23-27, about 800-1500 words each), from the slides and study guide; not yet machine-checked.
- Next: add a citation check for the guides + guide rendering (gray/thin box, bookmarks, section pointers) to build_print_docx.py, then build `Unit 2 Quick Guides.docx` (all five) and rebuild Ch 23 with its guide.
- 2026-10-28 (Claude Code, cloud session): user feedback: (1) the Ch 24–27 guides were thinner than Ch 23's; expand all to Ch 23's depth, 10 pages total is fine; (2) remove the box around each column (keep the column line). Done:
  - Ch 24–27 guides rewritten from the slides, text alternatives, study guide and textbook (1,600–2,160 words each; Ch 23 1,550). `Unit 2 Quick Guides.docx`: 10 pages at 11 pt, about 2 per chapter. Citation check passes.
  - Guide styles no longer have paragraph borders (in two columns they drew a box around each column). The page-1 how-to box keeps its border; its pBdr is now placed where the Word schema wants it (the validator had flagged it).
  - Builder runs on Linux too: `soffice` from PATH, and Liberation Sans Narrow (apt `fonts-liberation-sans-narrow`, same letter widths as Arial Narrow) for measuring and the font check. Mac behavior unchanged.
  - Slide-text reader (build_print_notes.py) now reads equation text (a14:m: e.g. "Ethylene (H2C=CH2)", "Pr", "Pfr", "H+") and text boxes inside mc:AlternateContent, which python-pptx skipped (26.1.10, 26.1.20, 26.3.37, 26.3.38 were empty), and whole multi-line titles (26.2.31, 26.2.33, 27.1.4, 27.4.40).
  - Ch 23 rebuilt as main + index: 12.25 pt, 15 + 5 = 20 pages, all checks pass (interim size; Stage 3 sets the final shared size).
  - Found for Stage 2: 25.2.21 and 25.3.41 have ion symbols as MathType OLE pictures: (H+), (K+), (NO3− and HPO4²−), H+, K+ (rebuild those slides' sentences in the data); 24.5.52's text alternative says CO2 leaves the leaf (it enters: correction); 24.4.42 lists only bark and pith (wood missing); textbook p. 437 says monocot roots have secondary growth but p. 440 says only conifers and woody eudicots do (slide 24.3.30 says they don't); hypocotyl: 27.2.22 "stem" vs 27.2.24 figure "root axis".
- Stage 2 done (same day): Ch 24, 25, 26, 27 data in print_notes_data.py (one block per chapter at the end of the file) and their main + index files. Per chapter: textbook captions and figure descriptions (24.3.33, 24.5.55, 26.1.15, 26.1.19, 26.3.43, 27.1.18 and others), corrections, comparison tables, look-alikes, sequences, n/2n/3n (Ch 27), uses, clue index, glossary (textbook definitions, mostly its glossary at PDF pp. 921–946), term index (audited for false hits).
  - Corrections added: 24.3.27 lignin; 24.4.42 woody stems (+ wood missing from the regions); 24.5.52 CO2 enters; 25.1.4 N missing; 25.2.19 wording; 25.3.30 tracheids have pits, not perforation plates; 25.3.34 wilted cell's potentials are all lower inside; 26.1.17 abscission is ethylene's; 26.2.29 roots; 26.3.41 mislabeled text alternative (moved to 26.2.35); 27.1.5 microspore becomes; 27.2.24 hypocotyl; 27.2.26 part A is a eudicot.
  - New data fields: SLIDE_TEXT (rebuilt slide text: 24.1.15 heading, 25.1.16 soil layers, 25.2.21 and 25.3.41 ions), FIG_FIX (typos in figure text: "rhizone", "drape", "Cose", "(2,4-D)Gibberellins"), TEXT_ALT_MATCH value None (unlink a mislabeled text alternative). Photo credits and "Figure 25B"-style labels are filtered as junk. Term-index entries now apply only to their own chapter.
- Stage 3 done: full build (`build_print_docx.py`, --fit) chose 12.25 pt for all ten files; Ch 23 20 pages (15 + 5), Ch 24 14 (11 + 3), Ch 25 12 (10 + 2), Ch 26 11 (9 + 2), Ch 27 12 (10 + 2). All checks pass; every page looked at.
- Stage 4: AGENTS.md and PRINTED_NOTES.md updated.
- 2026-10-28, user follow-up (all done):
  1. Whole-unit files for printing in one go: `Unit 2 Printed Notes.docx` (58 pages) and `Unit 2 Index.docx` (16 pages), each chapter on a new right-hand page. Bug found and fixed on the way: LibreOffice's PDF export dropped the inserted blank pages, so stored page numbers would have been short by one or more after Ch 23; now `IsSkipEmptyPages` is false and the layout check compares every printed page number with the real page.
  2. Open questions follow the textbook: 24.3.30 monocot roots do undergo secondary growth (p. 437; correction added); 27.2.24 hypocotyl contributes to the stem (p. 496). Study guide §11 now lists every slide error found while building the notes.
  3. Old PDFs moved to `Printed Exam Notes/Old/`; stale `~$ 23 Printed Notes.docx` deleted; `Unit 2 Quick Guides.docx` kept and rebuilt by every full build.
  5. Guides resized by content, not to a target: one rule for every chapter (explain every high-priority concept; one line per item in organism lists; numbers, extra examples, uses and textbook-only extras left to the tables). Ch 23 gained the high-priority points it lacked (23.1.11 tissues, 23.1.15 spores vs seeds disperse, 23.5.81 features, 23.5.86–87 cell counts); Ch 24–27 lost repeats, examples, uses and textbook extras. Words: Ch 23 1,660; 24 1,880; 25 1,660; 26 1,550; 27 1,750.
  - Full build: 12.25 pt; Ch 23 20 pages, 24 14, 25 12, 26 11, 27 12; all checks pass.

## Sources for how this plan is written (official OpenAI guidance only)
- OpenAI Codex best practices: a prompt with Goal / Context / Constraints / Done when; `AGENTS.md`; `PLANS.md`; verification. https://learn.chatgpt.com/guides/best-practices
- OpenAI, "Using GPT-6": autonomy and follow-through, when to ask, reasoning effort, testing. https://developers.openai.com/api/docs/guides/latest-model
