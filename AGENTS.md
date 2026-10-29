# BIO II

## Exam content

According to the professor (in her email), what appears on the tests will come from the PowerPoints, but not necessarily directly. According to her, students have to understand what is in the PowerPoints, not just memorize the slides. But the best guide to what will come on the exams is the Past Unit Tests.

## Concept and definition questions

Whenever I ask to understand a concept or ask for the definition of a term, first check the PowerPoints (`Chapter PPTs and Other Study Materials/`) for an existing definition or explanation. If one exists, tell me the chapter and slide number where it is found, and base the explanation on it.

## Printed exam notes ("do the printed notes for chapter N" / "for Unit N")

The professor said on a video call (by Oct 25, 2026) that printed notes are allowed on the exams: basically open-book, but no pictures and no computer. This is the standard for Unit 2 and every later unit. When I ask for it, do the whole job to this standard without asking me to review drafts: build, verify (the checklist in `Slide Notes Tools/PRINTED_NOTES.md`), fix, rebuild, then report.

**Files**
- **Word documents only**, built by `Slide Notes Tools/build_print_docx.py` from the untouched decks plus `Slide Notes Tools/print_notes_data.py`, `index_data.py` (glossary and term index) and `quick_guides.py`. The PDF builder (`build_print_notes.py`) is legacy.
- **Titles:** each chapter starts with just `Ch. NN: <chapter name>` (e.g. `Ch. 24: Flowering Plants: Structure and Organization`); its index adds ` (index)`. No "BIO II printed notes", no "(main)", and no repeated chapter heading further down (my choice, Oct 28).
- **Two files per chapter**, each chapter done separately:
  - `Printed Exam Notes/Ch NN Printed Notes.docx`: the title, then every slide in order (figures as words, "Textbook:" corrections), then lookup tables. **No quick guide and no contents** in it. The **how-to-use box appears once per unit**, under the title of the unit's first chapter (Ch 23 for Unit 2), and in no other chapter.
  - `Printed Exam Notes/Ch NN Index.docx`: the title, then the chapter's **contents** (sections, slide groups and lookup tables with their pages in the main notes, then this file's parts), then the clue index, glossary and term index, and nothing else.
