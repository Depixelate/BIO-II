"""Data for build_print_notes.py: everything printed besides the slides themselves.

Slides are (chapter, slide number), like the specs; the tool turns them into codes (23.2.17). Every entry must trace
to a slide (or its text alternative) or, where marked, to the textbook (PDF page = book page + 19).
"""

CHAPTERS = [23]
CHAPTER_NAMES = {
    23: "Plant Evolution and Diversity",
    24: "Flowering Plants: Structure and Organization",
    25: "Flowering Plants: Nutrition and Transport",
    26: "Flowering Plants: Control of Growth Responses",
    27: "Flowering Plants: Reproduction",
}


def s23(*ns):
    return [(23, n) for n in ns]


# page 1: how wrong answers looked on Unit 1 (Exam Pattern Analysis.md, sections 1 and 8)
REMINDERS = [
    "Answers with “only”, “all”, “always”, “exclusively”, “must” or “every” were wrong every time (22 of 22).",
    "Drop answers that put a term from another chapter into the wrong organism (e.g. peptidoglycan in a plant).",
    "The believable wrong answer is usually the look-alike term from the same slide: check the look-alike table.",
    "Questions follow slide order, so the questions before and after tell you which section to look in.",
    "Diagram questions ask about the process (n or 2n, where meiosis happens), not label names.",
]

# ---------------------------------------------------------------- slides and figures
# text alternatives the deck doesn't hyperlink to their slide: {chapter: {slide: hidden slide}}
TEXT_ALT_MATCH = {}
# hidden "text alternative" slides that belong to no content slide (e.g. the title photo's): {chapter: {slides}}
TA_SKIP = {23: {93}}   # 93: "Accessibility Content" cover slide

# life-cycle figures built up over several slides: the full description is printed once, on the final frame
CYCLES = {
    23: [
        {"name": "moss life cycle", "frames": range(23, 31), "final": 30},
        {"name": "fern life cycle", "frames": range(45, 53), "final": 52},
        {"name": "pine life cycle", "frames": range(60, 69), "final": 68},
    ],
}
# what each earlier frame shows, for its one-line pointer (step names from the final frame's text alternative)
FRAMES = {
    (23, 23): "Step 1 (mature gametophytes)", (23, 24): "Step 2 (fertilization)", (23, 25): "Step 3 (zygote)",
    (23, 26): "Step 4 (sporophyte)", (23, 27): "Step 5 (spores)", (23, 28): "Step 6 (spore dispersal)",
    (23, 29): "Step 7 (immature gametophyte)",
    (23, 45): "Overview (the dominant sporophyte)", (23, 46): "Step 1 (sporophyte)", (23, 47): "Step 2 (sporangia)",
    (23, 48): "Step 3 (spores)", (23, 49): "Step 4 (gametophyte)", (23, 50): "Step 5 (fertilization)",
    (23, 51): "Step 6 (zygote)",
    (23, 60): "Overview (the tree)", (23, 61): "Step 1 (pollen and seed cones)",
    (23, 62): "Step 2 (pollen sacs and ovules)", (23, 63): "Step 3 (microspores and megaspores)",
    (23, 64): "Step 4 (pollen grains)", (23, 65): "Step 5 (mature female gametophyte)", (23, 66): "Step 6 (zygote)",
    (23, 67): "Step 7 (sporophyte and seeds)",
}
# what a frame says that the final frame's description doesn't
FRAME_EXTRA = {
    (23, 60): "The tree is the diploid (2n) sporophyte, the most prominent structure in the pine life cycle; "
              "it bears both pollen cones and seed cones.",
}
# figure sentences deliberately not printed: (chapter, slide) -> {start of the sentence: reason}
FIG_SKIP = {
    (23, 27): {"Step 5, of the cycle": "frame label only"},
    (23, 62): {"Step 2 compares": "frame label only"},
    (23, 65): {"Step 5 illustrates": "frame label only"},
    (23, 66): {"Step 6 illustrates": "frame label only"},
    (23, 67): {"Step 7 illustrates": "frame label only"},
}
# slides whose short alt text is printed as well as the full text alternative, because it says something useful
PRINT_BOTH = {(23, 13)}


def cycle_of(ch, n):
    for c in CYCLES.get(ch, []):
        if n in c["frames"]:
            return c
    return None


def frame_line(ch, n, cycle, final_code):
    step = FRAMES.get((ch, n))
    return f"{step or 'A step'}; full description at {final_code}."


# textbook captions, only where the slide's short alt text leaves out what the figure shows (credits removed)
CAPTIONS = {
    (23, 8): "The charophytes (represented here by Chara and Coleochaete) are the green algae most closely related "
             "to the land plants.",
    (23, 39): "Whorls of branches and tiny leaves are at the nodes of the stem. Spore-producing sporangia are borne "
              "in strobili.",
    (23, 41): "Psilotum has no leaves; the branches carry on photosynthesis. The sporangia are yellow.",
    (23, 59): "Pine trees are the most common of the conifers. The pollen cones (male) are smaller than the seed "
              "cones (female) and produce pollen.",
    (23, 71): "Cycads may resemble ferns or palms, but they are cone-producing gymnosperms.",
    (23, 79): "Analysis of molecular data suggests that Amborella trichopoda is the most closely related to the "
              "first flowering plants.",
    (23, 85): "A flower has four main parts: sepals, petals, stamens, and carpels. A stamen has an anther and "
              "filament. A carpel has a stigma, style, and ovary. An ovary contains ovules.",
    # 23.1.15's text alternative only lists labels; the caption says what the diagram shows
    (23, 15): "Notice the reduction in the size of the gametophyte and the increase in the size of the sporophyte "
              "among these representatives of today's land plants. This trend occurred as these plants became adapted "
              "for life on land. In the moss and fern, spores disperse the gametophyte. In gymnosperms and "
              "angiosperms, seeds disperse the sporophyte.",
}
# the textbook's description of a process, where neither the text alternative nor the caption explains a diagram
PROCESS = {}

# slide errors, printed on the slide as "Textbook: ..."
CORRECTIONS = {
    (23, 22): "The protonema is only the first, thread-like stage of the moss gametophyte (a spore germinates into "
              "a male or female protonema, 23.2.30); it then produces the leafy shoots.",
    (23, 34): "Homosporous means making one type of spore, which grows into a gametophyte that makes both eggs and "
              "sperm. The slide's “one type of gamete” should read “one type of spore.”",
}
# scanning errors in a slide's text, fixed paragraph by paragraph: (chapter, slide) -> [(wrong, right)].
# The 23.1.4 table is a scan of textbook Table 23.1 (book p. 408); its rows are restored from the textbook's wording.
TYPO_FIX = {
    (23, 4): [
        ("KINGDOM Plantae", "KINGDOM: Plantae"),
        ("Multicellular; apical tissue produces specialtzed tissues altemations-of- generation life cycle: protection "
         "of the embryo: gametangla produces gametes waxy cuticle prevents water loss",
         "Multicellular; apical tissue produces specialized tissues; alternation-of-generations life cycle; protection "
         "of the embryo; gametangia produces gametes; waxy cuticle prevents water loss."),
        ("Nonvascular Plants The Bryophytes", "Nonvascular Plants—The Bryophytes"),
        ("Liverworts, hornworts, and mosses are low lying and live in moist environments. Dominant gametophyte "
         "produces flagellated sperm unbranched, dependent sporophyte produces windblown spores.",
         "Liverworts, hornworts, and mosses are low-lying and live in moist environments. Dominant gametophyte "
         "produces flagellated sperm; unbranched, dependent sporophyte produces windblown spores."),
        ("Seedless Vascular Plants - The Lycophytes", "Seedless Vascular Plants—The Lycophytes"),
        ("Dominate branched sporophyte has vascular tissue: Lignified xylem transports water, and phloem transports "
         "organic nutrients: typically has roots, stems and leaves sporangia borne on sides of leaves that produce "
         "windblown spores Independent and separate gametophyte produces flagellated sperm.",
         "Dominant, branched sporophyte has vascular tissue: lignified xylem transports water, and phloem transports "
         "organic nutrients; typically has roots, stems, and leaves; sporangia borne on sides of leaves that produce "
         "windblown spores; independent and separate gametophyte produces flagellated sperm."),
        ("Seeded Vascular Plants–The", "Seeded Vascular Plants—The"),
        ("Leaves are megaphylls: dominant sporophyte produces heterosperes that become dependent male and female "
         "gametophytes Male gametophyte",
         "Leaves are megaphylls; dominant sporophyte produces heterospores that become dependent male and female "
         "gametophytes. Male gametophyte"),
        ("Gymnosperms are cone bearing: sporophyte bears pollen cones. which produce windtown pollen (male "
         "gametopyte, and seed cones which produce seeds",
         "Gymnosperms are cone-bearing; sporophyte bears pollen cones, which produce windblown pollen (male "
         "gametophyte), and seed cones, which produce seeds."),
        ("which produce pollen grain and beat vules within an ovary Following double fertilization",
         "which produce pollen grains, and bear ovules within an ovary. Following double fertilization"),
        ("Fruit develops from ovary", "Fruit develops from ovary."),
    ],
}

# a slide's text rebuilt where the deck splits sentences around pictures of symbols (MathType objects such as "H+"):
# (chapter, slide) -> [paragraph, or (level, paragraph)]; every original fragment must still appear in it
SLIDE_TEXT = {}
# typos in a figure's text alternative, fixed when printed: (chapter, slide) -> [(wrong, right)]
FIG_FIX = {}

# page budget per chapter, main file + index file together, in double-sided sheets (the user's choice)
SHEETS_PER_CHAPTER = 10

