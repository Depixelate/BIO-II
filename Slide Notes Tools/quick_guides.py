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
        "Ch 24 is the anatomy of a flowering plant, built up from cells to tissues to organs. As in animals, a cell is "
        "the basic unit of life; a tissue is a group of specialized cells doing one job; an organ, such as a root, stem "
        "or leaf, is made of several tissues (24.1.4).",
        "Everything grows from meristems: undifferentiated cells that keep dividing for the plant's whole life. Each "
        "division leaves one meristem cell and one cell that goes on to specialize (24.1.5, 24.1.6). The new cells "
        "become three tissue types: epidermal tissue (the outer covering), ground tissue (the filler that "
        "photosynthesizes, stores and supports) and vascular tissue (the plumbing: xylem and phloem) (24.1.3, 24.1.6). "
        "These tissues build the three vegetative organs: roots, stems and leaves (24.2.18).",
        "Two kinds of growth run through the chapter. Primary growth, from apical meristems at the tips, makes roots and "
        "stems longer; secondary growth, from lateral meristems, makes woody stems thicker (24.1.6, 24.4.41, 24.4.42). "
        "The chapter is very term-heavy: understand the ideas here, and look up the names in the tables.",
    ],
    "sections": {
        1: [
            "Apical meristems at the tips of stems and roots make them longer. They produce three primary meristems, "
            "each of which makes one tissue type: protoderm makes epidermal tissue, ground meristem makes ground tissue, "
            "and procambium makes vascular tissue (24.1.3, 24.1.6).",
            ("Epidermal tissue: the protective skin", [
                "Closely packed epidermal cells; where they face the air they're covered by a waxy cuticle, which "
                "limits water loss (24.1.7).",
                "Root epidermal cells grow root hairs, which increase the root's surface area for absorbing water "
                "(24.1.7).",
                "Epidermal cells of stems, leaves and reproductive organs grow trichomes (hairs), which protect from "
                "sun and moisture loss and discourage herbivory (being eaten) (24.1.8).",
                "The lower leaf surface has stomata: pores, each between two guard cells, for gas exchange (24.1.8, "
                "24.1.9).",
                "In older woody stems the epidermis is replaced by periderm, mainly cork, made by the cork cambium "
                "(24.1.8). Cork cells contain waterproof suberin, so gases pass only at lenticels, loose spots in the "
                "cork (24.4.44).",
            ]),
            ("Ground tissue: the bulk of the plant", [
                "Parenchyma: the least specialized and most abundant cells, found in every organ. They can divide and "
                "give rise to more specialized cells, and those with chloroplasts photosynthesize (24.1.10).",
                "Collenchyma: living cells with thicker primary walls, in bundles under the epidermis; flexible "
                "support for young regions, like the strings in celery stalks (24.1.10).",
                "Sclerenchyma: thick secondary walls hardened with lignin; most are dead at maturity; they support "
                "mature regions. Fibers are long and slender (hemp, rope); sclereids are shorter and varied (seed "
                "coats, nutshells) (24.1.11).",
            ]),
            ("Vascular tissue: the plumbing", [
                "Xylem carries water and minerals from the roots to the leaves. Its two water-conducting cells are "
                "tracheids, long with tapered ends, where water crosses through pits in the walls, and vessel "
                "elements, larger, with perforation plates in their end walls, lined up into a continuous vessel "
                "(24.1.13, 24.1.15). Both are dead and hollow when they work (textbook).",
                "Vascular rays between rows of tracheids carry water sideways, across the width of the plant "
                "(24.1.15).",
                "Phloem carries sucrose and other organic compounds. Its conducting cells, sieve-tube members, have "
                "cytoplasm but no nucleus, and their walls have sieve plates (clusters of pores). Each has a companion "
                "cell, which has a nucleus and helps with transport; plasmodesmata (channels between plant cells) "
                "connect the two (24.1.16).",
                "Where it is: the vascular cylinder in roots, vascular bundles in stems, leaf veins in leaves "
                "(24.1.13).",
            ]),
            "Traps: tracheid vs vessel element (both xylem, both carry water); sieve-tube member (no nucleus) vs "
            "companion cell (nucleus); collenchyma (living, flexible) vs sclerenchyma (mostly dead, rigid, lignin); "
            "fibers (long) vs sclereids (short) (24.1.10, 24.1.11, 24.1.15, 24.1.16).",
        ],
        2: [
            "Vegetative organs are all the plant parts except the reproductive structures (flowers, seeds and fruits); "
            "they handle growth and nutrition. There are three: roots, stems and leaves (24.2.18). Most flowering "
            "plants have a root system, which is just the roots, and a shoot system, the stem and leaves (24.2.18, "
            "24.2.19).",
            "The stem is the main axis; it grows longer and produces leaves. Nodes are where leaves attach; internodes "
            "are the stretches of stem between nodes. The terminal bud at the stem's end contains the shoot apical "
            "meristem and produces new leaves (24.2.20, 24.2.21). Lateral (axillary) buds sit where a leaf joins the "
            "stem and can grow into branches (24.2.19, 24.2.21).",
            ("Monocots vs eudicots (24.2.22 to 24.2.24)", [
                "Cotyledons (seed leaves): monocots have one, which acts as transfer tissue, passing on nutrients "
                "from the endosperm; eudicots have two, which supply the seedling's nutrients themselves (24.2.22, "
                "24.2.23).",
                "Roots: monocot vascular tissue is in a ring; in eudicots the phloem sits between the arms of the "
                "xylem (24.2.22, 24.2.23).",
                "Stems: monocot vascular bundles are scattered; eudicot bundles are in a distinct ring (24.2.24).",
                "Leaves: monocots have parallel veins; eudicots have netted veins (24.2.22, 24.2.23).",
                "Flowers: monocot parts in threes; eudicot parts in fours or fives. Pollen: monocots have one pore or "
                "slit, eudicots three (24.2.24).",
            ]),
            "Annual plants live one growing season: they make just enough vegetative structures to support flowers "
            "and seeds, and die after the seeds are dispersed. Perennial plants live three or more seasons and spend "
            "energy on vegetative structures that let them survive for years (24.2.25).",
            "The switch between the two is a pair of flower-inducing genes, LEAFY and Apetala 1: when they turn on, "
            "the shoot apical meristem stops making leaves and starts making flowers (textbook). Blocking these genes "
            "in an annual makes it grow like a perennial (24.2.25).",
        ],
        3: [
            "Root zones, from the tip up (24.3.26, 24.3.28): the root cap covers and protects the root apical "
            "meristem; in the zone of cell division the primary meristems divide; in the zone of elongation cells "
            "lengthen and begin to specialize; in the zone of maturation cells are fully differentiated, and root "
            "hairs grow there.",
            ("Eudicot root tissues, from the outside in", [
                "Epidermis: the outer layer of the root, with the root hairs (24.3.27, 24.3.28).",
                "Cortex: parenchyma cells; water and minerals move between and through them (24.3.27). It mainly "
                "stores food (textbook).",
                "Endodermis: one layer of cells forming the boundary between the cortex and the vascular cylinder. "
                "Its Casparian strip, made of lignin and suberin, is a waterproof band, so water and minerals can't "
                "slip between the cells and must pass through the endodermal cells, which control what enters "
                "(24.3.27, 24.3.28). The slide says \"protein lignin\" (so does the textbook), but lignin isn't a "
                "protein.",
                "Pericycle: just inside the endodermis; its cells keep dividing and start branch (lateral) roots, "
                "which grow out through the cortex (24.3.27, 24.3.29).",
                "Vascular cylinder: in eudicots, star-shaped xylem with phloem between its arms (24.2.23, 24.3.28).",
            ]),
            "Monocot roots have the same growth zones and the same layers (pericycle, endodermis, cortex, "
            "epidermis), but a central pith surrounded by a ring of vascular tissue, and they don't undergo secondary "
            "growth (24.3.30, 24.3.31). (One textbook sentence says they do, but the textbook also says secondary "
            "growth occurs only in conifers and woody eudicots, which agrees with the slide.)",
            "Root types (24.3.32): a taproot is one long, fleshy main root that grows straight down and stores food "
            "(eudicots; textbook); a fibrous root system is many slender roots and lateral branches that anchor the "
            "plant (monocots).",
            ("Root specializations (24.3.32, 24.3.33; examples from the textbook)", [
                "Storage roots store large amounts of carbohydrate (sweet potato) (24.3.32, 24.3.33).",
                "Prop roots grow from the base of the stem for support in high wind (corn) (24.3.32, 24.3.33).",
                "Pneumatophores grow up out of the water so the roots can get oxygen (mangrove, bald cypress) "
                "(24.3.33).",
                "Aerial roots support, climb or take up moisture and sunlight (orchids, English ivy) (24.3.32, "
                "24.3.33).",
            ]),
            "Root partners (24.3.34): mycorrhizae are mutualistic fungi on roots that help extract water and minerals. "
            "Root nodules hold nitrogen-fixing bacteria: plants can't extract nitrogen from the air, but the bacteria "
            "take it up and reduce it, so the plant gets nitrogen and the bacteria get carbohydrates.",
            "Traps: root cap (protects the tip) vs root hairs (absorb, in the zone of maturation); endodermis "
            "(Casparian strip, controls entry) vs pericycle (makes branch roots); taproot vs fibrous roots; "
            "mycorrhizae (fungi) vs nodules (bacteria) (24.3.26, 24.3.27, 24.3.32, 24.3.34).",
        ],
        4: [
            "A woody twig (24.4.35, 24.4.36): the terminal bud at the tip holds the shoot tip, protected by bud "
            "scales. Each spring the scales drop and leave a ring of scars, so each scar ring marks one year of "
            "growth. Leaves attach at nodes, with axillary buds; lenticels dot the bark.",
            "The shoot apical meristem, inside the terminal bud and wrapped in leaf primordia (young leaves), makes "
            "the cells that lengthen the stem. Its primary meristems: protoderm makes the epidermis, ground meristem "
            "makes the pith and cortex, procambium makes primary xylem and phloem. Mature vascular bundles also "
            "contain vascular cambium (24.4.35, 24.4.37).",
            "Herbaceous (non-woody) stems have only primary growth and a waxy cuticle. Their vascular bundles are in "
            "a distinct ring in eudicots, with cortex outside and pith inside, and scattered in monocots (24.4.38, "
            "24.4.39, 24.4.40).",
            "Woody stems have both primary growth, which adds length, and secondary growth, which adds girth "
            "(thickness). Secondary tissues come from lateral meristems: the vascular cambium makes secondary xylem "
            "and secondary phloem each year, and the cork cambium makes cork (24.4.41, 24.4.42, 24.4.43).",
            "A woody stem has three regions: bark, wood and pith (24.4.42, 24.4.46). The slide's \"woody stems have "
            "no vascular tissue\" is wrong (the professor confirmed it): wood is secondary xylem and bark contains "
            "phloem (24.4.44, 24.4.45). The slide also lists only bark and pith; the third region is wood.",
            "Bark is everything outside the vascular cambium: cork, cork cambium, cortex and phloem (24.4.44). "
            "Girdling, removing a ring of bark all the way around, kills the tree, because the phloem in the bark "
            "can no longer carry organic nutrients (24.4.44).",
            "Wood is secondary xylem that builds up year after year; the vascular cambium is dormant in winter. Each "
            "annual ring is spring wood plus summer wood, and summer wood has fewer vessels, so counting rings gives "
            "the age. Sapwood, the outer rings, still carries water; heartwood, the inner rings of older trees, no "
            "longer does (24.4.45, 24.4.46, 24.4.47).",
            ("Stem types (24.4.48, 24.4.49)", [
                "Stolons: above-ground horizontal stems that make new plants where their nodes touch the ground "
                "(strawberry runners) (24.4.48, 24.4.49).",
                "Rhizomes: underground horizontal stems that contribute to asexual reproduction (iris) (24.4.48, "
                "24.4.49).",
                "Tubers: enlarged parts of rhizomes that store food; a potato is a tuber (24.4.48, 24.4.49).",
                "Corms: underground stems that make new plants the next season (gladiolus) (24.4.48, 24.4.49).",
                "Uses: sugar cane stems give table sugar; bark gives cinnamon and quinine; wood gives paper and "
                "building materials (24.4.48).",
            ]),
            "Traps: primary growth (length, apical meristems) vs secondary growth (girth, lateral meristems); bark vs "
            "wood; spring vs summer wood; heartwood vs sapwood; stolon (above ground) vs rhizome (below ground); "
            "bundles in a ring (eudicot) vs scattered (monocot) (24.4.38, 24.4.42, 24.4.45, 24.4.47, 24.4.48).",
        ],
        5: [
            "The leaf carries on most of the plant's photosynthesis, which needs water, carbon dioxide and sunlight "
            "(24.5.50). A foliage leaf is usually broad and thin: the blade is the wide part, the petiole is the "
            "stalk attaching it to the stem, and the leaf axil, the upper angle between petiole and stem, holds the "
            "axillary bud (24.5.50). Evergreens keep their leaves all year; deciduous plants lose all of them "
            "(24.5.50).",
            "Inside a leaf (24.5.51, 24.5.52): upper and lower epidermis with a waxy cuticle and trichomes; stomata "
            "in the lower epidermis for gas exchange; and mesophyll, the chloroplast-filled middle. In eudicots the "
            "mesophyll has two layers: palisade mesophyll, elongated cells near the top, and spongy mesophyll, "
            "irregular cells bounded by air spaces. Leaf veins bring water and minerals in through the xylem and "
            "carry sugar out through the phloem.",
            "The palisade layer does most of the photosynthesis, and the spongy layer's air spaces let carbon dioxide "
            "spread through the leaf (textbook). Carbon dioxide enters through the stomata, and oxygen and water "
            "vapor leave; the figure description saying carbon dioxide leaves is a slip (24.5.52).",
            "Leaf variety (24.5.53, 24.5.54): leaves are arranged on the stem as alternate (beech), opposite (maple) "
            "or whorled (bedstraw); a simple leaf has one blade (magnolia), while a compound leaf is divided into "
            "leaflets, pinnately in pairs (black walnut) or palmately from one point (buckeye).",
            "Leaves are adapted to their environment (24.5.53, 24.5.55; examples from the textbook): broad shade "
            "leaves; cactus spines, which are modified leaves that protect the fleshy stem; climbing leaves "
            "modified into tendrils (cucumber); reduced leaves (desert plants); and insect-catching leaves, as in "
            "the sundew (sticky hairs) and the Venus flytrap (hinged leaves that snap shut). Carnivorous plants grow "
            "where soil nitrogen is scarce, and the digested insects supply it (textbook).",
            "Traps: blade vs petiole; palisade vs spongy mesophyll; simple vs compound; alternate vs opposite vs "
            "whorled; evergreen vs deciduous; cactus spines are leaves, not stems (24.5.50, 24.5.51, 24.5.53, "
            "24.5.55).",
        ],
    },
    "look_up": [
        "Primary meristems and what each one makes; the three tissue types and their cells: the tissue tables.",
        "Root zones and root tissues in order, root types and root specializations: the root tables.",
        "Monocot vs eudicot: the comparison table.",
        "Stem types, leaf arrangements and leaf adaptations: the stem and leaf tables.",
        "Exact numbers: don't memorize them.",
    ],
}