- **Slide codes stay chapter.section.slide** everywhere (e.g. 23.2.17). Page-based codes were considered and dropped (Oct 28).
- **Glossary = key terms:** the terms I need to understand the chapter or to answer its exam questions (look-alikes as pairs), plus the few unexplained words needed to follow the slides. Not "every term the slides don't define". Short plain definitions, each with the slide where it's defined.
- **Term index:** for each term, the main place (where it's defined, marked "(def.)") and then 2–3 other places that matter, spread out: never one within 2 slides of a place already listed (e.g. rhizoids: 23.2.17 (def.), 23.2.22, 23.4.52, but not 23.1.15 or 23.2.18). List a 3rd extra place only if it's still important or could come up on the exam. Each place gets a very concise keyword (one to a few words) saying what the term is about there, e.g. "23.2.22 (mosses)" (my choice, Oct 28).
- **Whole-unit files**, for printing in one go: every full build also writes `Unit N Printed Notes.docx` and `Unit N Index.docx` (each chapter starts on a new right-hand page; the unit index's contents give pages in the unit main file) and a reading copy of all the quick guides, `Unit N Quick Guides.docx`, the only place the quick guides appear. Keep all of them up to date with every rebuild. Superseded outputs go in `Printed Exam Notes/Old/`; stale Word lock files (`~$...`) can be deleted.

**Page budget and font**
- At most **10 double-sided sheets per chapter**, counting the main and index files as printed separately: each file rounds up to whole sheets (2 pages = 1 sheet), so a 15-page main file plus a 5-page index is 8 + 3 = 11 sheets.
- **One body font size for all chapter and unit files**, in half-point steps (Word can't store finer sizes); headings and the page header are fixed steps above or below it. Unit 2 is **11.5 pt** (my choice, Oct 28: everything half a point smaller than before). For a new unit, use the largest size that fits the budget with a page to spare (`--fit`). The Quick Guides reading copy stays at 11 pt.
- **The files I print, `Unit N Printed Notes.docx` and `Unit N Index.docx`, use my handwriting font, Handwriting Final**, for everything in them (text, bullets, headings, tables, page header and numbers), at the same sizes (my choice, Oct 28). The font file is `Slide Notes Tools/fonts/HandwritingFinal.otf` (`UNIT_FILE_FONT` in `print_notes_data.py`); it must be installed on the computer that prints or builds the files. The chapter files and the Quick Guides copy keep Arial Narrow. The sheet budget is checked on these whole-unit files too, and every build warns about any character the font has no glyph for (say which and where; ask me for a new font version rather than working around it).

**Quick guides** (only in the `Unit N Quick Guides.docx` reading copy)
- Written for someone who hasn't gone through the chapter: simple, clear language, short sentences, every term explained in plain words where it first appears. It must cover every important concept and the terms needed to understand the chapter and answer its exam questions, so I'm not lost during the exam.
- Concise: no filler and no repetition (don't re-explain an earlier chapter or repeat the intro in the first section). Uses, history, exact numbers, extra examples and textbook-only extras go to the lookup tables, not the guide.
- Say what each organism or example is, so contrasts make sense: living or extinct, and which group it belongs to (e.g. Cooksonia is an extinct early vascular plant, not a lycophyte).
- Don't make a slide's claim stronger: never add absolute words ("only", "all", "always", "every"); on Unit 1 they marked the wrong answers.
- Length follows from a deep review of each chapter, not a target: explain every high-priority concept, give organism-by-organism lists one line per item, and end each section with its look-alike traps. Every chapter gets the same depth (questions are spread evenly across chapters).

**Layout**
- Two columns, a column line, borders on all table cells (black is fine), no pictures, no shaded fills. No boxes around text in the columns: the only box is the how-to box at the start of the unit's first chapter (it and the titles span the page). The quick guides are plain text.

**Accuracy**
- Every fact traces to a slide (or its text alternative) or the textbook, with slide codes.
- When a slide and the textbook disagree, the textbook wins, also on points worth asking the professor about (my decision, Oct 28): print the correct version on the slide as a "Textbook:" note and add a row to the study guide's slide-errors list. Exception: when the textbook contradicts itself, follow the slide (e.g. 24.3.30, monocot roots don't undergo secondary growth).
- Check every chapter at the same depth, not just the first: compare every slide bullet with the textbook, read every figure description (text alternative) for garbled or wrong statements, and check every guide sentence, glossary definition and term-index keyword against its slides. Double-check every slide code and every contents page number (the build checks them against the files). Work from the text actually printed in the packets, not an older dump.

The full how-to (workflow for a new chapter, data fields, figure rules, verification checklist) is in `Slide Notes Tools/PRINTED_NOTES.md`; follow it. The current Unit 2 job and its progress log are in `PLANS.md`.

## Working with me

- After making changes: commit, push and open a new pull request. Don't watch it; I review and merge. If the last pull request was already merged, start the branch fresh from `main`.
- When I ask for a review, report what you find and change nothing.
- In the report, say what changed, what you found that's still open, and anything worth asking the professor.

## Slide speaker notes ("do the notes thing for chapter N")

When I ask for this for a chapter, do the whole job without asking me to review it: write the spec (including the EXAM FOCUS section for every content slide), build, double-check, fix, and report. Ch 23 is done and is the worked example (`Slide Notes Tools/ch23_notes_spec.py`).

### Why I want it

I read the slides in PowerPoint and handwrite notes on my iPad (OneNote, exported as PDF), numbered like the slides. The same concept often comes up on many slides, sometimes in detail several times. I want to write each concept once, in one place (its "home"), and have every other slide point to it. Where a slide uses a term it doesn't explain, I want a short definition so I don't have to look it up.

### Scope and files

- Folder layout in `Chapter PPTs and Other Study Materials/`:
  - The chapter decks themselves stay untouched, with their original names. Never modify, rename or move them.
  - `Speaker Notes/`: one deck per chapter with the notes, named `<original name> (speaker notes).pptx`. Keep only the latest version: each build replaces the file; don't keep numbered versions.
  - `Speaker Notes/Working copy/`: used when I'm studying a speaker-notes deck (it's open in PowerPoint, or I say I'm using it). Build the new version here with the same file name, using `--only CH --out "<that path>"`, so the open file, the other decks and the PowerPoint app aren't touched. Move it into `Speaker Notes/` (replacing the old one) only when I say so. If the working copy itself is open (`~$` lock file next to it), don't overwrite it: the script refuses unless given `--force`. Build and verify the new version in the scratchpad instead (`--out <scratchpad path>`), then ask me to close the working copy and copy it over once I have.
  - `Textbook Links/`: the Ch 23 deck with textbook links and its `Ch23_Textbook_Links/` PDF folder. The links are relative, so the deck and that folder must stay together.
  - `Other/`: other study materials.
- Don't delete files; replacing the latest speaker-notes deck (or printed-notes PDF) with a better build is the one exception.
- Unit 2 decks: Ch 23, 24, 25, 26, 27. The Ch 25 deck (`Mader_Biology2024Release_PPT_Ch25_ACCESS.pptx`, posted Oct 22) is from the 2024 Release edition, the same edition as the textbook; the other decks are 14th edition.
- Never reference Ch 20-22 at all.
- Tools: `Slide Notes Tools/build_slide_notes.py` builds every deck that has notes from all `chNN_notes_spec.py` files in that folder. It reads the untouched originals and writes only into `Speaker Notes/` (or to the path given with `--out`). For a new chapter, write `chNN_notes_spec.py` with the same fields as the Ch 23 spec, then run the script with a venv that has python-pptx (create one in the scratchpad: `python3 -m venv venv && venv/bin/pip install python-pptx`). Use `--check --dump file.txt` for a dry run that writes the notes to a text file for review.
- Concept keys are shared across specs: reuse an existing key (and its home) when a concept already has one. If a later chapter's slide adds detail to a home in an earlier deck, list it in the new spec's ADDS and the script puts it in that earlier deck's home note.
- A full build rewrites every speaker-notes deck (the new chapter's and any deck holding a home it points to). Before writing, check none of them is open in PowerPoint (`~$` lock file in `Speaker Notes/`). If one is, build into `Speaker Notes/Working copy/` instead (see above), or, if a full build is needed, tell me which decks to close first.
- Don't open, control or script the PowerPoint app unless I ask. Do all edits with python-pptx and verify without PowerPoint (see "Before finishing").

### Format

- Refer to slides as chapter.section.slide, e.g. (23.1.12). Section = the last "NN.N" section-title slide at or before the slide. Hidden text-alternative slides at the end get no notes.
- Sections, in this order, with exactly these headings (omit empty ones):
  1. CLARIFICATION: only where the slide is wrong or misleading (e.g. a wrong definition, a picture that doesn't match the title).
  2. IMAGE DESCRIPTION: the picture's text alternative. If a full text alternative exists (hidden slide at the end, linked from "Access the text alternative"), show only that; show the short alt text instead when there's no full one, and both when the short one says something the full one doesn't.
  3. NOT EXPLAINED ON ANY SLIDE: "• Term: definition" for terms no slide in the Unit 2 decks explains. Only on the first slide that needs it.
  4. NOT EXPLAINED YET: "• Term: definition (home code)" for a concept the slide needs whose home comes later. Repeat on every slide that needs it, up to the home (see Rules).
  5. HOME NOTE: "• Concept name" for each concept whose home is this slide and that another slide points to. Under it, "Also write here:" then one line per source slide, "– Slide Title (code): details", with several details from the same slide on one line. Put "why" explanations here too ("– Why ...: ...").
  6. ADDS TO: one line, "Concept (code) · Concept (code)": this slide has details that were copied into those home notes.
  7. COVERED ELSEWHERE: one line, same format: concepts this slide explains (at least partly) but that add nothing beyond their home.
  8. EXAM FOCUS (High / Medium / Low): always the last section; required for every content slide whenever this task is done for a chapter (see "Exam focus" below).
- No slide titles or "later/earlier" in references (titles only in "Also write here" lines). No figure or table numbers anywhere. No "(brief definition)"-style explanations in headings.

### Rules

- Home = the slide, in any Unit 2 deck, that explains the concept in the most detail. Homes can be in later chapters; those decks get a small HOME NOTE block on the home slide (other slides in those decks are left alone until that chapter is done).
- Group concepts the way the textbook does (its sub-headings and bullet lists), with fewer, bigger homes, not one home per slide. A summary or overview slide (e.g. a "Characteristics of ..." table) is not a home; it just points outward with COVERED ELSEWHERE / NOT EXPLAINED YET. Don't give a home to a one-line point; fold it into the concept it belongs to.
- ADDS TO / Also write here: when a slide has a detail about a concept whose home is elsewhere, copy the detail into that home's note so I can write everything in one place without flipping, and leave the one-line ADDS TO pointer on the source slide. Put each detail in the home it is most naturally about. Picture slides that follow a text slide usually add to (or are covered by) that slide's home. Write each detail so it makes sense to someone who hasn't read the source slide yet.
- A concept only counts as explained at its home (its main explanation). On each slide that touches a concept:
  - Before the home, and the slide only mentions the concept: NOT EXPLAINED YET with a definition, if I need it to follow the slide. This holds even if an earlier slide gave a short or partial explanation.
  - Before the home, and the slide explains the concept itself: just the COVERED ELSEWHERE or ADDS TO pointer, no definition.
  - After the home: COVERED ELSEWHERE or ADDS TO if the slide explains it; nothing if it only mentions it.
  - If the home is in a later chapter (Ch 24-27), every slide in the current chapter that needs the concept gets the definition, pointing to that later home (e.g. ovule gets defined on about 12 Ch 23 slides, pointing to 27.1.14).
- Only define a concept where I need it to follow the slide, and never something I already know (see below). Don't define a word just because it appears.
- What counts as "explains it itself": a dedicated bullet, a described picture, or a table row that gives several facts (e.g. the bryophytes row of the Characteristics table). A one-line table entry (e.g. "Lycophyte leaves are microphylls with a single, unbranched vein"), a parenthetical, a passing clause or a label is only a mention.
- Steps of a life-cycle figure that is built up over several slides (e.g. moss, fern and pine cycles) point to the full figure's home with COVERED ELSEWHERE; they still get NOT EXPLAINED YET definitions for concepts whose home is later.
- Lists of group names (e.g. the groups on a cladogram, or "conifers, cycads, ginkgoes, gnetophytes") get a short definition of each group, since the slide is about how they relate.
- Definitions: short, plain words, accurate, enough for someone new to the idea to follow the slide. Make them specific to the slide's situation when that helps (e.g. on a moss slide, "the gametophyte is the leafy moss plant").
- What I already know (don't define): BIO I basics (mitosis, meiosis, haploid/diploid, gametes, zygote, fertilization, genes/alleles, chromosomes, cell parts), MYA, morphological, germination, embryo in its everyday sense, everyday words. What I don't know or only partly know (define): e.g. aerial stem, extant, substrate, uninucleated. When in doubt, define it.
- Be concise: cut anything that doesn't help me write or understand the notes, but keep every important fact.
- Slide vs textbook: when they disagree, follow the textbook (she confirmed this on Oct 22) and put the correct version in CLARIFICATION. Also list it in the study guide's slide-errors section, and suggest I ask her if it matters for the exam.

### Exam focus

- Goal: tell me, per slide, what the professor will probably ask, what she won't, how she'll ask it, and what to write in my notes. Keep it concise.
- Evidence to use: `Exam Pattern Analysis.md`, the past exams in `Past Unit Exams/` (wording and question types), `Unit 2 Study Guide.md` (key terms, look-alikes, slide errors, what to skip, learning objectives), and her emails in `Emails b:w me and professor/`. Update the patterns when a new past exam is added.
- Format (spec field `EXAM`): heading "EXAM FOCUS (High/Medium/Low)", then four parts; each can be one line or a short bulleted list:
  - "Likely:" the facts she'd test, in the slide's wording. Use bullets when there are several, so it's quick to scan.
  - "Unlikely:" what to skip on this slide. If there's nothing to skip, say "Nothing to skip; every point here is testable."
  - "How:" sample questions in her style, each with the answer and the trap (usually the look-alike term from the same slide). Dense slides get two or three questions (Unit 1 asked up to three from one slide); others get one.
  - "Write:" what goes in my handwritten notes. Where a table or box belongs, give it filled in (title, then the actual rows), not just its column names.
- "Write" follows the home-note system: each table or box is written in full on one slide only (e.g. the bryophyte table on the first bryophyte-group slide, with rows from the later slides); other slides say "Nothing here; it's the ... row of the table at (code)". Don't tell me to write the same thing in two places.
- The outline slide also gets the trap reminder: look-alike terms, absolute words (never correct on Unit 1), terms borrowed from other chapters.
- Concise means no filler, not thin: don't cut facts, questions or table rows that would help on the exam.
- Life-cycle frames, photos that repeat a bullet slide, and figures already covered by their text slide get a one-line pointer, e.g. "EXAM FOCUS (Low): Step 4 of the moss cycle (...); see 23.2.30." The title and end slides get nothing; the outline slide gets one line on question order.
- Priority, from the Unit 1 pattern: High = opening sections, definitions, life cycles, big comparison tables, "which group/structure" facts; Medium = organism-by-organism diversity slides; Low = photos, frames, uses, history, exact numbers and dates, branching details of phylogeny trees.
- Numbers, dates and uses (her Oct 22 email): know the major patterns and the sequence of evolutionary events (Medium or higher; e.g. which group came first and what each step added), not exact species counts or MYA. For uses, know the main examples and why they matter biologically, one line each.
- Every "Likely" must trace to the slide's text or text alternative. Don't promise anything is safe to skip: "Unlikely" means lower priority.
- Weighting (I confirmed this is what I want): what she actually asked on past exams counts most; what she said she'd do counts where it agrees with the exams or fills a gap; what she only said was possible (e.g. identifying structures in diagrams) counts least. When her words and the exams disagree, go with the exams.

### Before finishing

- Final deep pass (required every time speaker notes are added or changed, before reporting done): read every slide's complete notes in the dump, especially EXAM FOCUS, the way I'd use them while studying, and check both that they're as useful as they can be and that there are no errors:
  - every fact, definition and gathered detail matches the slide (or its text alternative) and the textbook
  - every practice question has an answer and a trap, and the trap is really wrong (not a correct answer under another name, e.g. a composite head is also an inflorescence)
  - claims about past exams are accurate (which question, which chapter)
  - every "it goes in / row of the table at (code)" points to a slide whose Write actually has that table or box, and each table is written in full only once
  - every typed chapter.section.slide code matches the deck
  - priorities follow the rules, filler is gone, and the same fact is worded consistently across slides
  - mechanical checks back up the read-through: questions without "Trap", bad codes, dangling table references, plus the keyword scans below
  - fix everything found, rebuild, and in the report say what was fixed, including any mistake in my own earlier messages
- Do the final pass on a dry run first (`--check --dump file.txt`), then check the built decks.
- Keyword scan (hand review alone misses things): dump each slide's text plus its image descriptions and text alternatives, then for every concept grep all its word forms (singular/plural, -ous/-y, related terms) on every slide. List the hits before each concept's home that aren't handled, and separately the hits after the home. Make sure each hit is handled correctly (NOT EXPLAINED YET, COVERED ELSEWHERE, ADDS TO, or nothing), and that no "covered" slide actually has a new detail that should be an ADDS TO.
- Check every definition and gathered detail against the slides and the textbook (`Official Textbook/`, PDF page = book page + 19 for this edition) for accuracy.
- After writing, verify without PowerPoint:
  - zip test
  - reload with python-pptx: same slide count, hidden slides and shape IDs as the original; original notes kept
  - checksums before and after of every file that must stay untouched (the originals, any deck open in PowerPoint, decks not being rebuilt)
  - `qlmanage -t -s 800 -o <scratch dir> "<deck>"` renders a thumbnail with macOS Quick Look, not PowerPoint
- Only if I ask for a PowerPoint check: copy the deck into `~/Library/Containers/com.microsoft.Powerpoint/Data/` (PowerPoint is sandboxed), open it with `osascript` wrapped in a time limit (`perl -e 'alarm 60; exec @ARGV' osascript ...`, since PowerPoint can hang if a dialog is open), close it without saving, and delete the copy.