# ---------------------------------------------------------------- lookup pages
# tables: {"ch", "title", "slides", "head", "rows", "wide"}; a row is cells, or (cells, slides) to cite slides;
# a "note" entry is a title plus one line of text
TABLES = [
    {"ch": 23, "title": "Plant groups", "slides": s23(4, 16, 32, 34, 36, 55, 56, 57, 77), "wide": True,
     "head": ["Group", "Examples", "Vascular tissue", "Dominant generation", "Leaves", "Spores", "Seeds / fruit",
              "Sperm reach the egg by"],
     "rows": [
         ["Bryophytes (nonvascular)", "liverworts, hornworts, mosses",
          "none, so low-lying; no true roots, stems or leaves", "gametophyte; sporophyte unbranched, dependent",
          "no true leaves", "windblown", "none", "flagellated sperm swim in a film of water"],
         ["Lycophytes (seedless vascular)", "ground pines, spike mosses, quillworts", "yes (lignified xylem, phloem); roots",
          "sporophyte; gametophyte independent, separate", "microphylls (one unbranched vein)",
          "windblown, from strobili; homosporous or heterosporous", "none", "flagellated sperm (need water)"],
         ["Pteridophytes (seedless vascular)", "ferns, horsetails, whisk ferns", "yes",
          "sporophyte; fern gametophyte independent", "megaphylls (branched veins); whisk ferns have none",
          "windblown; ferns: in sori; horsetails: in strobili", "none", "flagellated sperm swim in a film of water"],
         ["Gymnosperms (seed plants)", "conifers, cycads, ginkgoes, gnetophytes", "yes",
          "sporophyte; gametophytes dependent", "megaphylls (pine needles)", "heterosporous; spores kept, not released",
          "“naked” seeds, not enclosed by fruit; mostly on cones",
          "pollen tube; no external water (cycads, ginkgo: multiflagellated sperm swim from the burst tube)"],
         ["Angiosperms (seed plants)", "flowering plants: monocots, eudicots", "yes", "sporophyte; gametophytes dependent",
          "megaphylls", "heterosporous; spores kept", "seeds enclosed in the ovary, which becomes the fruit",
          "pollen tube carries 2 sperm; double fertilization; no external water"],
     ]},
    {"ch": 23, "title": "Life cycles compared", "slides": s23(30, 52, 68, 86, 87, 88, 89), "wide": True,
     "head": ["", "Moss", "Fern", "Pine", "Flowering plant"],
     "rows": [
         ["Dominant", "gametophyte (the leafy shoots)", "sporophyte; both generations independent",
          "sporophyte (the tree, 2n)", "sporophyte"],
         ["Meiosis in", "capsule (the sporangium) on top of the sporophyte",
          "sporangia in sori under the leaflets (covered by the indusium)",
          "pollen sacs under pollen-cone scales → 4 microspores; ovules on seed-cone scales → 4 megaspores, 1 survives",
          "anther's pollen sacs → microspores; ovule → 4 megaspores, 3 disintegrate"],
         ["Gametophyte", "spore → protonema (first stage) → leafy shoots with antheridia or archegonia",
          "spore → prothallus: archegonia at the notch, antheridia at the tip",
          "male: winged pollen grain; female: in the ovule, 2–6 archegonia with one egg each",
          "male: pollen grain (tube cell + generative cell → 2 sperm); female: embryo sac (8 nuclei: egg, 2 polar nuclei)"],
         ["Fertilization", "flagellate sperm swim in external water to the archegonia",
          "needs moisture: flagellated sperm swim in a film of water",
          "pollen tube digests toward the egg, releases 2 nonflagellated sperm; one fertilizes the egg",
          "pollen tube grows down the style to the ovule; double fertilization: sperm + egg → 2n zygote, "
          "sperm + 2 polar nuclei → 3n endosperm"],
         ["Then", "zygote stays in the archegonium; sporophyte = foot + stalk + capsule, always attached",
          "zygote grows in the archegonium; first leaf and roots appear; rhizome with fronds",
          "ovule → seed (embryo, reserve food, seed coat); in the fall of the second season the woody cone opens",
          "ovule → seed (embryo, endosperm, seed coat); ovary wall → fruit"],
         ["Dispersed as", "spores, by air currents", "windblown spores", "winged seeds",
          "seeds in fruits (wind, gravity, water, animals)"],
     ]},
    {"ch": 23, "title": "Land adaptations", "slides": s23(9, 11, 14),
     "head": ["Problem on land", "Solution"],
     "rows": [
         ["drying out", "waxy cuticle; tissues (lower surface-area-to-volume ratio than branched filaments)"],
         ["gas exchange through the cuticle", "stomata, mostly on the underside of leaves"],
         ["moving water up against gravity", "tracheids (vascular tissue)"],
         ["UV damage", "a diploid generation, which hides the effect of a single harmful allele"],
         ["(overall trend)", "dominant sporophyte: only sporophytes have vascular systems; the gametophyte shrinks "
                             "and becomes dependent"],
     ]},
    {"ch": 23, "title": "Bryophytes", "head": ["Group", "Key features"],
     "rows": [
         (["Liverworts", "thallose (flat thallus) or leafy (look like mosses); Marchantia has rhizoids; gemmae detach "
                         "and start new plants (asexual); stalks bear antheridia or archegonia; the sporophyte grows "
                         "from the fertilized egg in the archegonium, and its capsule releases spores"], s23(17, 18)),
         (["Hornworts", "small horn-like sporophytes grow continuously from thin gametophytes (both photosynthesize); "
                        "one chloroplast per sporophyte cell; moist, shaded places; cyanobacteria partners fix "
                        "nitrogen; asexual fragmentation"], s23(19, 20)),
         (["Mosses", "largest group of nonvascular plants; moist places; shrivel and turn brown when dry, revive "
                     "when it rains; peat, granite and true mosses; protonema → leafy shoots with rhizoids; "
                     "sporophyte = foot + stalk + capsule, always attached"], s23(21, 22)),
     ]},
    {"ch": 23, "title": "Seedless vascular plants", "head": ["Group", "Key features"],
     "rows": [
         (["Lycophytes", "roots (lower extensions of the stem); microphylls; strobili make spores by meiosis; "
                         "homosporous or heterosporous; ground pines, spike mosses, quillworts"], s23(34, 35)),
         (["Horsetails", "Equisetum; wet, marshy places; reduced leaves in whorls at the nodes; strobili at stem "
                         "tips; independent gametophytes; humidity-sensitive “spring-loaded” spores; silica makes "
                         "stems tough"], s23(38, 39)),
         (["Whisk ferns", "Psilotum, Tmesipteris; no leaves (Tmesipteris: appendages like reduced megaphylls); "
                          "horizontal rhizome; aboveground stems fork repeatedly; pumpkin-shaped sporangia on short "
                          "side branches"], s23(40, 41)),
         (["Ferns", "mostly warm, moist tropics; fronds (megaphylls) divided into leaflets; sori on the undersides; "
                    "dominant sporophyte; both generations independent"], s23(42, 43)),
     ]},
    {"ch": 23, "title": "Gymnosperm groups", "head": ["Group", "Key features"],
     "rows": [
         (["Conifers (most plentiful)", "cones; pine needles with a thick cuticle and recessed stomata; windblown "
                                        "pollen; the seed is the dispersal stage; monoecious"], s23(58, 59)),
         (["Cycads", "large, finely divided leaves at the top of the stem; very large cones; pollen and seed cones on "
                     "separate plants; insect-pollinated; multiflagellated sperm; plentiful in the Mesozoic "
                     "(dinosaurs ate the seeds)"], s23(70, 71)),
         (["Ginkgoes", "one species, Ginkgo biloba; dioecious; pollution-resistant; multiflagellated sperm"],
          s23(72, 73)),
         (["Gnetophytes", "3 genera; similar xylem; no archegonia; similar strobili; Gnetum (trees or vines with "
                          "leathery paired leaves), Ephedra (ephedrine), Welwitschia (two straplike leaves)"],
          s23(74, 75, 76)),
     ]},
    {"ch": 23, "title": "Flower parts", "slides": s23(83, 84, 85), "head": ["Part", "What it is / does"],
     "rows": [
         ["Sepals (together: calyx)", "protect the bud; usually green; may drop off or look like petals"],
         ["Petals (together: corolla)", "vary in size, shape and color; attract a particular pollinator"],
         ["Stamen (male)", "anther (sac that makes pollen) + filament (stalk holding up the anther)"],
         ["Carpel (female)", "stigma (sticky knob) + style (slender stalk) + ovary (encloses the ovules)"],
         ["After fertilization", "ovule → seed; ovary → fruit"],
     ]},
    {"ch": 23, "title": "Already a table on the slides",
     "note": "Monocots vs eudicots: 23.5.81 (examples on 23.5.80). Flower terms (complete, perfect, inflorescence, "
             "composite): 23.5.91. Characteristics of each plant group: 23.1.4."},
    {"ch": 23, "title": "Look-alikes", "head": ["These", "The difference"],
     "rows": [
         (["antheridia vs archegonia", "male gametangia (make sperm) vs female gametangia (make eggs)"], s23(12)),
         (["gametophyte vs sporophyte", "n, makes gametes by mitosis vs 2n, makes spores by meiosis"], s23(12)),
         (["gametangia vs sporangium", "where gametes are made (on the gametophyte) vs where spores are made "
                                       "(on the sporophyte)"], s23(12)),
         (["microphyll vs megaphyll", "one unbranched vascular strand (lycophytes) vs branched veins (ferns, seed "
                                      "plants)"], s23(34, 36, 37)),
         (["homosporous vs heterosporous", "one type of spore vs two (microspores and megaspores)"], s23(34)),
         (["microspore vs megaspore", "becomes the male gametophyte (pollen grain) vs the female gametophyte"],
          s23(34, 55)),
         (["strobili vs sori", "cone-shaped spore-making structures (lycophytes, horsetails, gnetophytes) vs "
                               "clusters of sporangia under fern fronds"], s23(34, 38, 74, 42)),
         (["rhizoids vs roots", "hair-like threads that anchor and absorb (bryophytes, fern gametophytes) vs true "
                                "roots (vascular plants; in lycophytes, lower extensions of the stem)"], s23(17, 34)),
         (["protonema vs prothallus", "first, thread-like stage of the moss gametophyte vs the fern gametophyte"],
          s23(30, 52)),
         (["gemmae vs spores", "groups of cells that detach from a liverwort (asexual) vs cells made by meiosis"],
          s23(17)),
         (["gymnosperm vs angiosperm", "ovules not fully enclosed at pollination (“naked” seeds) vs ovules enclosed "
                                       "in an ovary that becomes a fruit"], s23(56, 57)),
         (["monoecious vs dioecious", "one plant makes both pollen and seed cones (conifers) vs separate plants "
                                      "(ginkgo; cycads' cones are on separate plants)"], s23(58, 70, 72)),
         (["pollination vs fertilization", "pollen carried to the female part vs sperm uniting with the egg"],
          s23(55, 87, 88)),
         (["calyx vs corolla", "all the sepals vs all the petals"], s23(83)),
         (["stamen vs carpel", "male (anther + filament) vs female (stigma + style + ovary)"], s23(84)),
         (["complete vs perfect", "has all four flower parts vs has both stamens and carpels"], s23(91)),
         (["inflorescence vs composite", "a cluster of flowers vs what looks like one flower but is many tiny ones"],
          s23(91)),
         (["zygote vs endosperm", "sperm + egg, 2n vs sperm + 2 polar nuclei, 3n"], s23(88)),
         (["tube cell vs generative cell", "grows the pollen tube vs divides into the 2 sperm"], s23(87, 89)),
         (["multiflagellated vs nonflagellated sperm", "cycads and ginkgo (swim from the burst pollen tube) vs pine "
                                                       "and flowering plants"], s23(70, 72, 68, 89)),
     ]},
]

SEQUENCES = [
    {"ch": 23, "title": "Plant evolution, in order", "slides": s23(4, 6, 16, 32, 34, 36, 54, 55, 70, 78),
     "note": "freshwater green algae (charophytes protect the zygote) → bryophytes (first on land; no vascular "
             "tissue; dominant gametophyte) → first vascular plants such as Cooksonia (branched: more sporangia) and "
             "lycophytes (vascular tissue, roots, microphylls; dominant sporophyte) → pteridophytes (megaphylls; "
             "dominant from the late Devonian through the Carboniferous) → gymnosperms (seeds and pollen; no external "
             "water for fertilization; cycads plentiful in the Mesozoic) → angiosperms (flowers, fruit, double "
             "fertilization; Triassic fossil pollen; Amborella is the closest living relative of the first ones)"},
    {"ch": 23, "title": "Alternation of generations", "slides": s23(12, 13),
     "note": "sporophyte (2n) → meiosis in the sporangium → spores (n) → mitosis → gametophyte (n) → mitosis in "
             "the gametangia (antheridia: sperm; archegonia: eggs) → gametes (n) → fertilization → zygote (2n) → "
             "mitosis → sporophyte"},
    {"ch": 23, "title": "How a megaphyll evolved", "slides": s23(37),
     "note": "branched stem system → one branch dominates → side branches flatten into one plane → tissue fills the "
             "spaces between them → megaphyll"},
    {"ch": 23, "title": "Life cycles, step by step",
     "note": "Printed in full once each: moss 23.2.30, fern 23.4.52, pine 23.5.68, flowering plant 23.5.89; "
             "compared side by side in the Life cycles table."},
]

PLOIDY = [
    {"ch": 23, "title": "", "slides": s23(12, 13, 17, 56, 86, 88, 89), "head": ["", "Structures"],
     "rows": [
         ["n (haploid)", "spores (microspores, megaspores); every gametophyte: moss leafy shoots and protonema, fern "
                         "prothallus, pollen grain (male), embryo sac (female); antheridia and archegonia; eggs and "
                         "sperm; the polar nuclei (each n); tube cell, generative cell"],
         ["2n (diploid)", "zygote; every sporophyte: moss foot + stalk + capsule, the fern plant, the pine tree, the "
                          "flowering plant; sporangium; embryo; the ovary (sporophyte tissue) and the fruit it becomes"],
         ["3n (triploid)", "endosperm (sperm + 2 polar nuclei)"],
         ["Meiosis (2n → n)", "makes spores, in the sporophyte's sporangia: moss capsule; fern sporangia in sori; "
                              "lycophyte strobili; pine pollen sacs and ovules; the flowering plant's pollen sacs "
                              "(in anthers) and ovules"],
         ["Mitosis", "makes the gametes (in the gametangia); grows a spore into a gametophyte; grows the zygote into "
                     "a sporophyte"],
     ]},
]

USES = [
    {"ch": 23, "title": "", "slides": s23(21, 53, 69, 72, 74, 77), "head": ["Source", "Use (and why)"],
     "rows": [
         (["Peat moss", "improves the water capacity of soil; was a battlefield wound dressing; great commercial "
                        "and ecological importance"], s23(21)),
         (["Ferns", "edible ferns (food); Native Americans: astringent to stop bleeding in childbirth; florists, "
                    "ornamentals"], s23(53)),
         (["Maidenhair fern", "cold medicine"], s23(53)),
         (["Tropical tree ferns", "building wood, because it resists decay, especially by termites"], s23(53)),
         (["Pines", "parks and gardens (beauty, smell); needles and bark rich in vitamins A and C → teas for colds "
                    "and coughs; pine nuts (large seeds) in cooking; pine oil scents products"], s23(69)),
         (["Ginkgo", "pollution-resistant street and park trees; seeds a delicacy in Asia; extracts to improve "
                     "blood circulation"], s23(72)),
         (["Ephedra", "ephedrine, a medicine with serious side effects"], s23(74)),
         (["Angiosperms", "all fruits, vegetables, nuts, herbs and grains (staples of the human diet); clothing, "
                          "food, medicines"], s23(77)),
     ]},
]

