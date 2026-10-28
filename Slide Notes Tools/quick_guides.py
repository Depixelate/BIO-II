"""Quick guides: a plain-language crash course at the front of each chapter's printed notes.

QUICK_GUIDE[chapter] = {
    "intro": [paragraph, ...],                      # the big picture
    "sections": {section_number: [item, ...]},      # one part per section, in order
    "look_up": [item, ...],                         # "look these up, don't memorize"
}
An item is a paragraph string, or (subheading, [bullet, ...]).
Every statement cites slide codes like (23.1.12); build_print_docx.py checks that each cited slide exists and
mentions the statement's key words. Sources: the slides (and text alternatives), Unit 2 Study Guide.md, the textbook.
Written for someone who has never seen the material.
"""

QUICK_GUIDE = {}

QUICK_GUIDE[23] = {
    "intro": [
        "Plants are multicellular, photosynthetic eukaryotes that evolved from freshwater green algae (23.1.3). "
        "This chapter is the story of how plants moved onto land, and how each new group solved another problem of "
        "living there: drying out, moving water up against gravity, and reproducing without water for sperm to "
        "swim in (23.1.9, 23.1.11).",
        "There are four big groups, in the order they evolved (23.1.4, 23.1.6): bryophytes (mosses and their "
        "relatives: no plumbing), seedless vascular plants (lycophytes and ferns: plumbing, but spores instead of "
        "seeds), gymnosperms (seeds, usually on cones) and angiosperms (flowering plants: seeds inside a fruit).",
        "One idea runs through the whole chapter. Every plant has two generations that take turns: a haploid (n) "
        "gametophyte that makes eggs and sperm, and a diploid (2n) sporophyte that makes spores. Over evolution the "
        "sporophyte got bigger and the gametophyte got smaller (23.1.12, 23.1.14, 23.1.15).",
    ],
    "sections": {
        1: [
            "Plants come from green algae: both have chlorophylls, store starch and have cellulose cell walls (23.1.3). "
            "The closest living relatives are the charophytes (Chara and Coleochaete), which, like plants, protect "
            "the zygote (23.1.5). What plants add is protecting and nourishing the embryo (23.1.3, 23.1.7).",
            ("Problems on land and their solutions", [
                "Drying out: a waxy cuticle covers the exposed surfaces (23.1.9).",
                "Gas exchange through that waterproof layer: stomata, small openings mostly on the underside of "
                "leaves (23.1.9).",
                "Moving water up against gravity: tracheids, specialized water-conducting cells (23.1.9).",
                "UV damage: a diploid generation, whose second set of chromosomes hides the effect of a single "
                "deleterious (harmful) allele (23.1.11).",
            ]),
            ("Alternation of generations", [
                "The gametophyte is the haploid (n) plant. It makes eggs and sperm by mitosis in gametangia: "
                "antheridia make sperm, archegonia make eggs (23.1.12).",
                "Egg + sperm make a diploid zygote, which grows into the sporophyte, the diploid (2n) plant "
                "(23.1.12, 23.1.13).",
                "The sporophyte makes spores by meiosis in a sporangium. A spore lands, germinates and grows by "
                "mitosis into a new gametophyte (23.1.12).",
                "Trap: gametes are made by mitosis, spores by meiosis (23.1.12).",
            ]),
            "The dominant generation is the one you notice. In mosses it's the gametophyte; in ferns, pine trees "
            "and flowering plants it's the sporophyte (23.1.14). The shift to a dominant sporophyte is an adaptation "
            "to land: only sporophytes have vascular systems, and the gametophyte shrinks and becomes dependent on "
            "the sporophyte (23.1.14, 23.1.15).",
        ],
        2: [
            "Bryophytes (liverworts, hornworts and mosses) were the first plants to colonize land. With no vascular "
            "tissue they stay low-lying and have no true roots, stems or leaves. The gametophyte is dominant, and its "
            "flagellated sperm swim to the egg in a film of water, so bryophytes need moist places (23.2.16).",
            ("The three groups", [
                "Liverworts: a flat body (thallus) or leafy shoots. Marchantia has rhizoids (hair-like anchors, not "
                "true roots) and reproduces asexually with gemmae, groups of cells that detach and start a new "
                "plant (23.2.17, 23.2.18).",
                "Hornworts: small horn-shaped sporophytes rise out of the gametophyte; one chloroplast per sporophyte "
                "cell; cyanobacteria partners fix nitrogen (23.2.19, 23.2.20).",
                "Mosses: the largest group of nonvascular plants. They can dry out, turn brown and revive when it "
                "rains. Peat moss improves the water capacity of soil (23.2.21).",
            ]),
            "Moss life cycle (23.2.22, 23.2.30): a spore germinates into a thread-like protonema, the first stage of "
            "the gametophyte, which produces leafy shoots bearing antheridia or archegonia. Sperm swim in external "
            "water to the egg. The zygote stays in the archegonium and grows into the sporophyte: a foot, a stalk and "
            "a capsule, always attached to the gametophyte. Meiosis in the capsule makes spores, which are dispersed "
            "by air currents.",
            "Traps: the protonema (first stage of the moss gametophyte) vs the prothallus (the fern gametophyte); "
            "rhizoids vs true roots (23.2.17, 23.2.22, 23.4.52).",
        ],
        3: [
            "Vascular tissue is the plant's plumbing, and it let plants grow tall. Xylem conducts water and minerals "
            "up from the roots, and lignin strengthens its cell walls; phloem conducts sucrose and other organic "
            "compounds throughout the plant (23.3.31).",
            "The first vascular plants, such as Cooksonia, were small and branched; branching meant more sporangia "
            "and more spores (23.3.32, 23.3.33). Lycophytes and all later vascular plants have a dominant "
            "sporophyte (23.3.32).",
            "Lycophytes (ground pines, spike mosses and quillworts) have roots and microphylls: small leaves with a "
            "single strand of vascular tissue. Their spores are made in cone-shaped strobili (23.3.34).",
            "Homosporous plants make one type of spore. Heterosporous plants make two: microspores, which become male "
            "gametophytes, and megaspores, which become female gametophytes (23.3.34). (The slide says homosporous "
            "spores grow into 'one type of gamete'; it should say one type of spore.)",
        ],
        4: [
            "Pteridophytes are ferns and their allies (horsetails and whisk ferns): seedless vascular plants that were "
            "dominant from the late Devonian through the Carboniferous (23.4.36). Their big new feature is the "
            "megaphyll, a broad leaf with branching veins that collects more solar energy (23.4.36, 23.4.37).",
            ("The groups", [
                "Horsetails (Equisetum): reduced leaves in whorls at the nodes, strobili at the stem tips, and silica "
                "that makes the stems tough (23.4.38, 23.4.39).",
                "Whisk ferns (Psilotum): no leaves at all; stems that fork repeatedly grow up from a horizontal "
                "rhizome (23.4.40, 23.4.41).",
                "Ferns: large leaves called fronds, divided into leaflets, with clusters of sporangia called sori on "
                "the undersides (23.4.42).",
            ]),
            "Fern life cycle (23.4.43, 23.4.52): the fern you see is the sporophyte. Meiosis in the sporangia makes "
            "spores. A spore grows into a small, flat gametophyte, the prothallus, with archegonia and antheridia. "
            "Fertilization needs moisture, because the flagellated sperm swim to the egg. The new sporophyte grows out "
            "of the prothallus, which then disappears, so both generations live independently.",
            "Uses: maidenhair fern is the source of a cold medicine, and tropical tree-fern wood resists decay by "
            "termites (23.4.53).",
        ],
        5: [
            "A seed is a sporophyte embryo plus stored food inside a protective seed coat. It can survive harsh "
            "conditions in a dormant state, which largely explains why seed plants dominate today (23.5.54).",
            "Seed plants are heterosporous and keep their spores instead of releasing them. A microspore becomes a "
            "pollen grain (the male gametophyte); a megaspore becomes a female gametophyte inside an ovule, which "
            "becomes the seed. Wind or a pollinator carries pollen to the female gametophyte (pollination), and sperm "
            "reach the egg through a pollen tube, so no external water is needed (23.5.55).",
            "Gymnosperms vs angiosperms: gymnosperm ovules aren't completely enclosed (\"naked\" seeds, mostly on "
            "cones); angiosperm ovules are completely enclosed in an ovary, which becomes a fruit (23.5.56, 23.5.57).",
            ("Gymnosperm groups", [
                "Conifers (pines and relatives, the most plentiful): needle-like leaves with a thick cuticle and "
                "recessed stomata; windblown pollen; monoecious, meaning one plant has both pollen cones and seed "
                "cones (23.5.58).",
                "Pine life cycle: small pollen cones make winged pollen; seed cones hold ovules; in an ovule, meiosis "
                "makes four megaspores and only one survives; a pollen tube grows to the egg; the seed cone releases "
                "winged seeds in the fall of the second season (23.5.68).",
                "Cycads: palm- or fern-like, with cones that can be over 1 m long, pollen and seed cones on separate "
                "plants, insect pollination and sperm with many flagella (23.5.70, 23.5.71).",
                "Ginkgo: one surviving species, Ginkgo biloba; dioecious (separate pollen trees and seed trees); "
                "resistant to pollution (23.5.72).",
                "Gnetophytes: Gnetum, Ephedra (source of ephedrine) and Welwitschia (only two strap-like leaves); none "
                "have archegonia (23.5.74).",
            ]),
            "Angiosperms (flowering plants) are the largest, most successful group; their ovules are always enclosed "
            "(23.5.77). The living plant closest to the first flowering plants is Amborella (23.5.78, 23.5.79). The "
            "two main classes are monocots (one cotyledon, or seed leaf; flower parts in threes; usually parallel "
            "veins) and eudicots (two cotyledons; parts in fours or fives; usually net veins) (23.5.80, 23.5.81).",
            ("The flower", [
                "Sepals (together, the calyx) protect the flower bud; petals (together, the corolla) attract "
                "pollinators (23.5.83).",
                "Stamen (male): the anther makes pollen, on a stalk called the filament (23.5.84).",
                "Carpel (female): the sticky stigma, the stalk-like style, and the ovary, which encloses the ovules "
                "(23.5.84).",
                "After fertilization the ovule becomes the seed and the ovary becomes the fruit (23.5.84).",
            ]),
            "Flowering plant life cycle (23.5.86, 23.5.87, 23.5.88, 23.5.89): in the anther, meiosis makes "
            "microspores, which become pollen grains with a tube cell and a generative cell that divides into two "
            "sperm. In the ovule, meiosis makes four megaspores; three disintegrate and one becomes the embryo sac "
            "(female gametophyte), with an egg and two polar nuclei. After pollination, the pollen tube grows down "
            "the style to the ovule. Double fertilization: one sperm + the egg make the zygote (2n); the other sperm "
            "+ the two polar nuclei make the endosperm (3n), the seed's food.",
            "Flowers match their pollinators: wind-pollinated flowers aren't showy, bird- and insect-pollinated ones "
            "are colorful, and night-blooming ones are white or cream and aromatic (23.5.90). A complete flower has "
            "all four parts; a perfect flower has both stamens and carpels; an inflorescence is a cluster of flowers "
            "(23.5.91).",
            "Traps: monoecious (one plant has both) vs dioecious (separate plants); complete vs perfect; zygote (2n) "
            "vs endosperm (3n); pollination (pollen arrives) vs fertilization (sperm meets egg) (23.5.58, 23.5.72, "
            "23.5.88, 23.5.91).",
        ],
    },
    "look_up": [
        "Features of each plant group: the Plant groups table and 23.1.4.",
        "Which generation dominates and where meiosis happens: the Life cycles table, and the full steps at 23.2.30 "
        "(moss), 23.4.52 (fern), 23.5.68 (pine) and 23.5.89 (flowering plant).",
        "Which organism has which odd feature (Ephedra, Welwitschia, Psilotum, Equisetum, Marchantia...): the Index "
        "file's term index and clue index.",
        "Uses (peat moss, ferns, pines, ginkgo, Ephedra): the Uses table.",
        "Exact numbers and dates (species counts, millions of years ago): don't memorize them.",
    ],
}