QUICK_GUIDE[25] = {
    "intro": [
        "Ch 25 is about how a plant feeds itself and moves materials around. A plant builds most of its body from "
        "carbon dioxide and water; everything else comes from the soil as minerals (25.1.3). Water and minerals "
        "travel up in the xylem, and sugar travels in the phloem to wherever it's needed (25.3.28, 25.3.29).",
        "Most of the chapter is about how things move. Water always moves passively, from higher to lower water "
        "potential, and the plant spends no energy on it (25.3.31, 25.3.37). Minerals and sugar are moved actively: "
        "a pump uses ATP to push hydrogen ions (H+) out of a cell, and the H+ gradient then drives minerals and "
        "sugar across the membrane (25.2.21, 25.3.45).",
        "This deck is from the same edition as the textbook, so the slides and the book match closely.",
    ],
    "sections": {
        1: [
            "About 95% of a plant's dry weight is carbon, hydrogen and oxygen, the building blocks of organic "
            "compounds such as carbohydrates. Carbon dioxide supplies the carbon, and water supplies the hydrogen "
            "and oxygen (25.1.3). Everything else is absorbed by the roots as minerals; a mineral is an inorganic "
            "substance, usually with two or more elements (25.1.3).",
            "Leaves take in carbon dioxide and release oxygen and water; roots take in water, oxygen and minerals "
            "and release carbon dioxide, because root cells carry on cellular respiration (25.1.5). That's why roots "
            "need air in the soil: overwatering fills the air spaces and the plant dies (textbook).",
            "A nutrient is essential if it has an identifiable role, no other nutrient can substitute for it, and a "
            "deficiency causes the plant to die (25.1.4). Essential nutrients are macronutrients, needed in larger "
            "amounts (C, H, O, N, P, K, S, Ca, Mg), or micronutrients, needed in smaller amounts (Fe, B, Mn, Cu, "
            "Zn, Cl, Mo) (25.1.4). The slide's macronutrient list leaves out nitrogen (N); the textbook includes it.",
            "Why minerals matter (textbook): nitrogen goes into nucleic acids and proteins, magnesium into "
            "chlorophyll, and iron into cytochromes.",
            "Hydroponics, growing plants in water with dissolved nutrients, proved that plants need only sunlight, "
            "water and minerals; leaving one nutrient out and watching growth suffer shows it's essential (25.1.6, "
            "25.1.7). Deficiencies cause stunted growth and other symptoms, such as light yellow leaves without "
            "nitrogen (25.1.6, 25.1.8). Fertilizer's NPK ratio is its percentage by weight of nitrogen, phosphorus "
            "and potassium (25.1.6, 25.1.8).",
            ("Soil", [
                "Soil is a mixture of mineral particles, decaying organic material, living organisms, air and water "
                "(25.1.9).",
                "It forms by weathering of rock: mechanical (wind, rain, ice, rock grinding on rock) or chemical "
                "(acid rain, degradation by lichens and mosses) (25.1.9).",
                "Particles: sand is largest, and water drains readily between the grains; silt is in between; clay "
                "is smallest, with small spaces that fill with water. Loam combines sand's aeration with the mineral "
                "retention of silt and clay (25.1.10).",
                "Humus (decaying organic material) decreases runoff, prevents leaching (minerals being washed away), "
                "makes soil more acidic and retains positively charged minerals; bacteria and fungi break it down "
                "and return its nutrients to plants (25.1.11).",
                "Living organisms: plant roots open soil to bedrock, earthworms and ants mix and aerate it, "
                "microorganisms decompose humus, and soil bacteria make nitrogen available to plants (25.1.14).",
            ]),
            "Cation exchange (25.1.12, 25.1.13): clay and humus are negatively charged, so they hold positive mineral "
            "ions such as calcium (Ca2+) and potassium (K+), which keeps them from leaching away. A root hair releases "
            "hydrogen ions (H+), which exchange places with those minerals, so the root can take them up. Cation "
            "exchange capacity (CEC) is how many negative sites a soil has to bind them; sandy soil has a lower CEC.",
            "A soil profile is a vertical section from the surface down to unaltered rock, in layers called horizons "
            "(25.1.15, 25.1.16): A, the topsoil, with litter and the most humus; B, the subsoil, where inorganic "
            "nutrients leached from above accumulate; C, the weathered parent material (bedrock). The profile varies "
            "with the parent rock and climate.",
            "Erosion is water or wind carrying soil away; plowing, overgrazing, clearing land and stronger coastal "
            "storms make it worse. Crop rotation, reduced tillage and companion crops reduce farmland erosion, and "
            "trees prevent coastal erosion (25.1.17, 25.1.18).",
            "Traps: macro vs micro (amount needed, not importance); sand (drains) vs clay (holds water); A vs B vs C "
            "horizon; leaching vs cation exchange (25.1.4, 25.1.10, 25.1.12, 25.1.15).",
        ],
        2: [
            "Water and minerals enter the root by the same two pathways (25.2.19, 25.2.23): pathway A, between the "
            "porous cell walls until the Casparian strip of the endodermis blocks the way and forces them into the "
            "endodermal cells; pathway B, into root hairs and then from cell to cell through plasmodesmata "
            "(cytoplasmic strands connecting neighboring cells). Either way, everything reaching the xylem has passed "
            "through the endodermal cells.",
            "Water enters root cells passively, by osmosis, when there is more water outside the root than inside; "
            "the slide words this as the root's osmotic pressure being lower than the soil's (25.2.19). Minerals are "
            "different: plant cells spend energy to take them up actively and concentrate them, and the Casparian "
            "strip prevents backflow, so root xylem holds far more minerals than the soil (25.2.19, 25.2.20).",
            ("Order of mineral uptake across the membrane", [
                "1. A proton pump in the plasma membrane uses ATP to pump hydrogen ions (H+) out of the cell "
                "(25.2.21, 25.2.23).",
                "2. The resulting electrochemical gradient drives positive ions such as potassium (K+) into the cell "
                "through channel proteins (25.2.21, 25.2.23).",
                "3. Negative mineral ions such as nitrate (NO3-) and phosphate (HPO4 2-) come in together with H+ "
                "through carrier proteins; this needs no extra energy, because H+ is moving down its gradient "
                "(25.2.21, 25.2.23).",
                "Using a gradient this way is chemiosmosis. The minerals then move into the xylem and up to the "
                "leaves (25.2.21).",
            ]),
            "Mutualisms for nutrients (25.2.24, 25.2.25, 25.2.26): Rhizobium bacteria in root nodules fix "
            "atmospheric nitrogen, and the host plant gives them carbohydrates. In mycorrhizae, the fungus increases "
            "the surface area for water and mineral uptake and breaks down organic matter, and the root gives the "
            "fungus sugars and amino acids; plants with mycorrhizae grow better.",
            "Other ways to get nutrients (25.2.24, 25.2.27): parasitic plants such as dodder wrap around a host plant "
            "and tap its xylem and phloem through root-like projections (haustoria, textbook); carnivorous plants such "
            "as the sundew trap prey on sticky hairs that release digestive enzymes.",
            "Traps: proton pump (H+ out, uses ATP) vs channel protein (K+ in) vs carrier protein (negative ions in "
            "with H+); nodules (bacteria, nitrogen) vs mycorrhizae (fungus, surface area); water enters passively vs "
            "minerals actively (25.2.20, 25.2.21, 25.2.24).",
        ],
        3: [
            "Xylem carries water and minerals from the bottom of the plant to the top, through tracheids and vessel "
            "elements. Phloem carries sucrose and other organic materials in any direction, through sieve-tube "
            "members, whose end walls are sieve plates crossed by plasmodesmata; companion cells supply them with "
            "proteins (25.3.28, 25.3.29, 25.3.30).",
            "Water potential is the energy of water; water always moves passively from higher to lower water "
            "potential (25.3.31). Two things set it (25.3.33): pressure (the higher the pressure, the higher the "
            "water potential) and solutes (the more solute, the lower the water potential, so water moves toward "
            "the side with more solute). Water potential falls from soil to root to stem to leaf, so water flows "
            "that way (25.3.32).",
            "Turgor pressure is the pressure that builds up inside a cell as water enters by osmosis. Turgid cells "
            "keep the plant firm; a wilted plant's cells have lost turgor, and water flows back in until the water "
            "potential is equal inside and out (25.3.33, 25.3.34).",
            "Root pressure: minerals concentrated in the root draw water in, creating a positive pressure that "
            "pushes xylem sap upward. It can force water droplets out of vein endings along leaf edges, which is "
            "guttation (25.3.35, 25.3.36). Root pressure alone can't lift water to the top of a tall tree (textbook).",
            "The cohesion-tension model (25.3.37, 25.3.38, 25.3.39) explains how water rises, passively, all the way "
            "up. Transpiration, water evaporating from the leaves through the stomata, creates tension that pulls on "
            "the water in the xylem. Cohesion, water molecules clinging to each other by hydrogen bonds, keeps the "
            "column unbroken from leaf to root, and adhesion, water sticking to the vessel walls, holds it in place. "
            "Water lost in the leaf is replaced from the leaf veins, the stem's column is pulled upward, and water "
            "enters the root xylem by osmosis. Transpired water rises as mist over forests (25.3.40).",
            "Stomata (25.3.41, 25.3.42): each stoma is bordered by two guard cells. To open, K+ is actively "
            "transported into the guard cells (H+ is pumped out, so H+ builds up outside), water follows by osmosis, "
            "turgor rises and the stoma opens. When K+ and then water leave, the stoma closes. Light regulates them, "
            "and ABA (abscisic acid) can close them. While stomata are closed, the waxy cuticle prevents water loss "
            "(25.3.39), but carbon dioxide can't enter, so photosynthesis slows (textbook).",
            "Phloem moves sap from source to sink (25.3.43, 25.3.44): a source is where sugar is made or comes from "
            "(older leaves); a sink is where it's unloaded (roots, young leaves). Evidence: girdling a tree below the "
            "leaves makes the bark swell just above the cut, where sugar accumulates; radioactive tracers confirm "
            "that phloem carries organic nutrients; and aphids, whose mouthparts tap the sieve tubes, are used to "
            "collect phloem sap (25.3.43, 25.3.48).",
            "The pressure-flow model (25.3.45, 25.3.46, 25.3.47): at the source, an ATP-driven pump pushes H+ out, "
            "and sucrose is loaded into the sieve tubes together with H+ (co-transport). Water follows by osmosis, "
            "creating high positive pressure, which pushes the sap toward the sink. At the sink, sugar is unloaded "
            "and used for cellular respiration or stored, and the water returns to the xylem.",
            "Traps: cohesion (water to water) vs adhesion (water to walls); transpiration (pull from the top) vs "
            "root pressure (push from below); xylem (one way, up, pulled, no energy) vs phloem (any direction, pushed, "
            "active loading); source vs sink; stomata open when K+ enters, close when it leaves (25.3.29, 25.3.35, "
            "25.3.37, 25.3.41, 25.3.43).",
        ],
    },
    "look_up": [
        "Macronutrients and micronutrients: the nutrients table (with N added).",
        "Soil particles, horizons and what humus does: the soil tables.",
        "The three steps of mineral uptake, stomata opening and closing, cohesion-tension and pressure-flow: the "
        "sequences.",
        "Xylem vs phloem: the comparison table.",
        "Exact numbers (particle sizes, 10-20% humus, 10,000 times, erosion statistics): don't memorize them.",
    ],
}