# clue index: (group, [(clue in a scenario's words, answer, slides)])
CLUES = [
    ("Organisms and groups", [
        ("closest green-algal relatives of land plants; they protect the zygote", "charophytes (Chara, Coleochaete)", s23(5)),
        ("green alga with an unprotected embryo", "Oedogonium", s23(7)),
        ("first plants to colonize land; no vascular tissue; low-lying", "bryophytes", s23(16)),
        ("flat, ribbon-like body (thallus); gemmae; umbrella-shaped stalks with archegonia", "liverworts (Marchantia)", s23(17, 18)),
        ("horn-like sporophytes that keep growing; one chloroplast per cell; cyanobacteria partners", "hornworts (Anthoceros)", s23(19, 20)),
        ("looks dead and brown when dry, turns green after rain; largest nonvascular group", "mosses", s23(21)),
        ("improves soil's water capacity; old battlefield wound dressing", "peat moss", s23(21)),
        ("early fossil, a few cm tall, branched, sporangia at the branch tips", "Cooksonia", s23(32, 33)),
        ("leaves with one vascular strand; ground pines, spike mosses, quillworts", "lycophytes", s23(34)),
        ("dominant from the late Devonian through the Carboniferous; megaphylls; no seeds", "pteridophytes", s23(36)),
        ("silica in the stems; whorls of tiny leaves at the nodes; “spring-loaded” spores", "horsetails (Equisetum)", s23(38, 39)),
        ("no leaves; stems fork repeatedly; pumpkin-shaped sporangia", "whisk ferns (Psilotum)", s23(40, 41)),
        ("fronds; sori on the undersides; both generations independent", "ferns", s23(42, 43)),
        ("cold medicine", "maidenhair fern", s23(53)),
        ("termite-resistant building wood", "tropical tree ferns", s23(53)),
        ("“naked” seeds, not enclosed by a fruit", "gymnosperms", s23(56, 57)),
        ("needles with a thick cuticle and recessed stomata; one plant makes both cone types", "conifers (pines)", s23(58)),
        ("vitamin A and C teas; pine nuts; pine oil", "pines", s23(69)),
        ("insect-pollinated gymnosperm; huge cones on separate plants; dinosaurs ate its seeds", "cycads", s23(70)),
        ("sperm with many flagella swim out of a burst pollen tube", "cycads and ginkgo", s23(70, 72)),
        ("one surviving species; separate seed and pollen trees; survives city pollution", "Ginkgo biloba", s23(72)),
        ("no archegonia; three genera", "gnetophytes", s23(74)),
        ("source of ephedrine", "Ephedra (gnetophyte)", s23(74, 75)),
        ("only two huge straplike leaves that fray; southwestern Africa", "Welwitschia (gnetophyte)", s23(74, 76)),
        ("trees or climbing vines with broad, leathery leaves in pairs", "Gnetum (gnetophyte)", s23(74)),
        ("ovules always enclosed in diploid tissue; flowers and fruit", "angiosperms", s23(56, 77)),
        ("living plant most closely related to the first flowering plants; New Caledonia", "Amborella", s23(78, 79)),
        ("long the earliest known angiosperm fossil, with fruit and flowers", "Archaefructus", s23(78)),
        ("corn, tulips, pineapples, sugarcane", "monocots", s23(80)),
        ("cacti, strawberries, dandelions, poplars, beans", "eudicots", s23(80)),
    ]),
    ("Structures", [
        ("waxy, waterproof covering that prevents drying out", "cuticle", s23(9)),
        ("small openings, mostly under leaves, for gas exchange", "stomata", s23(9)),
        ("cells that carry water up against gravity", "tracheids", s23(9)),
        ("where sperm / eggs are made on a gametophyte", "antheridia / archegonia (gametangia)", s23(12)),
        ("where spores are made by meiosis", "sporangium", s23(12)),
        ("hair-like threads that anchor and absorb, not true roots", "rhizoids", s23(17)),
        ("groups of cells that break off a liverwort and grow into a new plant", "gemmae", s23(17)),
        ("thread-like first stage of a moss gametophyte", "protonema", s23(30)),
        ("the three parts of a moss sporophyte", "foot, stalk, capsule", s23(22)),
        ("lid of a moss capsule; teeth that close it except in dry weather", "operculum", s23(30)),
        ("strengthens the walls of xylem's conducting cells", "lignin", s23(31)),
        ("carries water and minerals up / sucrose throughout the plant", "xylem / phloem", s23(31)),
        ("small leaf with a single, unbranched vein", "microphyll", s23(34, 37)),
        ("broad leaf with branched veins; collects more solar energy", "megaphyll", s23(36, 37)),
        ("cone-shaped structure that makes spores", "strobilus (plural strobili)", s23(34, 38)),
        ("large fern leaf divided into leaflets", "frond", s23(42)),
        ("clusters of sporangia under a fern leaf; the flap covering them", "sori; indusium", s23(42, 52)),
        ("fern gametophyte with archegonia at the notch, antheridia at the tip", "prothallus", s23(52)),
        ("horizontal stem that gives rise to fronds or aboveground stems", "rhizome", s23(40, 52)),
        ("embryo + stored food in a protective coat", "seed", s23(54)),
        ("male gametophyte of a seed plant", "pollen grain", s23(55)),
        ("holds the female gametophyte; becomes the seed", "ovule", s23(55, 84)),
        ("seed leaves that nourish the embryo", "cotyledons", s23(80)),
        ("all the sepals / all the petals", "calyx / corolla", s23(83)),
        ("slender stalk holding up the anther / sac that makes pollen", "filament / anther", s23(84)),
        ("sticky knob / slender stalk / base enclosing ovules", "stigma / style / ovary", s23(84)),
        ("female gametophyte of a flowering plant (usually 7 cells)", "embryo sac", s23(86, 89)),
        ("two nuclei from opposite ends of the embryo sac", "polar nuclei", s23(86)),
        ("small opening in the ovule where the sperm enter", "micropyle", s23(87)),
        ("pollen cell that grows the tube / that divides into 2 sperm", "tube cell / generative cell", s23(87, 89)),
        ("triploid food tissue in the seed", "endosperm", s23(88)),
    ]),
    ("Processes and terms", [
        ("life switches between a many-celled n plant and a many-celled 2n plant", "alternation of generations", s23(12)),
        ("the generation you notice (bigger, longer-lived)", "dominant generation", s23(14)),
        ("why land plants have a diploid generation", "it hides the effect of a single deleterious allele (UV damage)", s23(11)),
        ("makes one type of spore / two types", "homosporous / heterosporous", s23(34)),
        ("seed plants keep their spores instead of releasing them", "seed plants (they retain the spores)", s23(55)),
        ("wind or an animal carries pollen to the female part", "pollination", s23(55, 87)),
        ("fertilization without outside water", "seed plants (sperm travel in a pollen tube)", s23(55)),
        ("arrested state that lets a seed survive harsh conditions", "dormancy", s23(54)),
        ("one sperm + egg, the other + polar nuclei", "double fertilization", s23(88)),
        ("flower with all four parts / missing one or more", "complete / incomplete", s23(91)),
        ("flower with stamens and carpels / only one of them", "perfect / imperfect", s23(91)),
        ("cluster of flowers / looks like one flower but is many tiny ones", "inflorescence / composite", s23(91)),
        ("one plant makes both pollen and seed cones", "monoecious (conifers)", s23(58)),
        ("separate pollen-making and seed-making plants", "dioecious (ginkgo)", s23(72)),
        ("plain flower, not showy", "wind-pollinated", s23(90)),
        ("colorful flower", "bird- or insect-pollinated", s23(90)),
        ("white or cream, fragrant, opens at night", "pollinated by nocturnal mammals or insects", s23(90)),
        ("moist, fleshy covering (apple) / dry covering (acorn)", "fruits (from the ovary)", s23(88)),
    ]),
]

# extra glossary entries beyond the specs' ANY lists: {chapter: [(term, definition, [slides])]}
GLOSSARY = {}
# spec terms that are the same concept, merged into one glossary entry: {term: merged term} (lowercase)
GLOSSARY_SAME = {
    "vascular": "vascular tissue", "vascular system (vascular tissue)": "vascular tissue",
    "xylem": "xylem and phloem", "pollen sacs": "pollen sacs (microsporangia)",
}

# term index: (term, regex searched in the printed slides, main slides listed first, note)
INDEX = [
    ("Alternation of generations", r"alternation", s23(12), None),
    ("Amborella", r"amborella", s23(78), "(angiosperm): closest living relative of the first flowering plants; New Caledonia"),
    ("Angiosperms", r"angiosperm|flowering plant", s23(77, 56), None),
    ("Anther", r"\banthers?\b", s23(84), None),
    ("Antheridia", r"antherid", s23(12), None),
    ("Archaefructus", r"archaefructus", s23(78), "(fossil): long the earliest known angiosperm; fruit and flowers"),
    ("Archegonia", r"archegoni", s23(12), None),
    ("Bryophytes (nonvascular plants)", r"bryophyte|nonvascular", s23(16), None),
    ("Calyx", r"calyx", s23(83), None),
    ("Capsella", r"capsella", s23(7), "(flowering plant): protected, nourished embryo in a seed"),
    ("Capsule", r"capsule", s23(22, 30), None),
    ("Carpel", r"carpel", s23(84), None),
    ("Chara", r"\bchara\b", s23(5, 8), "(charophyte)"),
    ("Charophytes", r"charophyte", s23(5), None),
    ("Club mosses, ground pines (Lycopodium)", r"club moss|ground pine|lycopodium", s23(34, 35), "(lycophytes)"),
    ("Coleochaete", r"coleochaete", s23(5), "(charophyte)"),
    ("Complete / incomplete flower", r"\bincomplete\b", s23(91), None),
    ("Composite flower", r"composite", s23(91), None),
    ("Conifers", r"conifer", s23(58), None),
    ("Cooksonia", r"cooksonia", s23(32, 33), "(early vascular plant fossil): branched, sporangia at the tips"),
    ("Corolla", r"corolla", s23(83), None),
    ("Cotyledons", r"cotyledon", s23(80), None),
    ("Cuticle", r"cuticle", s23(9), None),
    ("Cycads", r"cycad", s23(70), None),
    ("Dioecious", r"dioecious", s23(72), None),
    ("Dominant generation", r"dominant\b(?! from)|sporophyte dominance", s23(14), None),
    ("Dormancy", r"dorman", s23(54), None),
    ("Double fertilization", r"double fertilization", s23(88), None),
    ("Duckweed, Eucalyptus", r"duckweed|eucalyptus", s23(77), "(angiosperms): the tiniest and the tallest"),
    ("Embryo", r"\bembryos?\b", s23(3, 7, 54), None),
    ("Embryo sac", r"embryo sac", s23(86, 89), None),
    ("Endosperm (3n)", r"endosperm", s23(88), None),
    ("Ephedra", r"ephedr", s23(74, 75), "(gnetophyte): source of ephedrine"),
    ("Equisetum", r"equisetum", s23(38), "(horsetail): silica in stems; spring-loaded spores"),
    ("Eudicots", r"eudicot", s23(80, 81), None),
    ("Ferns", r"(?<!whisk )\bferns?\b", s23(42), None),
    ("Filament", r"\bfilament\b", s23(84), None),
    ("Flagellated sperm", r"(?<!non)flagell", s23(16, 70), None),
    ("Fronds", r"frond", s23(42), None),
    ("Fruit", r"\bfruits?\b", s23(84, 88), None),
    ("Gametangia", r"gametang", s23(12), None),
    ("Gametophyte", r"gametophyte", s23(12, 14), None),
    ("Gemmae", r"gemma", s23(17), None),
    ("Generative cell", r"generative cell", s23(89), None),
    ("Ginkgo biloba", r"ginkgo|gingko", s23(72), "(the only ginkgo): dioecious; pollution-resistant"),
    ("Gnetophytes", r"gnetophyte", s23(74), None),
    ("Gnetum", r"gnetum", s23(74), "(gnetophyte): trees or vines, leathery paired leaves"),
    ("Granite mosses, true mosses", r"granite moss|true moss", s23(21), None),
    ("Green algae", r"green alga", s23(3, 5), None),
    ("Gymnosperms", r"gymnosperm", s23(56, 57), None),
    ("Homosporous / heterosporous", r"heterospor|homospor", s23(34), None),
    ("Hornworts (Anthoceros)", r"hornwort|anthoceros", s23(19), None),
    ("Horsetails", r"horsetail", s23(38), None),
    ("Indusium", r"indusium", s23(52), None),
    ("Inflorescence", r"inflorescence", s23(91), None),
    ("Lignin", r"lignin|lignified", s23(31), None),
    ("Liverworts", r"liverwort", s23(17), None),
    ("Lycophytes", r"lycophyte", s23(34), None),
    ("Maidenhair fern", r"maidenhair", s23(53), "(fern): cold medicine"),
    ("Marchantia", r"marchantia", s23(17, 18), "(liverwort): rhizoids, gemmae"),
    ("Megaphylls", r"megaphyll", s23(36, 37), None),
    ("Megaspores", r"megaspore", s23(34, 55), None),
    ("Microphylls", r"microphyll", s23(34, 37), None),
    ("Micropyle", r"micropyle", s23(87), None),
    ("Microspores", r"microspore", s23(34, 55), None),
    ("Monocots", r"monocot", s23(80, 81), None),
    ("Monoecious", r"monoecious", s23(58), None),
    ("Mosses", r"\bmoss(es)?\b", s23(21), None),
    ("Oedogonium", r"oedogonium", s23(7), "(green alga): unprotected embryo"),
    ("Operculum", r"operculum", s23(30), None),
    ("Ovary", r"\bovar(y|ies)\b", s23(84), None),
    ("Ovule", r"ovule", s23(55, 84), None),
    ("Peat moss", r"\bpeat\b", s23(21), None),
    ("Perfect / imperfect flower", r"perfect", s23(91), None),
    ("Petals", r"petal", s23(83), None),
    ("Phloem", r"phloem", s23(31), None),
    ("Pines", r"(?<!ground )\bpines?\b", s23(58, 68, 69), "(conifers; ground pines are lycophytes)"),
    ("Polar nuclei", r"polar nucle", s23(86, 88), None),
    ("Pollen cones, seed cones", r"pollen cone|seed cone", s23(68), None),
    ("Pollen grain", r"pollen grain", s23(55, 87), None),
    ("Pollen tube", r"pollen tube", s23(55, 87), None),
    ("Pollination", r"pollinat", s23(55, 87, 90), None),
    ("Prothallus", r"prothall", s23(52), None),
    ("Protonema", r"protonema", s23(22, 30), None),
    ("Psilotum", r"psilotum", s23(40, 41), "(whisk fern): no leaves"),
    ("Pteridophytes", r"pteridophyte", s23(36), None),
    ("Quillworts (Isoetes)", r"quillwort|isoetes", s23(34), "(lycophytes)"),
    ("Rhizoids", r"rhizoid", s23(17), None),
    ("Rhizome", r"rhizome", s23(40), None),
    ("Seed", r"\bseeds?\b", s23(54), None),
    ("Seed plants", r"seed plant", s23(54, 55), None),
    ("Seedless vascular plants", r"seedless", s23(32), None),
    ("Sepals", r"sepal", s23(83), None),
    ("Sori", r"\bsori\b|\bsorus\b", s23(42), None),
    ("Spike mosses (Selaginella)", r"spike moss|selaginella", s23(34, 35), "(lycophytes)"),
    ("Sporangium", r"sporangi", s23(12), None),
    ("Spores", r"\bspores?\b", s23(12), None),
    ("Sporophyte", r"sporophyte", s23(12, 14), None),
    ("Spruce, juniper", r"spruce|juniper", s23(59), "(conifers)"),
    ("Stamen", r"stamen", s23(84), None),
    ("Stigma", r"stigma", s23(84), None),
    ("Stomata", r"stomat", s23(9), None),
    ("Strobili", r"strobil", s23(34), None),
    ("Style", r"\bstyle\b", s23(84), None),
    ("Thallus, thallose liverworts", r"\bthall(us|ose)", s23(17), None),
    ("Tmesipteris", r"tmesipteris", s23(40), "(whisk fern): appendages like reduced megaphylls"),
    ("Tracheids", r"tracheid", s23(9), None),
    ("Tracheophytes (vascular plants)", r"tracheophyte|(?<!non)vascular plant", s23(31), None),
    ("Tree ferns", r"tree fern", s23(53), "(ferns): termite-resistant wood"),
    ("Tube cell", r"tube cell", s23(87, 89), None),
    ("UV radiation", r"\buv\b", s23(11), None),
    ("Vascular tissue", r"vascular tissue", s23(31), None),
    ("Welwitschia", r"welwitschia", s23(74, 76), "(gnetophyte): two straplike leaves; SW Africa"),
    ("Whisk ferns", r"whisk fern", s23(40), None),
    ("Xylem", r"xylem", s23(31), None),
    ("Zygote", r"zygote", s23(13, 88), None),
]