QUICK_GUIDE[24] = {
    "intro": [
        "Ch 24 is the anatomy of a flowering plant, built up from cells to tissues to organs. A tissue is a group of "
        "specialized cells doing one job; an organ, such as a root, stem or leaf, is made of several tissues (24.1.4).",
        "Everything grows from meristems, zones of cells that keep dividing for the plant's whole life (24.1.6). The "
        "new cells become three tissue types: epidermal (the outer covering), ground (the filler that photosynthesizes, "
        "stores and supports) and vascular (the plumbing: xylem and phloem) (24.1.3, 24.1.7, 24.1.10, 24.1.13). Those "
        "tissues build the vegetative organs: roots, stems and leaves (24.2.18).",
        "This chapter is very term-heavy. Understand the ideas here, and look up the names in the tables.",
    ],
    "sections": {
        1: [
            "Apical meristems at the tips of roots and shoots make the plant longer. Their cells form three primary "
            "meristems: protoderm (becomes the epidermis), ground meristem (ground tissue) and procambium (vascular "
            "tissue) (24.1.3, 24.1.6).",
            ("Epidermal tissue", [
                "The outer protective covering: closely packed cells, covered by a waxy cuticle where they face the "
                "air (24.1.7).",
                "Root epidermal cells have root hairs, which add surface for taking up water (24.1.7).",
                "Trichomes (hairs) on stems and leaves protect from sun and moisture loss and discourage plant-eaters "
                "(24.1.8).",
                "The lower leaf surface has stomata. In older woody plants the epidermis is replaced by periderm "
                "(cork) (24.1.8).",
            ]),
            ("Ground tissue", [
                "Parenchyma: the least specialized and most abundant cells; they can divide, and some contain "
                "chloroplasts and photosynthesize (24.1.10).",
                "Collenchyma: thicker walls; flexible support for young stems (the strings in celery) (24.1.10).",
                "Sclerenchyma: thick walls with lignin, mostly dead at maturity; rigid support. Fibers are long "
                "(hemp, rope); sclereids are short (nutshells, seed coats) (24.1.11).",
            ]),
            ("Vascular tissue", [
                "Xylem carries water and minerals up. Its conducting cells are tracheids (long, tapered, water passes "
                "through pits) and vessel elements (larger, with perforation plates, joined end to end into open "
                "pipes) (24.1.13, 24.1.15).",
                "Phloem carries sugar. Its conducting cells, sieve-tube members, have cytoplasm but no nucleus and "
                "connect through sieve plates; each has a companion cell, with a nucleus, that supports it (24.1.16).",
                "Where they are: the vascular cylinder in roots, vascular bundles in stems, veins in leaves (24.1.13).",
            ]),
            "Traps: tracheids vs vessel elements (both xylem); sieve-tube member (no nucleus) vs companion cell; "
            "collenchyma (flexible, living) vs sclerenchyma (rigid, mostly dead) (24.1.10, 24.1.11, 24.1.15, 24.1.16).",
        ],
        2: [
            "The vegetative organs are all the plant parts except the reproductive ones: roots, stems and leaves. Most "
            "flowering plants have a root system below ground and a shoot system above (24.2.18).",
            "The shoot system is the stem, branches and leaves. Nodes are where leaves attach to the stem; internodes "
            "are the stretches of stem between nodes (24.2.20). A terminal bud sits at the stem tip, and axillary buds "
            "sit where leaves meet the stem (24.2.21, 24.4.35).",
            ("Monocots vs eudicots", [
                "Monocots: one cotyledon, which transfers nutrients from the endosperm; parallel leaf veins; flower "
                "parts in threes; root vascular tissue in a ring (24.2.22).",
                "Eudicots: two cotyledons, which supply the seedling's nutrients; netted leaf veins; flower parts in "
                "fours or fives; root phloem between the arms of the xylem (24.2.23).",
            ]),
            "Annual plants live one growing season: they make flowers and seeds, then die. Perennial plants live three "
            "or more seasons. The flower-inducing genes LEAFY and Apetala 1 act as the switch: blocking them in an "
            "annual makes it grow like a perennial (24.2.25).",
        ],
        3: [
            "Root zones, from the tip up (24.3.26): the root cap protects the root apical meristem; then come the zone "
            "of cell division, the zone of elongation (cells lengthen and start to specialize) and the zone of "
            "maturation (fully differentiated cells, with root hairs).",
            ("Root tissues, from the outside in", [
                "Epidermis: the outer layer (24.3.27).",
                "Cortex: parenchyma cells that water and minerals move through (24.3.27).",
                "Endodermis: the boundary around the vascular cylinder. Its Casparian strip is waterproof, so water "
                "and minerals must pass through the endodermal cells themselves (24.3.27).",
                "Pericycle: dividing cells where branch (lateral) roots start (24.3.27).",
                "The vascular cylinder in the center (24.3.27, 24.3.28).",
            ]),
            "Monocot roots have the same growth zones, but pith in the center surrounded by a ring of vascular tissue, "
            "and they don't undergo secondary growth (24.3.30).",
            "Root types (24.3.32): a taproot is one long, fleshy main root that grows straight down and stores food; a "
            "fibrous root system is many slender roots that anchor the plant (found in monocots). Some roots are "
            "specialized: storage roots, prop roots, pneumatophores that let swamp roots get oxygen, and aerial roots "
            "(24.3.32, 24.3.33).",
            "Root partners (24.3.34): mycorrhizae are fungi that live with roots and help them extract water and "
            "minerals; root nodules contain nitrogen-fixing bacteria, because plants can't take nitrogen from the air "
            "themselves.",
        ],
        4: [
            "A woody twig (24.4.35, 24.4.36): the terminal bud at the tip is protected by bud scales. Each spring the "
            "scales drop and leave a scar, so each ring of scars is one year of growth. Leaves attach at nodes, with "
            "axillary buds above them.",
            "Herbaceous (non-woody) stems have only primary growth and are covered with a waxy cuticle. Their vascular "
            "bundles are in a ring in eudicots and scattered in monocots (24.4.38, 24.4.39, 24.4.40).",
            "Woody stems also have secondary growth, which makes them thicker; secondary tissues come from lateral "
            "meristems each year (24.4.41, 24.4.42). A woody stem has three regions: bark, wood and pith (24.4.42). "
            "The slide's \"woody stems have no vascular tissue\" is wrong: wood is secondary xylem, and bark contains "
            "phloem (24.4.44, 24.4.45).",
            "Bark contains cork, cork cambium, cortex and phloem. Girdling (removing a ring of bark all the way "
            "around) kills a tree, because the phloem in the bark can no longer carry organic nutrients (24.4.44).",
            "Wood is secondary xylem that builds up year after year. One annual ring is spring wood plus summer wood; "
            "summer wood has fewer vessels. In older trees the inner rings, the heartwood, no longer carry water "
            "(24.4.45, 24.4.47).",
            "Stem types (24.4.48, 24.4.49): stolons are above-ground horizontal stems that make new plants where nodes "
            "touch the ground; rhizomes are underground horizontal stems; tubers (potato) are enlarged storage stems; "
            "corms are underground stems that make new plants the next season. Uses: sugar cane gives table sugar, "
            "bark gives cinnamon and quinine, and wood gives paper and building materials (24.4.48).",
        ],
        5: [
            "The leaf is the main organ of photosynthesis, which needs water, carbon dioxide and sunlight (24.5.50). A "
            "foliage leaf has a wide blade on a stalk called the petiole (24.5.50).",
            "Inside a leaf (24.5.51, 24.5.52): upper and lower epidermis with a waxy cuticle and trichomes, stomata in "
            "the lower epidermis for gas exchange, and the mesophyll in between. In eudicots the mesophyll is palisade "
            "mesophyll (elongated cells near the top) over spongy mesophyll (irregular cells with air spaces). Leaf "
            "veins carry the xylem and phloem.",
            "Leaves vary (24.5.53, 24.5.54): they can be arranged alternate, opposite or whorled on the stem; the blade "
            "can be simple or compound; and they adapt to their environment, as shade leaves, spines, climbing "
            "tendrils or insect-catching leaves (24.5.53, 24.5.55).",
            "Traps: stolon vs rhizome; palisade vs spongy mesophyll; simple vs compound leaves; taproot vs fibrous "
            "roots (24.3.32, 24.4.48, 24.5.51, 24.5.53).",
        ],
    },
    "look_up": [
        "Which tissue does which job: the ground-tissue and vascular-tissue tables.",
        "Root zones and root tissues in order: the root tables.",
        "Stem types, leaf types and leaf adaptations: the stem and leaf tables.",
        "Monocot vs eudicot details: the comparison table and 24.2.22, 24.2.23.",
    ],
}