QUICK_GUIDE[26] = {
    "intro": [
        "Plants can't move away from danger or toward food, so they respond to their surroundings mostly by changing "
        "how they grow (26.1.3). Ch 26 has three parts: the hormones that carry signals around the plant (26.1), "
        "growth and movement responses to light, gravity and touch (26.2), and phytochrome, the pigment that lets "
        "plants track day and night length (26.3).",
        "One pattern repeats throughout: a stimulus is detected by a receptor, the signal is passed along and "
        "amplified inside the cell, and the cell responds, often by changing which genes are turned on (26.1.4, "
        "26.1.5).",
    ],
    "sections": {
        1: [
            "Plants respond to stimuli such as light, gravity, carbon dioxide levels, pathogen infection, drought and "
            "touch, and responding helps the species survive. Responses can be short-term, like stomata opening and "
            "closing with light levels, or long-term, like roots growing down and stems growing up in response to "
            "gravity (26.1.3).",
            "Signal transduction (26.1.4, 26.1.5): a receptor, a protein in the plasma membrane, cytoplasm or "
            "nucleus, is activated by a specific signal (for example, blue light); a transduction pathway of relay "
            "proteins or enzymes amplifies the signal and converts it into one the cell's machinery understands; the "
            "cellular response follows, most often a change in gene expression (for example, a stem bending or roots "
            "growing).",
            "Hormones are chemical signals that let plant cells communicate and coordinate their responses. Each is "
            "made in one part of the plant and travels in the phloem or from cell to cell (26.1.6). There are five "
            "main ones (26.1.7).",
            ("Auxin (26.1.8 to 26.1.11)", [
                "Made in the shoot apical meristem; found in young leaves, flowers and fruits (26.1.8).",
                "Apical dominance: auxin from the shoot tip prevents the axillary buds below from growing (26.1.8), "
                "which is why pruning the tip makes a plant bushier (textbook).",
                "Promotes growth of roots and fruit, prevents loss of leaves and fruit, and makes stems bend toward "
                "light (positive phototropism) (26.1.8).",
                "Discovery: auxin from a coleoptile tip (the sheath over a grass seedling's first leaves), collected "
                "in a block of agar and placed on one side of a cut seedling, makes it curve (26.1.9).",
                "How it bends a stem (26.1.10, 26.1.11): with light from one side, auxin moves to the shady side; it "
                "binds receptors, which activates proton pumps; H+ pumped into the cell wall activates enzymes that "
                "break cellulose fibers and loosen the wall; water enters, turgor pressure rises, the cell enlarges "
                "and rebuilds a longer wall. Only the shady-side cells lengthen, so the stem bends toward the light.",
                "Synthetic auxins are used as herbicides (2,4-D; Agent Orange defoliated forests in Vietnam), and "
                "auxin can make fruit form without pollination (26.1.7, 26.1.10).",
            ]),
            ("Gibberellins (26.1.12, 26.1.13)", [
                "Growth-promoting hormones that cause stem elongation; the most common is gibberellic acid (26.1.12).",
                "They break the dormancy of buds and seeds; dormancy is a period when growth is suspended (26.1.12).",
                "Commercial use: inducing growth in crops; treated plants grow taller and treated grapes grow larger "
                "(26.1.12, 26.1.13).",
            ]),
            ("Cytokinins (26.1.14 to 26.1.16)", [
                "Promote cell division and organ formation; found in dividing root tissue, seeds and fruits "
                "(26.1.14).",
                "Responsible for root nodules (which house nitrogen-fixing bacteria) and galls on wounded trees "
                "(26.1.14).",
                "Together with auxin, prevent senescence (aging); in autumn, low cytokinin levels let leaves change "
                "color and die; used to prolong the life of cut flowers and stored vegetables (26.1.14, 26.1.16).",
                "In tissue culture, the ratio of auxin to cytokinin decides what forms: an undifferentiated callus, "
                "roots, leafy shoots or flowers (26.1.15; textbook).",
            ]),
            ("Abscisic acid, ABA (26.1.17 to 26.1.19)", [
                "Produced by any green tissue; called the stress hormone (26.1.17).",
                "Starts and maintains seed and bud dormancy; corn that can't respond to ABA shows vivipary, sprouting "
                "while still on the cob (26.1.17, 26.1.18).",
                "Closes stomata (26.1.17, 26.1.19). How (textbook): ABA binds a receptor on the guard cell, calcium "
                "ions enter as a second messenger, K+ channels open, K+ and then water leave, and the stoma closes.",
                "Commercial use: thinning fruit so the remaining fruit grows larger (26.1.7).",
            ]),
            ("Ethylene (26.1.20 to 26.1.22)", [
                "A gas formed from the amino acid methionine (26.1.20).",
                "Causes abscission, the dropping of leaves, fruit or flowers, by stimulating enzymes such as "
                "cellulase; a ripe apple under a jar makes a holly twig drop its leaves (26.1.20, 26.1.21).",
                "Ripens fruit, by activating enzymes that soften it and produce its flavor and smell; tomatoes "
                "engineered not to make ethylene are harvested green (26.1.20, 26.1.22).",
                "Also inhibits axillary buds and suppresses stem and root elongation (26.1.20).",
            ]),
            "Hormones mainly handle abiotic stimuli (light, oxygen, water, pH, temperature). Against biotic threats "
            "(herbivores, parasites, competing plants), plants rely on their epidermis and bark and on secondary "
            "metabolites, defense chemicals once thought to be waste products. Primary metabolites, such as sugars "
            "and amino acids, are the ones every cell needs to work normally (26.1.23).",
            "Traps: abscisic acid vs abscission (the ABA slide defines abscission, but ethylene causes it; the "
            "textbook says ABA no longer counts as its natural cause); gibberellins (break dormancy) vs ABA (keeps "
            "dormancy); auxin (apical dominance, elongation) vs cytokinins (cell division); primary vs secondary "
            "metabolites (26.1.12, 26.1.17, 26.1.20, 26.1.23).",
        ],
        2: [
            "A tropism is plant growth toward or away from a stimulus that comes from one direction: positive tropism "
            "is growth toward it, negative tropism is growth away (26.2.24). It happens because one side of the organ "
            "grows faster than the other (textbook).",
            ("The three tropisms", [
                "Phototropism (light): stems bend toward light because auxin makes the cells on the shady side "
                "elongate. The receptor pigment phototropin absorbs blue light, becomes phosphorylated and starts the "
                "transduction pathway that moves auxin. Roots are insensitive to light or grow away from it (26.2.25, "
                "26.2.26).",
                "Thigmotropism (touch from another plant, an animal, a rock or wind): stems and tendrils of runner "
                "beans and morning glories coil around a support. Thigmomorphogenesis is a change in the plant's "
                "overall shape due to touch, such as a barrier, wind or rain (26.2.27, 26.2.28); wind-blown plants "
                "grow shorter and sturdier (textbook).",
                "Gravitropism (gravity): a plant laid on its side grows its stem upward and its roots downward. Roots "
                "sense gravity with statoliths, starch grains inside organelles called amyloplasts in root-cap cells, "
                "which settle to the bottom of each cell and signal the downward direction; auxin may then direct the "
                "bending (26.2.29, 26.2.30). A clinostat keeps a plant turning so statoliths can't settle (26.2.30). "
                "The slide's \"stems with root caps grow downward\" should say roots (26.2.29).",
            ]),
            "Arabidopsis thaliana, a small flowering plant related to cabbage and mustard with no commercial value, "
            "is the model organism for plant molecular genetics, including signal transduction: it's small, matures "
            "in 5 to 6 weeks, normally self-pollinates but is easily cross-pollinated, and has relatively few base "
            "pairs of DNA (26.2.31, 26.2.32).",
            "Turgor movements, also called nastic movements, are caused by internal stimuli: they don't involve "
            "growth and don't depend on the direction of the stimulus. They come from electrical impulses, hormone "
            "action or changes in turgor pressure: a cell that fills with water is turgid, and one that loses water "
            "goes limp (26.2.33, 26.2.34).",
            "Examples (26.2.33, 26.2.35): touching Mimosa pudica (the sensitive plant) makes its leaflets collapse "
            "within a second, because cells in the leaf petiole lose turgor pressure; the Venus flytrap snaps shut "
            "when touched; and sleep movements, leaves folding daily with light and dark, follow a circadian rhythm.",
            "Traps: tropism (growth, directional) vs turgor movement (no growth, not directional); positive vs "
            "negative tropism; phototropin (blue light, phototropism) vs phytochrome (red and far-red, photoperiod) "
            "(26.2.24, 26.2.25, 26.2.33, 26.3.37).",
        ],
        3: [
            "Photoperiodism is any physiological response to changes in the length of day or night, such as when to "
            "flower. It requires a biological clock and the photoreceptor phytochrome (26.3.36).",
            "Phytochrome is a blue-green leaf pigment with two forms (26.3.37, 26.3.38, 26.3.39). Pr (phytochrome "
            "red), the inactive form, absorbs red light, which is plentiful in daylight, and turns into Pfr, the "
            "active form. Pfr absorbs far-red light and turns back into Pr in the evening, and whenever light is "
            "limited (shade, night). Switching between the two lets the plant detect photoperiod changes. "
            "Phytochrome also promotes seed germination and flowering and inhibits shoot elongation (26.3.37).",
            "Flowering (26.3.40, 26.3.41, 26.3.42): short-day plants flower when the day is shorter than a critical "
            "length; long-day plants, such as clover, flower when it is longer; day-neutral plants flower regardless "
            "of day length. What really counts is night length: a flash of light in the middle of the long night "
            "stops a short-day plant from flowering but makes a long-day plant flower. So short-day plants are "
            "long-night plants, and long-day plants are short-night plants.",
            "Shade and spacing (26.3.43, 26.3.44): leaf shade increases far-red light relative to red light, and "
            "plants measure the far-red light bounced back by neighboring plants; the more far-red they sense, the "
            "more energy they spend growing taller to outcompete the others for sunlight. Seedlings grown in darkness "
            "are etiolated: the shoot keeps elongating, and the leaves stay small and yellow (26.3.43; textbook).",
            "Circadian rhythms are biological rhythms with a cycle of about 24 hours, such as sleep movements and "
            "flowers opening and closing (26.3.45, 26.3.46). They persist without outside cues because a biological "
            "clock runs them, but a plant kept in dim light shifts its sleep cycle (26.3.45). Entrainment means being "
            "synchronized to light at daybreak (26.3.45).",
            "Traps: Pr (inactive, absorbs red) vs Pfr (active, absorbs far-red); short-day means long-night; a night "
            "flash changes night length, not day length; photoperiodism (seasons) vs circadian rhythm (daily) "
            "(26.3.37, 26.3.41, 26.3.42, 26.3.45). The text alternative printed with 26.3.41 actually describes "
            "Mimosa's leaves (26.2.35).",
        ],
    },
    "look_up": [
        "Each hormone: where it's made, what it does, its commercial use: the hormone table.",
        "Tropisms and turgor movements side by side: the movements table.",
        "Short-day, long-day and day-neutral plants, and what a night flash does: the photoperiod table.",
        "Exact numbers (136 gibberellins, Arabidopsis details): don't memorize them.",
    ],
}