# ======================================================================== Ch 24
def s24(*ns):
    return [(24, n) for n in ns]


CHAPTERS.append(24)
TA_SKIP[24] = {57}   # 57: "Accessibility Content" cover slide
SLIDE_TEXT[(24, 15)] = [   # the slide's "Tracheids" heading is only in its title
    "Tracheids", (1, "They are long with tapered ends."), (1, "Water moves across pits in end walls and side walls."),
    (1, "Vascular rays between rows of tracheids conduct water across the width of the plant."), "Vessel Elements",
    (1, "They are larger, with perforation plates in their end walls."),
    (1, "They form a continuous vessel for water and mineral transport."),
]
FIG_FIX[(24, 49)] = [("rhizone", "rhizome")]
CAPTIONS.update({
    (24, 21): "A terminal bud contains an apical meristem and produces new leaves and other tissues during primary "
              "growth. Lateral branches grow from the lateral bud.",
    (24, 29): "This cross section of a willow, Salix, shows the origination and growth of a branch root from the "
              "pericycle.",
    (24, 31): "In this overall cross section, it is possible to observe that a vascular ring surrounds a central pith.",
})
PROCESS.update({
    (24, 33): "a. Sweet potato plants have food storage roots. b. Prop roots (corn) are specialized for support in high "
              "winds. c. Pneumatophores (mangrove, bald cypress) extend above the water's surface, so a tree living in "
              "water can acquire oxygen. d. The aerial roots of orchids offer physical support, water and nutrient "
              "uptake, and in some cases even photosynthesis; English ivy uses aerial roots to climb.",
    (24, 55): "a. The spines of a cactus are modified leaves that protect the fleshy stem from animal predation. b. The "
              "tendrils of a cucumber are modified leaves that attach the plant to a physical support. c. The modified "
              "leaves of the Venus flytrap trap insect prey: when an insect triggers it, the leaf snaps shut and "
              "secretes digestive juices that break down the insect's soft parts.",
})
CORRECTIONS.update({
    (24, 27): "Lignin isn't a protein (the textbook uses the same wording): it's a chemical that hardens cell walls, "
              "and suberin is a waxy, waterproof lipid. Together they make the Casparian strip waterproof, so water "
              "and minerals must pass through the endodermal cells.",
    (24, 42): "Woody stems are mostly vascular tissue: wood is secondary xylem, and bark contains secondary phloem "
              "(24.4.43–45). The three regions are bark, wood and pith (the slide leaves out wood). The professor "
              "confirmed this slide is wrong (Oct 22).",
    (24, 52): "Carbon dioxide enters the leaf through the stoma; oxygen and water vapor leave through it (textbook "
              "Fig. 24.22). The description's “carbon dioxide leaving” is a slip.",
})

TABLES += [
    {"ch": 24, "title": "Meristems", "head": ["Meristem", "Where / what it makes"],
     "rows": [
         (["Apical meristem", "tips of stems and roots; primary growth (length); makes the three primary meristems"],
          s24(3, 6, 42)),
         (["Protoderm", "epidermis (epidermal tissue), the outer protective covering"], s24(3, 35)),
         (["Ground meristem", "ground tissue, which fills the interior; in stems, the pith and cortex"], s24(3, 35)),
         (["Procambium", "vascular tissue: primary xylem and phloem (and vascular cambium)"], s24(3, 35, 37)),
         (["Vascular cambium", "lateral meristem; secondary xylem and secondary phloem each year; secondary growth "
                               "(girth)"], s24(43, 45)),
         (["Cork cambium", "cork (periderm), which replaces the epidermis of woody stems"], s24(8, 44)),
     ]},
    {"ch": 24, "title": "Cell and tissue types", "head": ["Tissue / cell", "Features and job"],
     "rows": [
         (["Epidermis", "closely packed cells; waxy cuticle where exposed to air; root hairs (absorb water); "
                        "trichomes (protect from sun and moisture loss; discourage herbivory); stomata on the lower "
                        "leaf surface"], s24(7, 8)),
         (["Periderm (cork)", "replaces the epidermis in older woody stems; cork made by cork cambium; suberin; gas "
                              "exchange only at lenticels"], s24(8, 44)),
         (["Parenchyma", "least specialized, most abundant, in all organs; can divide; with chloroplasts, "
                         "photosynthesize"], s24(10)),
         (["Collenchyma", "living; thicker primary walls; bundles under the epidermis; flexible support of young "
                          "regions (celery strings)"], s24(10, 12)),
         (["Sclerenchyma", "thick secondary walls with lignin; mostly dead at maturity; support of mature regions; "
                           "fibers (long: hemp, rope) and sclereids (short: seed coats, nutshells)"], s24(11, 12)),
         (["Tracheids (xylem)", "long, tapered ends; water crosses pits in end and side walls"], s24(15)),
         (["Vessel elements (xylem)", "larger; perforation plates in end walls; form a continuous vessel"], s24(15)),
         (["Sieve-tube members (phloem)", "conducting cells; cytoplasm but no nucleus; sieve plate (cluster of "
                                          "pores)"], s24(16)),
         (["Companion cells (phloem)", "have a nucleus; joined to a sieve-tube member by plasmodesmata; help "
                                       "transport"], s24(16)),
     ]},
    {"ch": 24, "title": "Xylem vs phloem", "slides": s24(13, 15, 16, 44, 45), "head": ["", "Xylem", "Phloem"],
     "rows": [
         ["Carries", "water and minerals, roots to leaves", "sucrose and other organic compounds"],
         ["Conducting cells", "tracheids, vessel elements", "sieve-tube members (with companion cells)"],
         ["Location", "vascular cylinder (root), vascular bundles (stem), leaf veins (both)", "same, beside the xylem"],
         ["In a woody stem", "wood (secondary xylem); heartwood no longer carries water",
          "in the bark; girdling removes it and kills the tree"],
     ]},
    {"ch": 24, "title": "Monocots vs eudicots", "slides": s24(22, 23, 24, 32, 38), "head": ["", "Monocots", "Eudicots"],
     "rows": [
         ["Cotyledons", "one; transfer tissue (nutrients come from the endosperm)", "two; supply nutrients to the seedling"],
         ["Root vascular tissue", "in a ring (around a pith)", "phloem between the arms of the xylem"],
         ["Stem vascular bundles", "scattered", "in a distinct ring"],
         ["Leaf veins", "parallel", "netted"],
         ["Flower parts", "threes", "fours or fives"],
         ["Pollen", "one pore or slit", "three pores or slits"],
         ["Root system", "fibrous", "taproot (textbook)"],
     ]},
    {"ch": 24, "title": "Roots", "head": ["Type", "What it does (example)"],
     "rows": [
         (["Taproot", "one long, fleshy root growing straight down; stores food (eudicots; carrot)"], s24(32)),
         (["Fibrous root system", "slender roots and lateral branches; anchors the plant (monocots; grasses)"],
          s24(32)),
         (["Storage roots", "store large amounts of carbohydrate (sweet potato)"], s24(32, 33)),
         (["Prop roots", "support in high wind (corn)"], s24(33)),
         (["Pneumatophores", "get oxygen for trees growing in water (mangrove, bald cypress)"], s24(33)),
         (["Aerial roots", "support, climbing, water and nutrient uptake, some photosynthesis (orchids, English ivy)"],
          s24(32, 33)),
         (["Mycorrhizae", "fungus partners that help extract water and minerals"], s24(34)),
         (["Root nodules", "nitrogen-fixing bacteria; plant gets nitrogen, bacteria get carbohydrates"], s24(34)),
     ]},
    {"ch": 24, "title": "Woody stem, outside in", "head": ["Region", "Contains / does"],
     "rows": [
         (["Bark", "everything outside the vascular cambium: cork, cork cambium, cortex, phloem; girdling it kills the "
                   "tree"], s24(44, 46)),
         (["Vascular cambium", "lateral meristem; makes secondary xylem and secondary phloem each year; dormant in "
                               "winter"], s24(43, 45)),
         (["Wood", "secondary xylem in annual rings; sapwood (outer rings) still carries water"], s24(45, 47)),
         (["Annual ring", "spring wood + summer wood (summer wood has fewer vessels) = one year"], s24(45, 46)),
         (["Heartwood", "inner rings of older trees; no longer carry water"], s24(45, 47)),
         (["Pith", "the center"], s24(42, 46)),
     ]},
    {"ch": 24, "title": "Stems", "head": ["Type", "What it is (example)"],
     "rows": [
         (["Herbaceous stem", "nonwoody; primary growth only; waxy cuticle; bundles in a ring (eudicot) or scattered "
                              "(monocot)"], s24(38)),
         (["Woody stem", "primary + secondary growth; bark, wood, pith"], s24(41, 42)),
         (["Stolon", "above-ground horizontal stem; new plants where nodes touch the ground (strawberry)"], s24(48, 49)),
         (["Rhizome", "underground horizontal stem; asexual reproduction (iris)"], s24(48, 49)),
         (["Tuber", "enlarged storage part of a rhizome (potato)"], s24(48, 49)),
         (["Corm", "underground stem that makes new plants the next season (gladiolus)"], s24(48, 49)),
     ]},
    {"ch": 24, "title": "Leaves", "head": ["Term", "Meaning (example)"],
     "rows": [
         (["Blade / petiole", "the wide part / the stalk attaching it to the stem"], s24(50)),
         (["Leaf axil", "upper angle between petiole and stem; holds the axillary bud"], s24(50)),
         (["Evergreen / deciduous", "keeps leaves all year / loses all its leaves"], s24(50)),
         (["Palisade mesophyll", "elongated cells under the upper epidermis; most of the photosynthesis"], s24(51)),
         (["Spongy mesophyll", "irregular cells bounded by air spaces"], s24(51)),
         (["Stomata", "in the lower epidermis; CO2 in, O2 and water vapor out"], s24(51, 52)),
         (["Simple / compound", "one blade (magnolia) / leaflets: pinnately in pairs (black walnut) or palmately from "
                                "one point (buckeye)"], s24(53, 54)),
         (["Alternate / opposite / whorled", "beech / two leaves per node (maple) / several per node (bedstraw)"],
          s24(53, 54)),
         (["Adapted leaves", "shade leaves; spines (cactus, protect the stem); tendrils (cucumber, climbing); reduced "
                          "leaves; insect-catching leaves (sundew, Venus flytrap)"], s24(53, 55)),
     ]},
    {"ch": 24, "title": "Look-alikes", "head": ["These", "The difference"],
     "rows": [
         (["apical vs lateral meristem", "tips, length (primary growth) vs vascular and cork cambium, girth "
                                         "(secondary growth)"], s24(6, 41, 43)),
         (["tracheids vs vessel elements", "tapered, water through pits vs larger, perforation plates, continuous "
                                           "vessel"], s24(15)),
         (["sieve-tube member vs companion cell", "conducts, no nucleus vs has a nucleus, helps it"], s24(16)),
         (["collenchyma vs sclerenchyma", "living, flexible support of young parts vs mostly dead, lignin, support of "
                                          "mature parts"], s24(10, 11)),
         (["fibers vs sclereids", "long and slender (hemp, rope) vs short (seed coats, nutshells)"], s24(11)),
         (["root cap vs root hairs", "protects the root apical meristem vs absorb water (zone of maturation)"],
          s24(7, 26)),
         (["endodermis vs pericycle", "boundary with the Casparian strip vs dividing cells that start branch roots"],
          s24(27)),
         (["taproot vs fibrous roots", "one main root, stores food vs many slender roots, anchor"], s24(32)),
         (["mycorrhizae vs root nodules", "fungi (water, minerals) vs nitrogen-fixing bacteria"], s24(34)),
         (["herbaceous vs woody stem", "primary growth only vs primary + secondary growth"], s24(38, 41)),
         (["bark vs wood", "outside the vascular cambium, contains phloem vs secondary xylem"], s24(44, 45)),
         (["spring wood vs summer wood", "more vessels vs fewer vessels"], s24(45)),
         (["sapwood vs heartwood", "outer rings, still carry water vs inner rings, no longer do"], s24(45, 47)),
         (["stolon vs rhizome", "above-ground vs underground horizontal stem"], s24(48)),
         (["tuber vs corm", "enlarged storage part of a rhizome vs underground stem making new plants next season"],
          s24(48)),
         (["palisade vs spongy mesophyll", "elongated, packed cells vs irregular cells with air spaces"], s24(51)),
         (["simple vs compound leaf", "one blade vs divided into leaflets"], s24(53)),
         (["annual vs perennial", "one growing season vs three or more"], s24(25)),
     ]},
]