QUICK_GUIDE[25] = {
    "intro": [
        "Ch 25 is about how a plant feeds itself. It builds most of its body from carbon dioxide and water, takes other "
        "elements from the soil as minerals, pulls water up through the xylem, and pushes sugar through the phloem to "
        "wherever it's needed (25.1.3, 25.2.19, 25.3.28, 25.3.29).",
    ],
    "sections": {
        1: [
            "About 95% of a plant's dry weight is carbon, hydrogen and oxygen, which come from carbon dioxide and water "
            "(25.1.3). Everything else enters through the roots as minerals.",
            "A nutrient is essential if it has an identifiable role, no other nutrient can substitute for it, and a "
            "deficiency causes the plant to die (25.1.4). Macronutrients are needed in large amounts; micronutrients in "
            "small amounts (25.1.4). The slide's macronutrient list leaves out nitrogen; the textbook includes it.",
            "Hydroponics (growing plants in water with dissolved nutrients) showed which nutrients are essential: omit "
            "one and the plant grows poorly (25.1.6, 25.1.7). Fertilizer's three numbers, NPK, give its nitrogen, "
            "phosphorus and potassium (25.1.6, 25.1.8).",
            ("Soil", [
                "Soil is mineral particles, decaying organic material, living organisms, air and water. It forms by "
                "weathering of rock, which can be mechanical (wind, rain, ice) or chemical (25.1.9).",
                "Its particles are sand (largest; water drains fast), silt and clay (smallest) (25.1.10).",
                "Humus (decaying organic matter) decreases runoff, prevents leaching and holds positively charged "
                "minerals (25.1.11).",
                "Cation exchange: negatively charged clay and humus hold positive minerals such as calcium and "
                "potassium. Hydrogen ions from the root swap places with them, so the root can take them up (25.1.12).",
                "Soil profile: the A horizon (topsoil, with litter and humus), the B horizon (subsoil, with inorganic "
                "nutrients) and the C horizon (weathered parent material) (25.1.15, 25.1.16).",
            ]),
            "Erosion is water or wind carrying soil away. Crop rotation, reduced tillage, companion crops and trees "
            "reduce it (25.1.17, 25.1.18).",
        ],
        2: [
            "Water and minerals enter the root by the same pathways: between the porous cell walls until the Casparian "
            "strip forces them into the endodermal cells, or through root hairs and from cell to cell (25.2.19).",
            "Plant cells spend energy to take up minerals actively and concentrate them; the Casparian strip prevents "
            "minerals from leaking back out (25.2.20).",
            ("Order of mineral uptake", [
                "1. A proton pump in the plasma membrane pushes hydrogen ions (H+) out of the cell (25.2.21).",
                "2. The resulting electrochemical gradient drives positive ions such as K+ into the cell, through "
                "channel proteins (25.2.21, 25.2.23).",
                "3. Negative mineral ions, such as nitrate, come in together with H+ through carrier proteins "
                "(25.2.21, 25.2.23).",
            ]),
            "Helpers (25.2.24, 25.2.25, 25.2.26): Rhizobium bacteria in root nodules fix nitrogen from the air, and the "
            "host plant gives them carbohydrates; mycorrhizal fungi add surface for taking up water and minerals, and "
            "get sugars from the root. Other plants get nutrients other ways: parasitic plants tap a host plant, and "
            "carnivorous plants such as the sundew digest insects (25.2.27).",
        ],
        3: [
            "Xylem carries water and minerals from the bottom of the plant to the top, through tracheids and vessel "
            "elements. Phloem carries sucrose in any direction, through sieve-tube members with companion cells "
            "(25.3.28, 25.3.29).",
            "Water potential is the energy of water. Water moves passively from higher to lower water potential: from "
            "the soil into the root, up the stem, out of the leaves into the air (25.3.31, 25.3.32). Pressure raises "
            "water potential and dissolved solutes lower it (25.3.33). Turgor pressure, the pressure of water inside a "
            "cell, keeps it firm; a wilted plant has lost it (25.3.34).",
            "Water entering the roots creates root pressure, which pushes some water up and can force droplets out of "
            "leaf edges (guttation) (25.3.35, 25.3.36).",
            "Cohesion-tension model (25.3.37, 25.3.38, 25.3.39): transpiration, water evaporating from the leaves "
            "through stomata, pulls on the water in the xylem. Cohesion (water molecules clinging together) keeps the "
            "column unbroken from leaf to root, and adhesion (water clinging to the vessel walls) holds it up. It's "
            "passive: the plant spends no energy.",
            "Stomata (25.3.41, 25.3.42): each stoma is bordered by two guard cells. Potassium ions are actively pumped "
            "into the guard cells, water follows by osmosis, turgor rises and the stoma opens; when they leave, it "
            "closes. Light regulates opening and closing, and the hormone ABA can close them. The waxy cuticle "
            "prevents water loss while they're closed (25.3.39).",
            "Pressure-flow model (25.3.43 to 25.3.47): at a source (a leaf), sucrose is actively loaded into the sieve "
            "tubes using a hydrogen-ion gradient (25.3.45). Water follows by osmosis, building pressure that pushes "
            "the sap to a sink, such as roots or fruit, where the sugar is unloaded and used or stored (25.3.46). "
            "Evidence: girdling makes the bark swell just above the cut, where sugar collects, and aphids tap the "
            "sieve tubes to collect phloem sap (25.3.43, 25.3.48).",
            "Traps: cohesion vs adhesion; source vs sink; xylem (bottom to top, pulled) vs phloem (any direction, "
            "pushed); minerals taken up actively vs water entering passively (25.2.20, 25.3.29, 25.3.37, 25.3.43).",
        ],
    },
    "look_up": [
        "Which nutrients are macro and micro: the nutrients table (add N, which the slide leaves out).",
        "Soil horizons A, B and C: the soil table.",
        "The three steps of mineral uptake, and how stomata open and close: the sequences.",
        "Exact numbers (particle sizes, humus percentages, erosion statistics): don't memorize them.",
    ],
}