QUICK_GUIDE[27] = {
    "intro": [
        "Ch 27 follows the flowering plant's life cycle in detail: how a flower makes pollen (the male gametophyte) "
        "and the embryo sac (the female gametophyte), pollination and double fertilization (27.1), how the embryo "
        "develops inside the seed (27.2), fruits, seed dispersal and germination (27.3), and reproduction without "
        "seeds (27.4).",
        "It builds on the Ch 23 life cycle. Keep two rules in mind: meiosis makes spores and mitosis makes gametes; "
        "after fertilization, the ovule becomes the seed and the ovary becomes the fruit (27.1.3, 27.1.5).",
    ],
    "sections": {
        1: [
            "Plants have a two-stage, alternating life cycle (27.1.3). The diploid (2n) sporophyte is dominant; it is "
            "the plant you see and the stage that bears flowers. Its flowers make two kinds of haploid spores by "
            "meiosis: microspores (in anthers) and megaspores (in ovules). Each spore divides by mitosis into a "
            "haploid gametophyte, which makes gametes; gametes fuse into a diploid zygote, which grows by mitosis "
            "into a new sporophyte (27.1.3, 27.1.4).",
            "A microspore becomes the male gametophyte, the pollen grain; a megaspore becomes the female gametophyte, "
            "the embryo sac, inside an ovule inside an ovary. The ovule becomes a seed, and the ovary becomes a fruit "
            "(27.1.5). The slide's \"Microspore – Male gametophyte\" means a microspore becomes one; the spore itself "
            "isn't the gametophyte.",
            "The cycle suits life on land (textbook): the tiny gametophytes develop inside the sporophyte, protected "
            "from drying out; pollen has a tough wall; sperm reach the egg through a pollen tube, so no outside water "
            "is needed; and the seed coat protects the embryo until conditions favor germination.",
            "Flowers are unique to angiosperms: they attract pollinators and produce fruits that enclose seeds. "
            "Flowering often responds to signals such as day length: a meristem stops producing leaves and starts "
            "producing flowers. Monocot flower parts come in threes, eudicot parts in fours or fives (27.1.6, "
            "27.1.9).",
            ("Flower structure (27.1.7, 27.1.8)", [
                "Four whorls of modified leaves sit on the receptacle, at the end of the flower stalk (peduncle) "
                "(27.1.7).",
                "Sepals protect the bud; petals attract pollinators (27.1.7).",
                "Stamen (male): the anther, a saclike container where pollen forms, on a slender filament (27.1.7).",
                "Carpel (female): the stigma, an enlarged sticky knob; the style, a slender stalk; and the ovary, the "
                "enlarged base enclosing the ovules, which produce the megaspores (27.1.7).",
            ]),
            ("Flower and plant types (27.1.10, 27.1.11)", [
                "Complete flowers have sepals, petals, stamens and a carpel; incomplete flowers are missing one or "
                "more (27.1.10).",
                "Perfect (bisexual) flowers have both stamens and carpels; imperfect (unisexual) flowers have one "
                "but not the other (27.1.10).",
                "Monoecious plants have staminate (male) and carpellate (female) flowers on the same plant "
                "(Jatropha); dioecious plants have them on separate plants, so only female holly trees bear berries "
                "(27.1.10, 27.1.11).",
            ]),
            "Male gametophyte (27.1.12, 27.1.13): each anther has four pollen sacs full of microspore mother cells. "
            "Each mother cell undergoes meiosis to make four haploid microspores, and each microspore undergoes "
            "mitosis to make a pollen grain. At first it is an immature gametophyte of two cells: a tube cell, which "
            "will produce the pollen tube, and a generative cell, which divides by mitosis into two sperm. Then the "
            "pollen grain is the mature male gametophyte.",
            "Female gametophyte (27.1.13, 27.1.14): an ovule is a central mass of parenchyma cells covered by "
            "integuments. One cell enlarges into a megaspore mother cell, which undergoes meiosis to make four "
            "haploid megaspores, three of them nonfunctional. The functional megaspore divides by mitosis until "
            "there are eight nuclei. The embryo sac then has one egg cell with two synergid cells beside it, a "
            "central cell with two polar nuclei, and three antipodal cells (seven cells, eight nuclei; textbook).",
            "Pollination is the transfer of pollen from an anther to the stigma of a carpel: self-pollination if the "
            "pollen comes from the same plant, cross-pollination if it comes from a different plant of the same "
            "species (27.1.15). Wind-pollinated plants such as grasses release huge amounts of pollen (27.1.16; "
            "textbook).",
            "Fertilization comes after pollination (27.1.17): the pollen grain germinates on the stigma, and its "
            "pollen tube passes between the stigma and style to the ovule's micropyle (a small opening). Double "
            "fertilization follows: one sperm unites with the egg to make the 2n zygote, and the other unites with "
            "the two polar nuclei to make the 3n endosperm nucleus, which develops into the endosperm, the embryo's "
            "food. A mature seed contains the embryo, stored food and the seed coat (27.1.17).",
            "Pollinators (27.1.18, 27.1.19; textbook): bees favor yellow, blue or white flowers (bees can't see red) "
            "with ultraviolet nectar guides; butterflies favor flowers with a landing platform, such as composite "
            "flowers; hummingbirds favor red, slender-tubed flowers curved back, with lots of nectar and little "
            "smell; bats favor large, sturdy, pale flowers that open at night and smell musky. Plants and their "
            "pollinators coevolved, each adapting to the other (textbook).",
            "Traps: pollination (pollen reaches the stigma) vs fertilization (sperm meets egg); microspore vs "
            "megaspore; tube cell vs generative cell; synergids (beside the egg) vs antipodals vs polar nuclei; "
            "complete vs perfect; monoecious vs dioecious; zygote (2n) vs endosperm (3n) (27.1.10, 27.1.12, 27.1.14, "
            "27.1.15, 27.1.17).",
        ],
        2: [
            "Development is a programmed series of stages from a simple to a more complex form, and cells "
            "differentiate (specialize) as it proceeds (27.2.20).",
            ("Stages of a eudicot embryo (27.2.20 to 27.2.24)", [
                "Zygote: right after double fertilization, the zygote and the endosperm appear (27.2.23).",
                "Proembryo: the zygote divides repeatedly into a proembryo and a suspensor, a stalk that anchors the "
                "embryo; the root-shoot axis is already set (27.2.20, 27.2.23).",
                "Globular stage: the proembryo is a ball of cells; its outermost cells will become the dermal "
                "tissue, which protects against drying out and includes stomata (27.2.20, 27.2.24).",
                "Heart stage: the embryo becomes heart-shaped as the cotyledons (seed leaves) appear (27.2.21, "
                "27.2.24).",
                "Torpedo stage: the embryo enlarges and elongates; the shoot apical meristem (for aboveground "
                "growth) and root apical meristem (for underground growth) are present (27.2.21, 27.2.24).",
                "Mature embryo: the epicotyl, above the cotyledons, develops into the shoot; the hypocotyl, below "
                "them, contributes to the stem and ends in the radicle, the embryonic root (27.2.22). The figure's "
                "description calls the hypocotyl the root axis (27.2.24); the slide's wording is the safer one.",
            ]),
            "As the embryo develops, the ovule's integuments become the seed coat, which protects the embryo and its "
            "food (textbook).",
            "Monocot vs eudicot seeds (27.2.25, 27.2.26): a monocot has one cotyledon, which stores some nutrients, "
            "absorbs others from the endosperm and passes them to the embryo, so a corn kernel still has endosperm "
            "when mature. Eudicot cotyledons store all the nutrients the embryo needs, because they have taken up the "
            "endosperm, as in a bean seed (27.2.25). In corn, the coleoptile is a sheath protecting the shoot, and the "
            "coleorhiza a sheath protecting the root (27.2.26; textbook).",
            "Traps: epicotyl (shoot) vs hypocotyl (stem, below the cotyledons) vs radicle (root); suspensor (anchors "
            "the embryo) vs cotyledon (seed leaf); globular, then heart, then torpedo; coleoptile (shoot sheath) vs "
            "coleorhiza (root sheath) (27.2.20, 27.2.21, 27.2.22, 27.2.26).",
        ],
        3: [
            "A fruit is a mature ovary (27.3.27); fruits protect seeds and help disperse them (textbook). Simple "
            "fruits come from a single ovary, with one or several chambers. Compound fruits come from several "
            "ovaries: aggregate fruits from the ovaries of a single flower on one receptacle (blackberry), and "
            "multiple fruits from the ovaries of separate flowers clustered together (pineapple) (27.3.27).",
            "As the fruit develops, the ovary wall thickens into the pericarp, which can have three layers: the "
            "exocarp (the outermost skin), the mesocarp (the flesh) and the endocarp (the boundary around the seeds, "
            "like a peach pit) (27.3.28).",
            "In dry fruits the pericarp is papery, leathery or woody at maturity. Dehiscent fruits split open when "
            "ripe (legumes, such as pea pods); indehiscent fruits don't (grains) (27.3.29).",
            ("Named fruit types (27.3.30; examples from the textbook)", [
                "Drupe: fleshy, with a pit containing a single seed, from a simple ovary (peach) (27.3.30).",
                "Berry: fleshy, with seeds and pulp, from a compound ovary (tomato) (27.3.30).",
                "Legume: dry and dehiscent, from a single ovary (pea) (27.3.30).",
                "Samara: dry and indehiscent, winged, from a simple ovary (maple) (27.3.30).",
            ]),
            "Dispersal (27.3.31, 27.3.32): many dry fruits are carried by wind on woolly hairs, plumes or wings "
            "(dandelion); fleshy fruits feed animals (peaches, cherries, tomatoes), which carry the seeds away; hooks "
            "and spines attach dry fruits to animal fur and clothing (burdock); and dehiscent fruits disperse their "
            "seeds by forced ejection.",
            "Germination is when the embryo resumes growth and metabolic activity (27.3.33). Some seeds first need a "
            "dormant period with no growth: in temperate zones cold weather breaks dormancy, and fleshy fruits "
            "contain inhibitors so seeds don't germinate while still on the plant (27.3.33). A seed needs oxygen (for "
            "metabolism), warmth (for enzyme activity) and water (to hydrate its cells) (27.3.34).",
            "Bean vs corn germination (27.3.35; textbook): in a bean (eudicot) the root emerges first, the shoot is "
            "hook-shaped to protect the young leaves as it pushes up through the soil, and the two cotyledons feed "
            "the seedling until its leaves photosynthesize, then wither. In corn (monocot) the coleoptile covers the "
            "first leaf and the coleorhiza covers the first root as they emerge; later come adventitious and prop "
            "roots.",
            "Traps: simple vs aggregate vs multiple fruit; dehiscent vs indehiscent; exocarp vs mesocarp vs endocarp; "
            "drupe vs berry; dormancy vs germination (27.3.27, 27.3.28, 27.3.29, 27.3.30, 27.3.33).",
        ],
        4: [
            "Asexual reproduction makes clones, offspring genetically identical to their single parent (textbook). "
            "Plants do it with stolons, horizontal stems that run above ground (strawberry), and rhizomes, "
            "underground stems that produce new plants. New plants arise at the nodes of stolons and rhizomes, where "
            "new growth can occur; the \"eyes\" of a white potato are buds that can produce a new plant if planted "
            "with a portion of the tuber (27.4.36, 27.4.37).",
            "Tissue culture is the growth of a plant tissue in an artificial liquid or solid medium. It works because "
            "many plant cells are totipotent: each has the genetic capability of becoming an entire plant (27.4.38).",
            "Steps (27.4.39, 27.4.40): meristem tissue is placed on a medium containing auxin, cytokinins and "
            "nutrients; an undifferentiated mass of cells, the callus, forms first; organogenesis (organ formation) "
            "then starts roots and shoots; finally a plantlet forms. The plantlets are clones with identical traits, "
            "and rare plants such as the ladyslipper orchid are grown this way for conservation (27.4.40, 27.4.41).",
            "Cell suspension culture (27.4.40): rapidly growing calluses are cut into small pieces and shaken into a "
            "liquid nutrient medium, where single cells or small clumps form a suspension. Chemicals can be extracted "
            "from these cells, such as heart-disease drugs from Digitalis, which avoids overcollecting wild plants.",
            "Traps: stolon (above ground) vs rhizome (underground) vs tuber (swollen storage part); callus "
            "(undifferentiated) vs plantlet; tissue culture (whole plants) vs cell suspension culture (chemicals) "
            "(27.4.36, 27.4.40).",
        ],
    },
    "look_up": [
        "Male vs female gametophyte, step by step: the gametophyte table.",
        "Flower parts and flower terms: the flower tables.",
        "Embryo stages, seed parts, fruit types and dispersal: the seed and fruit tables.",
        "Pollinators and their flowers: the pollinator table.",
        "Exact numbers (species counts, seed sizes): don't memorize them.",
    ],
}