SEQUENCES += [
    {"ch": 24, "title": "Root zones, from the tip up", "slides": s24(26, 28),
     "note": "root cap (protects the root apical meristem) → zone of cell division (primary meristems) → zone of "
             "elongation (cells lengthen and start to specialize) → zone of maturation (fully differentiated cells; "
             "root hairs)"},
    {"ch": 24, "title": "Eudicot root tissues, outside in", "slides": s24(27, 28),
     "note": "epidermis (root hairs) → cortex (parenchyma; water and minerals move through) → endodermis with the "
             "Casparian strip (forces water and minerals through its cells) → pericycle (starts branch roots) → "
             "vascular cylinder: star-shaped xylem, phloem between its arms"},
    {"ch": 24, "title": "Secondary growth of a woody stem", "slides": s24(41, 43, 44, 45),
     "note": "vascular cambium (lateral meristem) makes secondary xylem and secondary phloem each year → the xylem "
             "builds up as wood in annual rings (spring wood, then summer wood); inner rings become heartwood → cork "
             "cambium makes cork, which replaces the epidermis (periderm) → bark = everything outside the vascular "
             "cambium"},
]

USES += [
    {"ch": 24, "title": "", "slides": s24(11, 48), "head": ["Source", "Use (and why)"],
     "rows": [
         (["Sugar cane", "table sugar (its stem stores sugar)"], s24(48)),
         (["Bark", "cinnamon and quinine"], s24(48)),
         (["Wood", "paper and building materials (wood is secondary xylem)"], s24(48)),
         (["Hemp fibers", "rope (fibers are long sclerenchyma cells)"], s24(11)),
     ]},
]

CLUES += [
    ("Tissues and cells", [
        ("undifferentiated cells that keep dividing all the plant's life", "meristem", s24(6)),
        ("outer layer that becomes the epidermis / ground tissue / vascular tissue", "protoderm / ground meristem / procambium", s24(3)),
        ("hairs on stems and leaves; protect from sun and moisture loss; discourage plant-eaters", "trichomes", s24(8)),
        ("extensions of root epidermal cells that add surface for absorbing water", "root hairs", s24(7)),
        ("replaces the epidermis of an older woody stem", "periderm (cork)", s24(8)),
        ("least specialized, most abundant cells; can divide; may photosynthesize", "parenchyma", s24(10)),
        ("the strings in celery; flexible support for young parts", "collenchyma", s24(10)),
        ("dead cells with lignin walls that support mature parts", "sclerenchyma", s24(11)),
        ("long, slender sclerenchyma cells used for rope", "fibers (hemp)", s24(11)),
        ("short sclerenchyma cells in nutshells and seed coats", "sclereids", s24(11)),
        ("water-conducting cells with tapered ends and pits", "tracheids", s24(15)),
        ("wider water-conducting cells with perforation plates, joined into a pipe", "vessel elements", s24(15)),
        ("carry water sideways across the plant", "vascular rays", s24(15)),
        ("sugar-conducting cell with cytoplasm but no nucleus", "sieve-tube member", s24(16)),
        ("cell with a nucleus that serves a sieve-tube member", "companion cell", s24(16)),
        ("cluster of pores in the wall of a sieve-tube member", "sieve plate", s24(16)),
    ]),
    ("Roots", [
        ("cap that protects the root apical meristem", "root cap", s24(26)),
        ("region where cells lengthen and begin to specialize", "zone of elongation", s24(26)),
        ("region with fully differentiated cells and root hairs", "zone of maturation", s24(26)),
        ("waterproof band (lignin and suberin) that forces water through cells", "Casparian strip (endodermis)", s24(27)),
        ("dividing layer where branch roots start", "pericycle", s24(27, 29)),
        ("ground tissue in the center of a monocot root", "pith", s24(30)),
        ("one thick root that stores food (carrot)", "taproot", s24(32)),
        ("many slender roots that anchor the plant (grasses)", "fibrous root system", s24(32)),
        ("roots growing from the base of a corn stem for support", "prop roots", s24(33)),
        ("roots that stick up out of swamp water to get oxygen", "pneumatophores", s24(33)),
        ("orchid roots hanging in the air", "aerial roots", s24(33)),
        ("fungi that help roots take up water and minerals", "mycorrhizae", s24(34)),
        ("swellings on roots holding nitrogen-fixing bacteria", "root nodules", s24(34)),
    ]),
    ("Stems", [
        ("where a leaf attaches / the stem between two of them", "node / internode", s24(20)),
        ("bud at the stem tip with the shoot apical meristem", "terminal bud", s24(20, 21)),
        ("each ring of bud-scale scars on a twig", "one year of growth", s24(35)),
        ("vascular bundles scattered through the stem", "monocot stem", s24(38, 40)),
        ("vascular bundles in a ring", "herbaceous eudicot stem", s24(38, 39)),
        ("increases a stem's girth", "secondary growth (vascular and cork cambium)", s24(42, 43)),
        ("makes secondary xylem and secondary phloem", "vascular cambium", s24(43)),
        ("removing a ring of bark kills the tree", "girdling (the phloem is in the bark)", s24(44)),
        ("waterproof substance in cork cells", "suberin", s24(44)),
        ("the only spots where a woody stem exchanges gases", "lenticels", s24(44)),
        ("secondary xylem built up year after year", "wood", s24(45)),
        ("wood with fewer vessels, made late in the season", "summer wood", s24(45)),
        ("inner rings that no longer carry water", "heartwood", s24(45, 47)),
        ("strawberry runners: new plants where nodes touch the ground", "stolons", s24(48)),
        ("underground horizontal stem (iris)", "rhizome", s24(48, 49)),
        ("potato", "tuber (a stem, not a root)", s24(48, 49)),
        ("gladiolus: underground stem that makes new plants next season", "corm", s24(48, 49)),
    ]),
    ("Leaves", [
        ("the wide part of a leaf / its stalk", "blade / petiole", s24(50)),
        ("upper angle between petiole and stem, where the axillary bud is", "leaf axil", s24(50)),
        ("loses all its leaves", "deciduous", s24(50)),
        ("elongated cells under the upper epidermis", "palisade mesophyll", s24(51)),
        ("irregular cells with air spaces", "spongy mesophyll", s24(51)),
        ("one blade / blade divided into leaflets", "simple / compound leaf", s24(53, 54)),
        ("two leaves at each node / several at each node", "opposite / whorled", s24(53, 54)),
        ("cactus spines", "modified leaves", s24(53, 55)),
        ("cucumber's coiling climbers", "tendrils (modified leaves)", s24(53, 55)),
    ]),
    ("Processes and terms", [
        ("lives one growing season, then dies after making seeds", "annual", s24(25)),
        ("lives three or more seasons", "perennial", s24(25)),
        ("genes that switch a plant between annual and perennial", "LEAFY and Apetala 1", s24(25)),
        ("one cotyledon, parallel veins, parts in threes", "monocot", s24(22, 24)),
        ("two cotyledons, netted veins, parts in fours or fives", "eudicot", s24(23, 24)),
        ("all plant parts except flowers, seeds and fruits", "vegetative organs", s24(18)),
    ]),
]

GLOSSARY[24] = [
    ("Adventitious roots", "roots that grow from a stem, e.g. at the nodes of stolons and rhizomes (textbook)", [49]),
    ("Cotyledon", "a seed leaf of the embryo; provides nutrients before photosynthesis begins (textbook)", [22, 23]),
    ("Differentiated cell", "a cell that has specialized in structure and job (textbook)", [5, 6, 26]),
    ("Endosperm", "the seed's food-storage tissue, made when a sperm joins the polar nuclei (textbook)", [22]),
    ("Guard cells", "the two cells around each stoma; changes in their turgor open and close it (textbook)", [9, 52]),
    ("Herbivory", "animals eating plants (textbook)", [8]),
    ("Leaf primordia", "immature leaves wrapped around the shoot apical meristem in the terminal bud (textbook)",
     [35, 37]),
    ("Leaf scar, bundle scars", "marks on a twig where a leaf dropped and where its vascular bundles were "
                               "(textbook)", [36]),
    ("Lenticels", "loose patches of cork cells without suberin, where gases pass in and out of a woody stem "
                  "(textbook)", [9, 36, 44]),
    ("Lignin", "a chemical that hardens the cell walls of land plants (textbook); not a protein", [11, 27]),
    ("Mutualism", "a relationship in which both species benefit (textbook)", [34]),
    ("Nitrogen fixation", "bacteria converting nitrogen gas from the air into compounds plants can use, such as "
                          "ammonium (textbook)", [34]),
    ("Perforation plate", "the end wall of a vessel element, with openings that water flows through (textbook)",
     [14, 15]),
    ("Pith", "parenchyma tissue in the center of some stems and roots (textbook)", [30, 42]),
    ("Pits", "thin spots in a tracheid's wall, where no secondary wall forms, that let water pass (textbook)", [15]),
    ("Plasmodesmata", "narrow channels through cell walls that connect the cytoplasm of neighboring plant cells "
                      "(textbook)", [16]),
    ("Primary / secondary cell wall", "every plant cell has a primary wall; some build a thicker secondary wall "
                                      "inside it, often with lignin (textbook)", [10, 11]),
    ("Suberin", "a waxy, waterproof lipid in cork cells and the Casparian strip (textbook)", [27, 44]),
    ("Tendril", "a slender structure (often a modified leaf) that attaches a climbing plant to a support (textbook)",
     [53, 55]),
]

INDEX += [
    ("Annual / perennial", r"\bannual\b(?! ring)|perennial", s24(25), None),
    ("Annual ring", r"annual\s+ring", s24(45, 46), None),
    ("Apical meristem", r"apical meristem", s24(6, 3), None),
    ("Axillary (lateral) bud", r"axillary bud|lateral bud", s24(50, 21), None),
    ("Bark", r"\bbark\b", s24(44), None),
    ("Blade, petiole", r"\bblade\b|petiole", s24(50), None),
    ("Branch (lateral) roots", r"branch root|lateral roots", s24(27, 29), None),
    ("Bud scales", r"bud ?scale", s24(35, 36), None),
    ("Casparian strip", r"casparian", s24(27), None),
    ("Collenchyma", r"collenchyma", s24(10), None),
    ("Companion cell", r"companion cell", s24(16), None),
    ("Cork, cork cambium", r"\bcork\b", s24(8, 44), None),
    ("Corm", r"\bcorms?\b", s24(48), "(gladiolus)"),
    ("Cortex", r"cortex", s24(27), None),
    ("Cuticle", r"cuticle", s24(7), None),
    ("Deciduous, evergreen", r"deciduous|evergreen", s24(50), None),
    ("Endodermis", r"endodermis", s24(27), None),
    ("Epidermis, epidermal tissue", r"epiderm", s24(7), None),
    ("Eudicots", r"eudicot", s24(23, 24), None),
    ("Fibers, sclereids", r"\bfibers?\b|sclereid", s24(11), None),
    ("Fibrous root system", r"fibrous", s24(32), None),
    ("Girdling", r"girdling", s24(44), None),
    ("Ground meristem", r"ground meristem", s24(3, 35), None),
    ("Ground tissue", r"ground tissue", s24(10), None),
    ("Heartwood, sapwood", r"heartwood|sapwood", s24(45, 47), None),
    ("Herbaceous stems", r"herbaceous|nonwoody", s24(38), None),
    ("LEAFY, Apetala 1", r"leafy|apetala", s24(25), "(flower-inducing genes)"),
    ("Leaf axil", r"axil\b", s24(50), None),
    ("Leaf veins", r"\bveins?\b|venation", s24(13, 52), None),
    ("Meristem", r"meristem", s24(6), None),
    ("Mesophyll (palisade, spongy)", r"mesophyll", s24(51), None),
    ("Monocots", r"monocot", s24(22, 24), None),
    ("Mycorrhizae", r"mycorrhiza", s24(34), None),
    ("Node, internode", r"\bnodes?\b|internode", s24(20), None),
    ("Organs (vegetative)", r"\borgans?\b", s24(4, 18), None),
    ("Parenchyma", r"parenchyma", s24(10), None),
    ("Pericycle", r"pericycle", s24(27), None),
    ("Periderm", r"periderm", s24(8), None),
    ("Phloem", r"phloem", s24(13, 16), None),
    ("Pneumatophores, prop roots, aerial roots", r"pneumatophore|prop root|aerial root", s24(33), None),
    ("Primary / secondary growth", r"primary growth|secondary growth", s24(42), None),
    ("Procambium", r"procambium", s24(3, 35), None),
    ("Protoderm", r"protoderm", s24(3, 35), None),
    ("Rhizome", r"rhizome", s24(48), "(iris)"),
    ("Root cap", r"root cap", s24(26), None),
    ("Root hairs", r"root hair", s24(7), None),
    ("Root nodules", r"nodule", s24(34), None),
    ("Root system, shoot system", r"root system|shoot system", s24(18, 19), None),
    ("Root zones (division, elongation, maturation)", r"zone of", s24(26, 28), None),
    ("Sclerenchyma", r"sclerenchyma", s24(11), None),
    ("Sieve plate, sieve-tube members", r"sieve", s24(16), None),
    ("Simple / compound leaves", r"\bcompound\b", s24(53, 54), None),
    ("Spines, tendrils", r"\bspines?\b|tendril", s24(53, 55), "(modified leaves)"),
    ("Spring wood, summer wood", r"spring wood|summer wood", s24(45), None),
    ("Stolon", r"stolon", s24(48), "(strawberry runners)"),
    ("Stomata", r"stomat|\bstoma\b", s24(8, 51), None),
    ("Sundew, Venus flytrap", r"sundew|flytrap", s24(53), "(insect-catching leaves)"),
    ("Taproot", r"taproot", s24(32), None),
    ("Terminal bud", r"terminal bud", s24(20, 35), None),
    ("Tissue", r"\btissues?\b", s24(4), None),
    ("Tracheids", r"tracheid", s24(15), None),
    ("Trichomes", r"trichome", s24(8), None),
    ("Tuber", r"\btubers?\b", s24(48), "(potato)"),
    ("Vascular bundles", r"vascular bundle", s24(13, 38), None),
    ("Vascular cambium", r"vascular cambium", s24(43), None),
    ("Vascular cylinder", r"vascular cylinder", s24(13, 27), None),
    ("Vascular rays", r"vascular rays?", s24(15), None),
    ("Vessel elements", r"vessel element", s24(15), None),
    ("Whorled, alternate, opposite leaves", r"whorled", s24(53, 54), None),
    ("Wood", r"\bwood\b", s24(45), None),
    ("Xylem", r"xylem", s24(13, 14), None),
]