QUICK_GUIDE[26] = {
    "intro": [
        "Plants can't move away from danger or toward food, so they respond by changing how they grow (26.1.3). Ch 26 "
        "covers the hormones that carry signals around the plant (26.1), growth and movement responses to light, "
        "gravity and touch (26.2), and phytochrome, the pigment that lets plants measure day and night length (26.3).",
    ],
    "sections": {
        1: [
            "Plants respond to stimuli such as light, gravity, carbon dioxide, infection, drought and touch. Some "
            "responses are short-term (stomata opening and closing); others are long-term (roots growing down and "
            "stems growing up) (26.1.3).",
            "Signal transduction (26.1.4, 26.1.5): a receptor is activated by a signal; a chain of relay proteins "
            "amplifies it and passes it on; the cell responds, often by turning genes on or off.",
            "Hormones are chemical signals made in one part of the plant that travel in the phloem or from cell to "
            "cell and coordinate cell responses (26.1.6).",
            ("The five hormones", [
                "Auxin: made in the shoot apical meristem. It stops the axillary buds below from growing (apical "
                "dominance), promotes root and fruit growth, prevents leaf loss, and bends stems toward light "
                "(26.1.8). Synthetic auxins are used as weed killers (26.1.10).",
                "Gibberellins: growth-promoting hormones that cause stem elongation and break dormancy (26.1.12, "
                "26.1.13).",
                "Cytokinins: promote cell division and organ formation; with auxin, their ratio decides which organs "
                "form; low levels in autumn let leaves change color and die (26.1.14, 26.1.15, 26.1.16).",
                "Abscisic acid (ABA), the stress hormone: starts and maintains seed and bud dormancy and closes "
                "stomata. Corn that can't respond to it sprouts on the cob (26.1.17, 26.1.18, 26.1.19).",
                "Ethylene: a gas made from the amino acid methionine; it causes leaves, fruit or flowers to drop "
                "(abscission) and ripens fruit (26.1.20, 26.1.21, 26.1.22).",
            ]),
            "How auxin bends a stem toward light (26.1.9, 26.1.11): when light comes from one side, auxin moves to the "
            "shady side. There, cells pump hydrogen ions into their walls, the walls loosen, water enters and the "
            "cells stretch, so the stem bends toward the light.",
            "Plants also defend themselves against living threats, such as plant-eaters and parasites, by making "
            "protective chemicals (26.1.23).",
        ],
        2: [
            "A tropism is growth toward (positive) or away from (negative) a stimulus that comes from one direction "
            "(26.2.24).",
            ("Tropisms", [
                "Phototropism (light): stems grow toward light because cells on the shady side elongate under auxin. "
                "The receptor pigment, phototropin, absorbs blue light (26.2.25, 26.2.26).",
                "Thigmotropism (touch): tendrils of runner beans and morning glories coil around supports. "
                "Thigmomorphogenesis is a change in the whole plant's shape because of touch or wind (26.2.27).",
                "Gravitropism (gravity): a plant laid on its side grows its stem upward and its roots downward. "
                "Statoliths, starch grains inside amyloplasts in root-cap cells, settle to the bottom of the cell and "
                "signal which way is down (26.2.29). The slide's \"stems with root caps grow downward\" means roots.",
            ]),
            "Arabidopsis thaliana, a small plant related to cabbage and mustard with no commercial value, is the model "
            "organism for studying plant molecular genetics (26.2.31).",
            "Turgor (nastic) movements don't involve growth and don't depend on the stimulus's direction; they come "
            "from changes in water pressure inside cells. Examples: Mimosa leaflets folding when touched, the Venus "
            "flytrap closing, and daily sleep movements (26.2.33, 26.2.35).",
        ],
        3: [
            "Photoperiodism is any response to changes in day or night length, such as when to flower. It needs a "
            "biological clock and a photoreceptor pigment called phytochrome (26.3.36).",
            "Phytochrome has two forms (26.3.37, 26.3.38, 26.3.39): Pr absorbs red light (in daylight) and becomes "
            "Pfr, the active form; Pfr turns back into Pr in darkness or far-red light. Switching between them lets "
            "the plant detect changes in day length. Phytochrome also promotes seed germination and flowering and "
            "inhibits shoot elongation.",
            "Flowering (26.3.40, 26.3.41, 26.3.42): short-day plants flower when the day is shorter than a critical "
            "length, so they're really long-night plants; long-day plants flower when the day is longer. A flash of "
            "light that interrupts the long night stops a short-day plant from flowering but lets a long-day plant "
            "flower. Day-neutral plants flower whatever the day length.",
            "Shade and spacing (26.3.43, 26.3.44): leaf shade increases far-red light relative to red, which tells a "
            "plant it has neighbors, and it grows taller to compete. In darkness, stems keep elongating and stay "
            "yellow (etiolation; textbook).",
            "Circadian rhythms are roughly 24-hour cycles that keep going even without outside cues, run by a "
            "biological clock; sleep movements of leaves are an example (26.3.45, 26.3.46).",
            "Traps: tropism (growth, directional) vs turgor movement (not growth); Pr vs Pfr; short-day (long-night) "
            "vs long-day plants (26.2.24, 26.2.33, 26.3.39, 26.3.41).",
        ],
    },
    "look_up": [
        "Each hormone's effects and commercial uses: the hormone table (26.1.7).",
        "Short-day, long-day and day-neutral plants, and what a night flash does: the photoperiod table.",
        "Which tropism responds to what, and which receptor: the tropism table.",
    ],
}

