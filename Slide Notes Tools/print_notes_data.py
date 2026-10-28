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