# ======================================================================== Ch 25
def s25(*ns):
    return [(25, n) for n in ns]


CHAPTERS.append(25)
TA_SKIP[25] = {50, 51}   # 50: "Accessibility Content" cover; 51: the title slide's photo
SLIDE_TEXT.update({
    # the ions are MathType pictures on the slide: (H+), (K+), (NO3− and HPO4²−), H+, H+
    (25, 21): [
        "A plasma-membrane proton pump can transport hydrogen ions (H+) out of the cell.",
        "An electrochemical gradient drives positively charged ions (K+) into the cell.",
        "Negatively charged mineral ions (NO3− and HPO4²−) are transported with H+ by carrier proteins.",
        "No energy is required when H+ is moving down its concentration gradient.",
        "This model of mineral ion transport is called chemiosmosis, which occurs when an electrochemical gradient is "
        "used by a cell to do work.",
        "Minerals move into xylem and then are transported into leaves.",
    ],
    # K+, H+, K+ are MathType pictures on the slide
    (25, 41): [
        "Each stoma in a leaf epidermis is bordered by guard cells.",
        (1, "Increased turgor pressure in guard cells opens stoma."),
        (1, "Active transport of K+ into guard cells causes water to enter by osmosis and stomata to open."),
        (1, "H+ ions accumulate outside guard cells as K+ moves in."),
        (1, "Opening and closing of stomata are regulated by light."),
        (1, "ABA (abscisic acid) can also cause stomata to close."),
    ],
    # three one-column tables, each a layer name and its description
    (25, 16): [
        "Soil Profile Layers", (1, "Topsoil (A): Top layer, containing the most humus"),
        (1, "Subsoil (B): Accumulation of leached materials"), (1, "Bedrock (C): Weathered parent material"),
    ],
})
TYPO_FIX.update({
    (25, 4): [("C a, Mg", "Ca, Mg"), ("F e, B, M n, C u, Z n, C l, M o", "Fe, B, Mn, Cu, Zn, Cl, Mo")],
    (25, 41): [("A B A (abscisic", "ABA (abscisic")],
})
CORRECTIONS.update({
    (25, 4): "Nitrogen (N) is missing from the macronutrients: the textbook's Table 25.1 lists C, H, O, N, P, K, S, Ca, "
             "Mg. N is the first number in NPK fertilizer (25.1.6).",
    (25, 19): "Not an error, but confusing: it means that when there is more water outside the root than inside, water "
              "moves in by osmosis, i.e. from higher to lower water potential (25.3.32).",
    (25, 30): "Tracheids have no perforation plates: water passes from one tracheid to the next through pits; vessel "
              "elements have perforation plates at each end (25.3.35).",
    (25, 34): "In the wilted cell, water potential, pressure potential and osmotic potential are all lower inside the "
              "cell than in the fluid outside (textbook Fig. 25B), so water enters; the description's “higher” for the "
              "inside of the cell is a slip.",
})

TABLES += [
    {"ch": 25, "title": "Essential nutrients", "slides": s25(3, 4, 6, 8), "head": ["", "Elements / facts"],
     "rows": [
         ["Essential if", "it has an identifiable role; no other nutrient can substitute; a deficiency causes the plant to "
                          "die"],
         ["Macronutrients", "C, H, O, N, P, K, S, Ca, Mg (large amounts; the slide leaves out N)"],
         ["Micronutrients", "Fe, B, Mn, Cu, Zn, Cl, Mo (small amounts)"],
         ["C, H, O", "about 95% of dry weight; from CO2 (C) and water (H, O)"],
         ["Roles (textbook)", "N: nucleic acids and proteins; Mg: chlorophyll; Fe: cytochromes"],
         ["NPK fertilizer", "% nitrogen, phosphorus, potassium by weight; N: lush green growth, P: root development, K: "
                            "overall vigor"],
     ]},
    {"ch": 25, "title": "Soil", "head": ["Part", "What it is / does"],
     "rows": [
         (["Weathering", "mechanical (wind, rain, ice, rock grinding on rock) or chemical (acid rain, lichens, mosses)"],
          s25(9)),
         (["Sand", "largest particles; water drains readily"], s25(10)),
         (["Silt", "medium particles"], s25(10)),
         (["Clay", "smallest particles; small spaces fill with water; negatively charged, binds Ca2+ and K+"],
          s25(10, 12)),
         (["Loam", "sand's aeration + the mineral retention of silt and clay"], s25(10)),
         (["Humus", "decaying organic material; decreases runoff, prevents leaching, makes soil more acidic, retains "
                    "positive minerals"], s25(9, 11)),
         (["Cation exchange", "H+ and other positive ions swap places with positive minerals so roots can take them up"],
          s25(12, 13)),
         (["Cation exchange capacity", "negative sites that can bind cations; lower in sandy soil"], s25(12)),
         (["Living organisms", "roots open the soil; earthworms and ants aerate it; microorganisms decompose humus; "
                               "bacteria make nitrogen available"], s25(14)),
     ]},
    {"ch": 25, "title": "Soil profile", "slides": s25(15, 16), "head": ["Horizon", "Contains"],
     "rows": [
         ["A (topsoil)", "leaf litter and the most humus (organic matter)"],
         ["B (subsoil)", "inorganic nutrients: minerals leached from above accumulate"],
         ["C (parent material)", "weathered rock (bedrock)"],
     ]},
    {"ch": 25, "title": "Getting nutrients", "head": ["Partner", "Gives / gets"],
     "rows": [
         (["Rhizobium (root nodules)", "fixes atmospheric nitrogen; gets carbohydrates from the plant"], s25(24, 25)),
         (["Mycorrhizal fungi", "more surface area for water and minerals, break down organic matter; get sugars and "
                                "amino acids"], s25(24, 26)),
         (["Parasitic plants", "dodder taps its host's xylem and phloem (haustoria, textbook)"], s25(24, 27)),
         (["Carnivorous plants", "sundew: sticky hairs trap prey and release digestive enzymes"], s25(24, 27)),
     ]},
    {"ch": 25, "title": "Xylem vs phloem", "slides": s25(28, 29, 30, 35, 37, 43, 46),
     "head": ["", "Xylem", "Phloem"],
     "rows": [
         ["Carries", "water and minerals", "sucrose and other organic materials"],
         ["Direction", "bottom to top", "any direction, source to sink"],
         ["Cells", "tracheids (pits), vessel elements (perforation plates)",
          "sieve-tube members (sieve plates, plasmodesmata); companion cells provide proteins"],
         ["Moved by", "cohesion-tension: transpiration pulls; passive", "pressure flow: sucrose loaded actively, water "
                                                                       "follows, pressure pushes"],
         ["Evidence", "root pressure, guttation", "girdling (bark swells above the cut), tracers, aphids"],
     ]},
    {"ch": 25, "title": "Water potential", "slides": s25(31, 32, 33, 34), "head": ["", "Effect"],
     "rows": [
         ["Water moves", "passively, from higher to lower water potential: soil → root → stem → leaf"],
         ["More pressure", "higher water potential (pressure potential)"],
         ["More solutes", "lower water potential (osmotic potential); water moves toward more solute"],
         ["Turgor pressure", "pressure potential from osmosis; keeps cells firm; a wilted plant has lost it"],
     ]},
    {"ch": 25, "title": "Look-alikes", "head": ["These", "The difference"],
     "rows": [
         (["macronutrients vs micronutrients", "needed in larger vs smaller amounts"], s25(4)),
         (["sand vs clay", "largest, drains readily vs smallest, holds water and minerals"], s25(10)),
         (["topsoil (A) vs subsoil (B) vs parent material (C)", "litter and humus vs leached minerals vs weathered "
                                                                "rock"], s25(15)),
         (["pathway A vs pathway B", "between cell walls to the Casparian strip vs root hairs, then cell to cell "
                                     "(plasmodesmata)"], s25(19, 23)),
         (["active vs passive transport", "minerals, uses energy vs water, no energy"], s25(19, 20)),
         (["channel protein vs carrier protein", "lets K+ in vs brings negative ions in with H+"], s25(21, 23)),
         (["root nodules vs mycorrhizae", "nitrogen-fixing bacteria vs fungus adding surface area"], s25(24)),
         (["pressure potential vs osmotic potential", "effect of pressure vs effect of solutes"], s25(33)),
         (["turgid vs wilted", "full of water, firm vs lost turgor, droops"], s25(34)),
         (["root pressure vs tension", "push from water entering roots vs pull from transpiration"], s25(35, 39)),
         (["guttation vs transpiration", "droplets forced out of leaf edges vs evaporation through stomata"],
          s25(35, 37)),
         (["cohesion vs adhesion", "water to water vs water to vessel walls"], s25(37)),
         (["source vs sink", "where sugar comes from vs where it's unloaded"], s25(43)),
     ]},
]

SEQUENCES += [
    {"ch": 25, "title": "Mineral uptake across the membrane", "slides": s25(21, 23),
     "note": "1. an ATP-driven proton pump pushes H+ out of the cell → 2. the electrochemical gradient lets K+ (and other "
             "positive ions) in through a channel protein → 3. negative ions (NO3−, HPO4²−) come in with H+ through a "
             "carrier protein; no energy needed, as H+ moves down its gradient (chemiosmosis) → minerals move into the "
             "xylem"},
    {"ch": 25, "title": "Water's path", "slides": s25(19, 23, 32, 38),
     "note": "soil (higher water potential) → root hair → cortex (between cell walls, pathway A, or cell to cell, pathway "
             "B) → endodermis (the Casparian strip forces it through the cells) → xylem → stem → leaf → out through the "
             "stomata (transpiration)"},
    {"ch": 25, "title": "Cohesion-tension", "slides": s25(37, 38, 39),
     "note": "transpiration at the leaves creates tension → evaporated water is replaced from the leaf veins → cohesion "
             "keeps the column continuous and adhesion keeps it in place → the column is pulled up the stem → water "
             "enters the root xylem by osmosis (passive)"},
    {"ch": 25, "title": "Stomata", "slides": s25(41, 42),
     "note": "open: H+ pumped out → K+ actively enters the guard cells → water follows by osmosis → turgor rises → "
             "stoma opens; close: K+ leaves → water leaves → stoma closes. Light regulates them; ABA closes them."},
    {"ch": 25, "title": "Pressure flow", "slides": s25(45, 46, 47),
     "note": "source (leaf): an ATP-driven pump moves H+ out; sucrose enters the sieve tube with H+ (co-transport) → "
             "water follows by osmosis → high positive pressure → mass flow through the sieve tubes → sink (root): "
             "sugar unloaded and used for cellular respiration or stored; water exits by osmosis and returns to the "
             "xylem"},
]

USES += [
    {"ch": 25, "title": "", "slides": s25(6, 8, 18, 48), "head": ["Source", "Use (and why)"],
     "rows": [
         (["Fertilizer", "NPK ratio: supplies nitrogen, phosphorus and potassium to avoid deficiencies"], s25(6, 8)),
         (["Hydroponics", "growing plants in nutrient solution; testing which nutrients are essential"], s25(6, 7)),
         (["Crop rotation, reduced tillage, companion crops", "reduce farmland erosion"], s25(18)),
         (["Trees", "prevent coastal erosion"], s25(18)),
         (["Aphids", "collect phloem sap for study"], s25(43, 48)),
     ]},
]