QUICK_GUIDE[27] = {
    "intro": [
        "Ch 27 follows a flowering plant's life cycle in detail: how a flower makes pollen and the embryo sac, "
        "pollination and double fertilization, how the embryo develops inside the seed, fruits and how seeds spread, "
        "germination, and reproduction without seeds (27.1.3, 27.2.20, 27.3.27, 27.4.36).",
    ],
    "sections": {
        1: [
            "The diploid sporophyte, the plant you see, is dominant: it bears the flowers and makes haploid spores by "
            "meiosis (27.1.3). A microspore becomes the male gametophyte (the pollen grain), and a megaspore becomes "
            "the female gametophyte (27.1.5). The slide calls the spores themselves gametophytes; each spore becomes "
            "one.",
            "Flowers are unique to angiosperms: they attract pollinators and produce fruits that enclose seeds (27.1.6). "
            "A eudicot flower has four whorls attached to a receptacle at the end of a stalk called the peduncle: sepals "
            "protect the bud, petals attract pollinators, stamens make pollen, and carpels hold the ovules (27.1.7).",
            "Complete flowers have sepals, petals, stamens and a carpel; incomplete flowers lack one or more. Perfect "
            "flowers have both stamens and carpels; imperfect flowers have only one kind (27.1.10). Monoecious plants "
            "carry both kinds of imperfect flower; dioecious plants (holly) carry only one kind per plant (27.1.10, "
            "27.1.11).",
            "Male gametophyte (27.1.12): each anther has four pollen sacs with many microspore mother cells. Meiosis "
            "makes four haploid microspores; each becomes a pollen grain with a tube cell and a generative cell, and "
            "the generative cell divides into two sperm.",
            "Female gametophyte (27.1.14): in the ovule, a megaspore mother cell undergoes meiosis to make four "
            "megaspores, and three of them die. The survivor divides by mitosis into the embryo sac, with eight "
            "nuclei: the egg, two synergids beside it, a central cell with two polar nuclei, and three antipodal "
            "cells. The ovule's integuments become the seed coat.",
            "Pollination is the transfer of pollen from an anther to a stigma: self-pollination if the pollen comes "
            "from the same plant, cross-pollination if it comes from another plant of the same species (27.1.15). "
            "Fertilization comes afterwards: the pollen grain germinates on the stigma, its pollen tube grows through "
            "the style to the ovule's micropyle, and double fertilization follows: one sperm + the egg make the "
            "zygote, the other + the polar nuclei make the endosperm (27.1.17).",
            "Pollinators (27.1.18, 27.1.19; textbook): bees prefer yellow, blue or white flowers with ultraviolet "
            "markings; hummingbirds prefer red, tube-shaped flowers with lots of nectar; bats prefer large, pale "
            "flowers that open at night.",
        ],
        2: [
            "Development is a programmed series of stages from simple to complex (27.2.20). After double "
            "fertilization, the zygote divides into an embryo and a suspensor that anchors it. The embryo goes "
            "through a globular stage, then a heart stage when the cotyledons appear, then a torpedo stage as it "
            "elongates (27.2.20, 27.2.21).",
            "The mature embryo (27.2.22): the epicotyl, above the cotyledons, becomes the shoot; the hypocotyl, below "
            "them, becomes the stem; the radicle is the embryonic root.",
            "Monocot vs eudicot seeds (27.2.25, 27.2.26): a monocot has one cotyledon, which stores some nutrients, "
            "absorbs others from the endosperm and passes them to the embryo; eudicot cotyledons store all the "
            "nutrients the embryo needs.",
        ],
        3: [
            "A fruit is a mature ovary (27.3.27). Simple fruits come from a single ovary; aggregate fruits from many "
            "ovaries of one flower (blackberry); multiple fruits from the ovaries of many flowers (pineapple) "
            "(27.3.27).",
            "The ovary wall becomes the pericarp, with up to three layers: exocarp (the skin), mesocarp (the flesh) "
            "and endocarp (around the seed) (27.3.28). Dry fruits either split open when ripe (dehiscent: legumes) or "
            "stay closed (indehiscent: grains) (27.3.29). Named fruit types include drupe, berry, legume and samara "
            "(27.3.30).",
            "Fruits help spread seeds: by wind (hairs, plumes, wings), by animals that eat the fruit, and by hooks and "
            "spines that catch on fur and clothing (27.3.31, 27.3.32).",
            "Germination (27.3.33, 27.3.34, 27.3.35): the embryo resumes growth. Some seeds must go through a dormant "
            "period first; in temperate zones cold weather breaks dormancy, and fleshy fruits contain inhibitors so "
            "seeds don't sprout on the plant. A seed needs oxygen, warmth and water. In corn, a sheath called the "
            "coleoptile covers the first leaf as it grows up.",
        ],
        4: [
            "Asexual reproduction makes clones, genetically identical copies. Plants use stolons (horizontal stems "
            "above ground), rhizomes (underground stems) and tubers; new growth starts at the nodes of stems, and a "
            "potato's \"eyes\" are buds (27.4.36, 27.4.37).",
            "Tissue culture grows a plant tissue on an artificial medium. It works because many plant cells are "
            "totipotent: each can become an entire plant (27.4.38). Meristem tissue on a medium with auxin, cytokinins "
            "and nutrients first forms an undifferentiated callus, then organs, then plantlets, all clones (27.4.39, "
            "27.4.40). In cell suspension culture, cells grow in liquid to make chemicals, such as heart drugs from "
            "Digitalis (27.4.40).",
            "Traps: pollination vs fertilization; microspore vs megaspore; epicotyl vs hypocotyl vs radicle; "
            "aggregate vs multiple fruit; dehiscent vs indehiscent (27.1.15, 27.1.17, 27.2.22, 27.3.27, 27.3.29).",
        ],
    },
    "look_up": [
        "The cells of the embryo sac and the steps of each gametophyte: the gametophyte table.",
        "Fruit types and examples: the fruit table.",
        "Pollinators and their flowers: the pollinator table.",
        "Germination steps for bean and corn: 27.3.35.",
    ],
}