CLUES += [
    ("Nutrients and soil", [
        ("about 95% of a plant's dry weight", "carbon, hydrogen and oxygen", s25(3)),
        ("supplies a plant's carbon / its hydrogen and oxygen", "carbon dioxide / water", s25(3)),
        ("inorganic substance, usually with two or more elements", "mineral", s25(3)),
        ("has an identifiable role, can't be replaced, deficiency kills the plant", "essential nutrient", s25(4)),
        ("needed in large amounts: C, H, O, N, P, K, S, Ca, Mg", "macronutrients", s25(4)),
        ("needed in small amounts: Fe, B, Mn, Cu, Zn, Cl, Mo", "micronutrients", s25(4)),
        ("growing plants in nutrient solution to find essential nutrients", "hydroponics", s25(6, 7)),
        ("the three numbers on a fertilizer bag", "NPK ratio (nitrogen, phosphorus, potassium)", s25(6, 8)),
        ("light yellow tomato leaves", "nitrogen deficiency", s25(8)),
        ("rock broken down by wind, rain and ice / by acid rain and lichens", "mechanical / chemical weathering", s25(9)),
        ("largest soil particles; water drains readily", "sand", s25(10)),
        ("smallest soil particles; spaces fill with water", "clay", s25(10)),
        ("ideal soil: aeration plus mineral retention", "loam", s25(10)),
        ("decaying organic matter; decreases runoff, prevents leaching", "humus", s25(9, 11)),
        ("root hair releases H+ to free bound K+ and Ca2+", "cation exchange", s25(12, 13)),
        ("negative sites that hold cations; low in sandy soil", "cation exchange capacity (CEC)", s25(12)),
        ("topsoil with litter and the most humus", "A horizon", s25(15, 16)),
        ("subsoil where leached minerals accumulate", "B horizon", s25(15, 16)),
        ("weathered parent rock", "C horizon", s25(15, 16)),
        ("earthworm casts; ant colonies", "mix and aerate soil", s25(14)),
        ("soil carried away by water or wind", "erosion", s25(17)),
        ("crop rotation, reduced tillage, companion crops", "reduce farmland erosion", s25(18)),
    ]),
    ("Uptake", [
        ("between porous cell walls until the Casparian strip", "pathway A", s25(23)),
        ("into root hairs, then cell to cell", "pathway B", s25(19, 23)),
        ("stops minerals flowing back out of the root", "Casparian strip", s25(20)),
        ("pushes H+ out of the cell using ATP", "proton pump", s25(21, 23)),
        ("lets K+ into the cell", "channel protein", s25(23)),
        ("brings nitrate in together with H+", "carrier protein (co-transport)", s25(21, 23)),
        ("using an H+ gradient to do work", "chemiosmosis", s25(21)),
        ("nitrogen-fixing bacteria in root nodules", "Rhizobium", s25(24)),
        ("fungus that adds surface area; gets sugars and amino acids", "mycorrhizae", s25(24, 26)),
        ("dodder wrapped around a host plant", "parasitic plant", s25(24, 27)),
        ("sundew digesting insects", "carnivorous plant", s25(24, 27)),
    ]),
    ("Transport", [
        ("water moves from higher to lower", "water potential", s25(31)),
        ("the higher it is, the higher the water potential", "pressure (pressure potential)", s25(33)),
        ("the more of them, the lower the water potential", "solutes (osmotic potential)", s25(33)),
        ("pressure from osmosis that keeps cells firm", "turgor pressure", s25(33, 34)),
        ("drooping plant whose cells lost turgor", "wilted", s25(34)),
        ("positive pressure from water entering roots", "root pressure", s25(35)),
        ("droplets forced out along leaf edges", "guttation", s25(35, 36)),
        ("water evaporating through stomata", "transpiration", s25(37, 39)),
        ("water molecules clinging to each other", "cohesion", s25(37)),
        ("water clinging to vessel walls", "adhesion", s25(37)),
        ("transpiration pulls a continuous water column up", "cohesion-tension model", s25(37, 38)),
        ("K+ enters guard cells and water follows", "stoma opens", s25(41, 42)),
        ("hormone that can close stomata", "ABA (abscisic acid)", s25(41)),
        ("where sugar comes from / where it's unloaded", "source / sink", s25(43, 44)),
        ("bark swells just above a girdle", "sugar accumulates (phloem)", s25(43)),
        ("insects used to collect phloem sap", "aphids", s25(43, 48)),
        ("sucrose loaded at the source, water follows, pressure pushes sap", "pressure-flow model", s25(46, 47)),
    ]),
]

GLOSSARY[25] = [
    ("Channel protein", "a membrane protein that forms a channel for a particular ion to cross (textbook)", [21, 23]),
    ("Carrier protein", "a membrane protein that binds a substance and changes shape to move it across (textbook)",
     [21, 23]),
    ("Co-transport", "two substances crossing a membrane together through one carrier, e.g. sucrose with H+ "
                     "(textbook)", [45]),
    ("Companion crops", "crops that hold and nourish the soil (textbook)", [18]),
    ("Electrochemical gradient", "a difference in charge and concentration across a membrane, here of H+, that can "
                                 "drive ions across (textbook)", [21, 23]),
    ("Haustoria", "root-like projections a parasitic plant pushes into its host's xylem and phloem (textbook)", [27]),
    ("Leaching", "minerals being washed out of the soil by water (textbook)", [11, 12, 16]),
    ("Mass (bulk) flow", "a liquid moving as a whole, pushed from high to low pressure (textbook)", [47]),
    ("Mutualism", "a relationship in which both species benefit (textbook)", [24, 26]),
    ("Nitrogen fixation", "bacteria converting nitrogen gas from the air into compounds plants can use, such as "
                          "ammonium (textbook)", [24]),
    ("Parent material", "the original rock a soil forms from (textbook)", [15, 16]),
    ("Plasmodesmata", "narrow channels through cell walls connecting the cytoplasm of neighboring plant cells "
                      "(textbook)", [19, 28]),
    ("Runoff", "rainwater running off the soil surface instead of soaking in (textbook)", [11]),
    ("Stylet", "an aphid's needle-like mouthpart, which taps a sieve tube (textbook)", [48]),
    ("Succession", "larger plants gradually replacing small ones as soil builds up (textbook)", [14]),
]

INDEX += [
    ("ABA (abscisic acid)", r"\bA ?B ?A\b|abscisic", s25(41), "(closes stomata)"),
    ("Adhesion", r"adhesion", s25(37), None),
    ("Aphids", r"aphid", s25(43, 48), "(phloem sap)"),
    ("Carnivorous plants (sundew)", r"carnivorous|sundew", s25(24, 27), None),
    ("Casparian strip", r"casparian", s25(19, 20), None),
    ("Cation exchange, CEC", r"cation exchange", s25(12, 13), None),
    ("Chemiosmosis", r"chemiosmosis", s25(21), None),
    ("Cohesion", r"cohesion", s25(37), None),
    ("Cohesion-tension model", r"cohesion-tension", s25(37, 38), None),
    ("Companion cells", r"companion cell", s25(28), None),
    ("Electrochemical gradient", r"electrochemical", s25(21), None),
    ("Erosion", r"erosion", s25(17, 18), None),
    ("Essential nutrients", r"essential", s25(4), None),
    ("Fertilizer, NPK", r"fertilizer|\bNPK\b", s25(6, 8), None),
    ("Guard cells", r"guard cell", s25(41, 42), None),
    ("Guttation", r"guttation", s25(35, 36), None),
    ("Humus", r"humus", s25(11), None),
    ("Hydroponics", r"hydroponic", s25(6, 7), None),
    ("Leaching", r"leach", s25(11, 12), None),
    ("Loam, sand, silt, clay", r"\bloam\b|\bsand|\bsilt\b|\bclay\b", s25(10), None),
    ("Macronutrients, micronutrients", r"macronutrient|micronutrient", s25(4), None),
    ("Mineral", r"\bminerals?\b", s25(3), None),
    ("Mycorrhizae", r"mycorrhiza", s25(24, 26), None),
    ("Osmotic potential", r"osmotic potential", s25(33), None),
    ("Parasitic plants (dodder)", r"parasitic|dodder", s25(24, 27), None),
    ("Phloem", r"phloem", s25(28, 43), None),
    ("Plasmodesmata", r"plasmodesmata", s25(19, 28), None),
    ("Pressure-flow model", r"pressure-flow", s25(46, 47), None),
    ("Pressure potential", r"pressure potential", s25(33), None),
    ("Proton pump", r"proton pump|ATP-driven pump", s25(21), None),
    ("Rhizobium, root nodules", r"rhizobium|nodule", s25(24, 25), None),
    ("Root pressure", r"root pressure", s25(35), None),
    ("Sieve-tube members, sieve plates", r"sieve", s25(28), None),
    ("Source, sink", r"\bsource\b|\bsinks?\b", s25(43, 44), None),
    ("Soil", r"\bsoil\b", s25(9), None),
    ("Soil profile, horizons", r"soil profile|horizon|topsoil|subsoil", s25(15, 16), None),
    ("Stomata", r"stomat|\bstoma\b", s25(41, 42), None),
    ("Sucrose loading", r"sucrose", s25(45, 46), None),
    ("Tension", r"\btension\b", s25(38, 39), None),
    ("Tracheids, vessel elements", r"tracheid|vessel element", s25(28), None),
    ("Transpiration", r"transpir", s25(37, 39), None),
    ("Turgor pressure, wilting", r"turgor|wilt", s25(33, 34), None),
    ("Water potential", r"water potential", s25(31, 33), None),
    ("Weathering", r"weather", s25(9), None),
    ("Xylem", r"xylem", s25(28, 29), None),
]


# ======================================================================== Ch 26
def s26(*ns):
    return [(26, n) for n in ns]


CHAPTERS.append(26)
TA_SKIP[26] = {48}   # 48: "Accessibility Content" cover slide
# The text alternative linked from 26.3.41 (hidden slide 56) describes Mimosa's leaves, not the short-day plant:
# print it with the Mimosa slide instead, and give 26.3.41 its short alt text (cocklebur).
TEXT_ALT_MATCH[26] = {41: None, 35: 56}
PRINT_BOTH |= {(26, 35)}   # its short alt text says why the leaflets collapse
FIG_FIX[(26, 7)] = [("(2,4-D)Gibberellins", "(2,4-D). Gibberellins")]
CAPTIONS.update({
    (26, 13): "a. The plant on the right was treated with gibberellins; the plant on the left was not. b. The grapes "
              "are larger on the right, because gibberellins increased the space between the grapes, allowing them to "
              "grow larger.",
})
PROCESS.update({
    (26, 15): "Tissue culture experiments show that auxin and cytokinin interact: with the usual amounts of the two "
              "hormones, tobacco cells form a callus of undifferentiated tissue; one ratio of auxin to cytokinin makes "
              "the callus produce roots; another, vegetative shoots and leaves; yet another, floral shoots. It is the "
              "relative concentrations of both hormones that produce the effect.",
    (26, 19): "When ABA (the first messenger) binds to its receptor in the guard cell plasma membrane, the second "
              "messenger, calcium ions (Ca2+), enters. Then K+ channels open and K+ leaves the guard cells; water "
              "follows, and the stoma closes.",
    (26, 43): "If red light is prevalent, as in bright sunlight, growth is normal. If far-red light is prevalent, as in "
              "the shade, or the plant grows in darkness, etiolation occurs: the shoot increases in length and the "
              "leaves stay small and yellow. These effects are due to phytochrome.",
})
CORRECTIONS.update({
    (26, 17): "Abscission isn't ABA's job: applying ABA promotes it, but ABA is no longer believed to cause it "
              "naturally; ethylene brings it about (26.1.20).",
    (26, 29): "Roots, which have root caps, grow downward; stems grow upward.",
    (26, 41): "The deck's text alternative for this slide describes Mimosa's leaves (printed with 26.2.35). The figure "
              "is cocklebur, a short-day plant: it flowers when the night is longer than a critical length, and a "
              "flash of light that interrupts that night stops it flowering (Fig. 26.16a).",
})

TABLES += [
    {"ch": 26, "title": "Plant hormones", "slides": s26(7, 8, 12, 14, 17, 20), "wide": True,
     "head": ["Hormone", "Made in", "Effects", "Commercial use"],
     "rows": [
         (["Auxin (IAA)", "shoot apical meristem; young leaves, flowers, fruits",
           "apical dominance (blocks axillary buds); root and fruit growth; prevents loss of leaves and fruit; "
           "phototropism (shady-side cells elongate); gravitropism",
           "herbicides (2,4-D; Agent Orange); fruit without pollination"], s26(7, 8, 10)),
         (["Gibberellins (GA3)", "young leaves, roots, embryos, seeds, fruits (textbook)",
           "stem elongation; break bud and seed dormancy", "induce growth in crops; larger grapes"], s26(12, 13)),
         (["Cytokinins (zeatin)", "dividing root tissue, seeds, fruits",
           "cell division and organ formation; root nodules, galls; with auxin, prevent senescence; low levels in "
           "autumn let leaves change color and die", "prolong the life of cut flowers and stored vegetables"],
          s26(14, 16)),
         (["Abscisic acid (ABA)", "any green tissue",
           "the stress hormone: starts and maintains seed and bud dormancy; closes stomata; corn that can't respond "
           "shows vivipary", "thinning fruit, so the remaining fruit grows larger"], s26(7, 17, 18)),
         (["Ethylene (gas)", "formed from the amino acid methionine",
           "abscission (stimulates cellulase); ripens fruit (softening, flavor, smell); inhibits axillary buds; "
           "suppresses stem and root elongation", "ripening fruit for market"], s26(20, 21, 22)),
     ]},
    {"ch": 26, "title": "Movements", "head": ["Response", "Stimulus / how"],
     "rows": [
         (["Phototropism", "light: stems grow toward it (shady-side cells elongate, auxin); roots insensitive or "
                           "negative; phototropin absorbs blue light"], s26(25, 26)),
         (["Thigmotropism", "touch (plant, animal, rock, wind): tendrils and stems coil (runner beans, morning "
                            "glories)"], s26(27, 28)),
         (["Thigmomorphogenesis", "whole-plant shape change from touch: barrier, wind, rain"], s26(27)),
         (["Gravitropism", "gravity: stem up, roots down; statoliths (starch in amyloplasts) settle in root-cap "
                           "cells; auxin"], s26(29, 30)),
         (["Turgor (nastic) movement", "no growth, not directional: turgor changes, electrical impulses or "
                                       "hormones (Mimosa pudica, Venus flytrap)"], s26(33, 35)),
         (["Sleep movements", "daily, with light and dark; circadian rhythm"], s26(33, 46)),
     ]},
    {"ch": 26, "title": "Photoperiod", "slides": s26(40, 41, 42), "head": ["Plant", "Flowers when", "Night flash"],
     "rows": [
         ["Short-day (long-night)", "day shorter than the critical length (night longer)", "stops flowering"],
         ["Long-day (short-night)", "day longer than the critical length (night shorter); clover",
          "makes it flower"],
         ["Day-neutral", "regardless of day length", "–"],
     ]},
    {"ch": 26, "title": "Phytochrome", "slides": s26(37, 38, 39, 43, 44), "head": ["", "What it does"],
     "rows": [
         ["Pr", "inactive; absorbs red light (daylight) and becomes Pfr"],
         ["Pfr", "active; absorbs far-red light and becomes Pr in the evening, shade or night"],
         ["Effects", "detects photoperiod changes; promotes germination and flowering; inhibits shoot elongation"],
         ["Spacing", "more far-red light (shade from neighbors) → grows taller to compete"],
         ["Darkness", "etiolation: long shoots, small yellow leaves"],
     ]},
    {"ch": 26, "title": "Look-alikes", "head": ["These", "The difference"],
     "rows": [
         (["auxin vs cytokinins", "apical dominance, elongation, phototropism vs cell division, organ formation"],
          s26(8, 14)),
         (["gibberellins vs abscisic acid", "break dormancy vs start and keep dormancy"], s26(12, 17)),
         (["abscisic acid vs abscission", "the stress hormone vs leaf, fruit or flower drop (caused by ethylene)"],
          s26(17, 20)),
         (["primary vs secondary metabolites", "sugars, amino acids every cell needs vs defense chemicals"], s26(23)),
         (["positive vs negative tropism", "toward vs away from the stimulus"], s26(24)),
         (["tropism vs turgor movement", "growth, directional vs no growth, not directional"], s26(24, 33)),
         (["thigmotropism vs thigmomorphogenesis", "growth toward a touch vs whole-plant shape change"], s26(27)),
         (["phototropin vs phytochrome", "blue light, phototropism vs red and far-red light, photoperiod"],
          s26(25, 36, 37)),
         (["statoliths vs amyloplasts", "starch grains that settle vs the organelles holding them"], s26(29)),
         (["short-day vs long-day plant", "flowers when nights are long vs short"], s26(40)),
         (["photoperiodism vs circadian rhythm", "response to day or night length vs a roughly 24-hour cycle"],
          s26(36, 45)),
     ]},
]

SEQUENCES += [
    {"ch": 26, "title": "Signal transduction", "slides": s26(4, 5),
     "note": "signal (e.g. blue light) → receptor protein (plasma membrane, cytoplasm or nucleus) activated → "
             "transduction pathway: relay proteins amplify and convert the signal → cellular response, most often a "
             "change in gene expression (stem bending, root growth, defense)"},
    {"ch": 26, "title": "Auxin bends a stem toward light", "slides": s26(10, 11),
     "note": "light from one side → auxin moves to the shady side → binds receptors → proton pumps push H+ into the cell "
             "wall → enzymes break cellulose fibers; the wall loosens → water enters, turgor rises → the cell enlarges "
             "and rebuilds a longer wall → shady side elongates; stem bends toward the light"},
    {"ch": 26, "title": "Auxin experiment", "slides": s26(9),
     "note": "coleoptile tip (contains auxin) removed → placed on agar; auxin diffuses into it → agar block placed on one "
             "side of the cut coleoptile → it curves beneath the block"},
    {"ch": 26, "title": "ABA closes stomata", "slides": s26(19),
     "note": "ABA binds a receptor on the guard cell → Ca2+ enters (second messenger) → K+ channels open; K+ leaves → "
             "water leaves → stoma closes (textbook)"},
    {"ch": 26, "title": "Roots sense gravity", "slides": s26(29, 30),
     "note": "statoliths (starch grains in amyloplasts) settle to the bottom of root-cap cells → they press on "
             "organelles, signaling down → auxin redistributes → the root grows down (a clinostat's rotation stops "
             "them settling)"},
    {"ch": 26, "title": "Phytochrome cycle", "slides": s26(37, 38, 39),
     "note": "Pr (inactive) absorbs red light in daylight → Pfr (active) → Pfr reverts (far-red light; evening, shade, "
             "night) → Pr"},
]

USES += [
    {"ch": 26, "title": "", "slides": s26(7, 10, 13, 14, 22, 31), "head": ["Source", "Use (and why)"],
     "rows": [
         (["Synthetic auxins", "herbicides (2,4-D); fruit without pollination"], s26(7, 10)),
         (["Agent Orange", "a synthetic auxin used to defoliate forests in Vietnam"], s26(10)),
         (["Gibberellins", "induce crop growth; larger grapes"], s26(12, 13)),
         (["Cytokinins", "keep cut flowers and stored vegetables fresh"], s26(14)),
         (["ABA", "thinning fruit so the rest grows larger"], s26(7)),
         (["Ethylene", "ripening fruit for market; tomatoes engineered without it ship green"], s26(7, 22)),
         (["Arabidopsis", "model organism for plant molecular genetics"], s26(31)),
     ]},
]

CLUES += [
    ("Hormones", [
        ("chemical signal made in one part, acts elsewhere; travels in phloem", "hormone", s26(6)),
        ("receptor → relay proteins → response", "signal transduction", s26(4, 5)),
        ("the shoot tip keeps side buds from growing", "apical dominance (auxin)", s26(8)),
        ("weed killer 2,4-D; Agent Orange", "synthetic auxins", s26(7, 10)),
        ("coleoptile tip on agar makes a seedling curve", "auxin", s26(9)),
        ("makes stems elongate; breaks seed and bud dormancy", "gibberellins", s26(12)),
        ("bigger grapes, much taller plants", "gibberellins", s26(13)),
        ("cell division and organ formation; root nodules; galls", "cytokinins", s26(14)),
        ("keeps cut flowers and stored vegetables fresh; prevents aging", "cytokinins", s26(14)),
        ("leaves change color in autumn", "low cytokinin levels", s26(14, 16)),
        ("their ratio decides roots or shoots in tissue culture", "auxin and cytokinins", s26(15)),
        ("stress hormone; keeps seeds and buds dormant; closes stomata", "abscisic acid (ABA)", s26(17)),
        ("corn kernels sprouting on the cob", "vivipary (insensitive to ABA)", s26(17, 18)),
        ("gas formed from methionine", "ethylene", s26(20)),
        ("leaves, fruit or flowers dropping off", "abscission (ethylene)", s26(20, 21)),
        ("a ripe apple makes a holly twig drop its leaves", "ethylene", s26(21)),
        ("softens fruit and gives it flavor and smell", "ethylene", s26(20, 22)),
        ("defense chemicals once thought to be waste", "secondary metabolites", s26(23)),
        ("sugars and amino acids every cell needs", "primary metabolites", s26(23)),
    ]),
    ("Movements", [
        ("growth toward or away from a stimulus from one direction", "tropism", s26(24)),
        ("stem bends toward a window", "positive phototropism", s26(25)),
        ("pigment that absorbs blue light for phototropism", "phototropin", s26(25, 26)),
        ("tendrils coiling around a pole", "thigmotropism", s26(27, 28)),
        ("wind-blown plant grows short and sturdy", "thigmomorphogenesis", s26(27)),
        ("plant laid sideways: stem turns up, root turns down", "gravitropism", s26(29, 30)),
        ("starch grains settling in root-cap cells", "statoliths (in amyloplasts)", s26(29)),
        ("rotating chamber that cancels gravity's effect", "clinostat", s26(30)),
        ("weed with a 5–6-week generation time; no commercial value", "Arabidopsis thaliana (model organism)", s26(31)),
        ("movement with no growth that doesn't depend on direction", "turgor (nastic) movement", s26(33)),
        ("leaflets collapse within a second of a touch", "Mimosa pudica (turgor loss)", s26(33, 35)),
        ("trap snaps shut on an insect", "Venus flytrap (turgor movement)", s26(33)),
        ("leaves fold every night", "sleep movements", s26(33)),
    ]),
    ("Light and timing", [
        ("response to day or night length, e.g. when to flower", "photoperiodism", s26(36)),
        ("blue-green leaf pigment with two forms", "phytochrome", s26(37)),
        ("inactive form of phytochrome; absorbs red light", "Pr", s26(37, 38)),
        ("active form of phytochrome", "Pfr", s26(38, 39)),
        ("flowers only when the night is longer than a critical length", "short-day (long-night) plant", s26(41)),
        ("flowers when a flash of light interrupts a long night", "long-day (short-night) plant", s26(42)),
        ("flowers regardless of day length", "day-neutral plant", s26(40)),
        ("seedlings grown in the dark: long, yellow shoots", "etiolation", s26(43)),
        ("more far-red light from neighbors → grows taller", "phytochrome (plant spacing)", s26(44)),
        ("about 24 hours; continues without outside cues", "circadian rhythm", s26(45, 46)),
        ("internal timer that keeps a rhythm going", "biological clock", s26(45)),
        ("rhythm synchronized to light at daybreak", "entrainment", s26(45)),
    ]),
]

GLOSSARY[26] = [
    ("Abiotic / biotic", "nonliving (light, water, temperature) / living (herbivores, parasites, competing plants) "
                         "(textbook)", [23]),
    ("Agar", "a gelatin-like material (textbook)", [9]),
    ("Callus", "a mass of undifferentiated cells grown in tissue culture (textbook)", [15]),
    ("Cellulase", "an enzyme that breaks down cellulose, the main material of plant cell walls (textbook)", [20]),
    ("Clinostat", "a device that slowly rotates a plant so its statoliths can't settle, cancelling the effect of "
                  "gravity (textbook)", [30]),
    ("Coleoptile", "a protective sheath over a grass seedling's young leaves (textbook)", [9]),
    ("Critical length", "the day (or night) length a plant's flowering depends on; for example, 14 hours for spinach "
                        "and ragweed (textbook)", [40, 41, 42]),
    ("Gall", "a tumor-like growth caused by bacteria, fungi, insects or nematodes (textbook)", [14]),
    ("Herbicide", "a weed killer (textbook)", [7, 10]),
    ("Herbivory", "animals eating plants (textbook)", [23]),
    ("Phosphorylated", "with a phosphate group added (from ATP) (textbook)", [26]),
    ("Photoreceptor", "a protein with a pigment that responds to light (textbook)", [25, 36]),
    ("Pulvinus", "a thickening at the base of a leaflet; its cells' loss of turgor folds Mimosa's leaves (textbook)",
     [35]),
    ("Second messenger", "a molecule inside the cell, such as Ca2+, that passes on the signal from a receptor "
                         "(textbook)", [19]),
]

INDEX += [
    ("Abscisic acid (ABA)", r"abscisic|\bABA\b", s26(17), None),
    ("Abscission", r"abscission", s26(20, 21), "(ethylene)"),
    ("Agent Orange, 2,4-D", r"agent orange|2,4-D", s26(10, 7), "(synthetic auxins)"),
    ("Amyloplasts, statoliths", r"amyloplast|statolith", s26(29), None),
    ("Apical dominance", r"apical dominance", s26(8), None),
    ("Arabidopsis thaliana", r"arabidopsis|A\. thaliana", s26(31), "(model organism)"),
    ("Auxin", r"auxin", s26(8), None),
    ("Biological clock", r"biological clock", s26(36, 45), None),
    ("Circadian rhythm", r"circadian", s26(45, 46), None),
    ("Coleoptile", r"coleoptile", s26(9), None),
    ("Cytokinins", r"cytokinin", s26(14), None),
    ("Day-neutral plants", r"day-neutral", s26(40), None),
    ("Dormancy", r"dorman", s26(12, 17), None),
    ("Entrainment", r"entrainment", s26(45), None),
    ("Ethylene", r"ethylene", s26(20), None),
    ("Etiolation", r"etiolat", s26(43), None),
    ("Gibberellins", r"gibberell", s26(12), None),
    ("Gravitropism", r"gravitropism", s26(29), None),
    ("Hormones", r"hormone", s26(6, 7), None),
    ("Long-day (short-night) plants", r"long-day", s26(40, 42), None),
    ("Mimosa pudica", r"mimosa", s26(33, 35), "(turgor movement)"),
    ("Phototropin", r"phototropin", s26(25, 26), None),
    ("Phototropism", r"phototropism", s26(25), None),
    ("Photoperiodism", r"photoperiod", s26(36), None),
    ("Phytochrome (Pr, Pfr)", r"phytochrome|\bPfr\b", s26(37, 38), None),
    ("Primary, secondary metabolites", r"metabolite", s26(23), None),
    ("Senescence", r"senescence", s26(14), None),
    ("Short-day (long-night) plants", r"short-day", s26(40, 41), None),
    ("Signal transduction", r"transduction", s26(4, 5), None),
    ("Sleep movements", r"sleep", s26(33), None),
    ("Stomata closing", r"stomat", s26(17, 19), "(ABA)"),
    ("Thigmomorphogenesis", r"thigmomorphogenesis", s26(27), None),
    ("Thigmotropism", r"thigmotropism", s26(27), None),
    ("Tropism (positive, negative)", r"tropism", s26(24), None),
    ("Turgor (nastic) movements", r"turgor movement|nastic|turgid|limp", s26(33, 34), None),
    ("Venus flytrap", r"flytrap", s26(33), "(turgor movement)"),
    ("Vivipary", r"vivipary", s26(17), None),
]
