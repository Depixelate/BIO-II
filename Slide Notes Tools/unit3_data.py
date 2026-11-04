"""Printed-notes data for Unit 3 (Ch 28-30): the same fields as print_notes_data.py, which merges this file in.

Sources: the three decks (Mader Biology 14e, Ch 28-30) and the textbook (Mader, Biology, 2024 Release; book pages
504-574, PDF page = book page + 19). Every correction and caption cites the textbook page or figure it comes from.
"""

CHAPTERS = [28, 29, 30]
CHAPTER_NAMES = {28: "Invertebrate Evolution", 29: "Vertebrate Evolution", 30: "Human Evolution"}
# body font of the Unit 3 chapter and unit files: the largest size that fits the sheet budget with a page to spare
# (build_print_docx.py --unit 3 --fit)
FONT_SIZE = 13


def s28(*ns):
    return [(28, n) for n in ns]


def s29(*ns):
    return [(29, n) for n in ns]


def s30(*ns):
    return [(30, n) for n in ns]


# ---------------------------------------------------------------- slides and figures
TEXT_ALT_MATCH = {}
TA_SKIP = {28: {74}, 29: {48}, 30: {56}}   # the "Accessibility Content" cover slides
CYCLES, FRAMES, FRAME_EXTRA = {}, {}, {}
# figure sentences deliberately not printed: (chapter, slide) -> {start of the sentence: reason}
FIG_SKIP = {
    (28, 12): {"The data for": "filler (“the data ... are as follows”)"},
    (30, 13): {"The data ranges": "filler, reworded as the line's heading"},
    (30, 6): {"The details of hands": "filler (“the details ... are as follows”)"},
}
# the short alt text says something the full text alternative doesn't
PRINT_BOTH = {
    (28, 6),    # the infolding that makes two tissue layers
    (28, 71),   # the sea apple is a sea cucumber
    (29, 4),    # names the four chordate characteristics
    (29, 7),    # names the sea squirt's siphons, gill slit and tunic
}
FIG_SPLIT = {
    (28, 30): ["b. Land snail"],
    (28, 32): ["b. Bigfin reef squid"],
    (28, 66): ["Head: It consists"],
    (29, 36): ["c) Prairie rattlesnake"],
    (30, 13): ["70 to 60:"],
    (30, 19): ["During the evolution of hominins"],
    (30, 21): ["The data (in millions", "Sahelanthropus tchadensis:", "Ardipithecus ramidus:", "Paranthropus robustus:",
               "Paranthropus boisei:", "Australopithecus afarensis:", "Australopithecus africanus:",
               "Australopithecus sediba:", "Homo habilis:", "Homo erectus:", "Homo heidelbergensis:",
               "Homo neanderthalensis:", "Homo sapiens:"],
    (30, 42): ["Migration of Homo erectus:", "Migration of early Homo species:", "Migration of modern humans:",
               "Note: All data"],
}

CAPTIONS = {
    (28, 19): "a. The sea anemone, sometimes called the flower of the sea, is a solitary polyp. b. Corals are colonial "
              "polyps residing in a calcium carbonate or proteinaceous skeleton. c. The Portuguese man-of-war is a "
              "colony of modified polyps and medusae. d. Jellyfish, Aurelia.",
    (28, 23): "a. The lophophore feeding apparatus. b. A trochophore larva.",
    (28, 30): "Gastropods have the three parts of a mollusk, and the foot is muscular, elongated, and flattened.",
    (28, 32): "Cephalopods have tentacles and/or arms in place of a head. Speed suits their predatory lifestyle, and "
              "only the chambered nautilus has a shell.",
    (28, 39): "Clam worms are predaceous polychaetes that undergo cephalization; their parapodia are used for "
              "swimming and as respiratory organs. Medical leeches are blood suckers.",
    (28, 53): "a. Ascaris, a common cause of a roundworm infection in humans. b. Encysted Trichinella larva in muscle. "
              "c. A filarial worm infection causes elephantiasis, a swollen body part when the worms block lymphatic "
              "vessels.",
    (28, 62): "a. A centipede has a pair of appendages on almost every segment. b. A millipede has two pairs of legs "
              "on most segments.",
    (29, 14): "Lampreys are agnathans (jawless fishes), with an elongated, rounded body and nonscaly skin; the "
              "toothed oral disk attaches to the glass.",
    (29, 23): "A coelacanth is a lobe-finned fish once thought to be extinct.",
    (29, 30): "a. Snake venom may be used to create pain medications. b. Mammals, such as these goats, may express "
              "pharmaceutical compounds in their milk. c. Pigs are now being genetically altered to provide a supply "
              "of hearts for heart transplant operations.",
    (29, 36): "e. The crocodile's eggshell is leathery and flexible, not brittle like birds' eggs. f. Inside the "
              "amniotic egg, the embryo is surrounded by three membranes: the chorion aids in gas exchange, the "
              "allantois stores waste, and the amnion encloses a fluid that prevents drying out and provides "
              "protection. The yolk sac provides nutrients for the embryo.",
    (29, 40): "a. A bald eagle's beak allows it to tear apart prey. b. A woodpecker's beak is used to chisel in wood. "
              "c. A parrot's (macaw's) beak is modified to pry open nuts. d. A cardinal's beak allows it to crack "
              "tough seeds.",
    (29, 45): "The duckbill platypus is a monotreme that inhabits Australian streams. The koala is an Australian "
              "marsupial that lives in trees. The opossum is the only marsupial in North America.",
    (30, 4): "Today's prosimians (tarsier) may resemble the earliest groups of primates. Modern monkeys are divided "
             "into the New World monkeys (white-faced monkey) and the Old World monkeys (baboon). The apes can be "
             "divided into the Asian apes (orangutans and gibbons) and the African apes (chimpanzees and gorillas). "
             "Humans (hominins) are also primates.",
    (30, 8): "In primates, the snout is reduced, and the eyes are at the front of the head. The result is a "
             "binocular field that aids depth perception and provides stereoscopic vision.",
    (30, 28): "a. A reconstruction of Lucy. b. Fossilized footprints in ash from a volcanic eruption some 3.7 million "
              "years ago (Tanzania): the larger footprints are double, and a third, smaller individual was walking "
              "to the side. The footprints suggest that A. afarensis walked bipedally.",
    (30, 34): "The dates show the migration of early Homo erectus out of Africa.",
    (30, 36): "This skeleton of a 10-year-old boy, who lived 1.6 million years ago in eastern Africa, shows femurs "
              "that are angled and elongated.",
    (30, 52): "a. Some of the differences among ethnic groups may be due to adaptations to their original "
              "environments. b. The Maasai live in East Africa and tend to be slightly built with elongated limbs. "
              "c. The Inuit live near the Arctic Circle and tend to have a bulkier build with shorter limbs "
              "(textbook p. 569: Bergmann's and Allen's rules, 30.4.53).",
}
PROCESS = {
    (30, 13): "Primates descend from a mammalian ancestor that entered the trees and may have resembled a tree shrew. "
              "Order in which the groups split off (oldest first): lemurs, tarsiers (prosimians); New World monkeys; "
              "Old World monkeys; gibbons; orangutans; gorillas; then chimpanzees and humans, the last to split. "
              "Anthropoids = New World monkeys through humans; hominids = orangutans, gorillas, chimpanzees and "
              "humans (textbook Fig. 30.4).",
}

# slide errors, printed on the slide as "Textbook: ..."
CORRECTIONS = {
    # ------------------------------------------------------------ Ch 28
    (28, 4): "Panel d's “haploid cells” is wrong: most animals reproduce sexually, beginning life as a diploid (2n) "
             "zygote that develops into a multicellular animal with specialized tissues (textbook Fig. 28.1d).",
    (28, 8): "Radial symmetry: any lengthwise cut through the central point gives two identical halves (like a "
             "wheel). Bilateral symmetry: only one cut, down the midline, gives two equal halves (p. 510; 28.1.10).",
    (28, 11): "Spiral cleavage occurs in most protostomes, but not in ecdysozoans (roundworms, arthropods; p. 512, "
              "524). The opening is the blastopore, made when the blastula indents: the mouth (protostomes) or the "
              "anus (deuterostomes) appears at or near it.",
    (28, 15): "They may be the oldest animal lineage (not the first organisms): their DNA sequences seem more "
              "ancient than sponges', but their placement is still debated, because that DNA evidence is uncertain "
              "and their physiology is more advanced than sponges' (p. 514).",
    (28, 16): "The inner layer is a tissue (from endoderm) that secretes digestive juices into the gastrovascular "
              "cavity; the outer epidermis comes from ectoderm, and mesoglea separates the two layers (p. 514).",
    (28, 22): "The slide misprints the two groups as “Lophophorus” and “Protozoans” (fixed above); protozoans are "
              "protists, not animals. Trochozoans (mollusks, annelids) have a trochophore larva; flatworms and "
              "rotifers are also counted as trochozoans because they descend from an ancestor with one. The "
              "textbook calls this section “Diversity of the Lophotrochozoans”; Spiralia was an older grouping, and "
              "lophotrochozoans are bilaterally symmetrical in at least one stage of development (p. 516).",
    (28, 24): "Over 150,000 named species: mollusks are the second most numerous group of animals (p. 516).",
    (28, 44): "Schistosoma has separate sexes: female flukes lay the eggs, and adult males and females copulate in "
              "the blood vessels (p. 522, Fig. 28.27). Flukes have an oral sucker and at least one more; tapeworms "
              "are the hermaphrodites (p. 523).",
    (28, 50): "Many (not all) ecdysozoans have separate sexes that copulate (p. 525).",
    (28, 56): "The five pairs of appendages are on the head: antennae and antennules (sensory, in front of the mouth) "
              "and mandibles and first and second maxillae (mouthparts, behind it). The thorax and abdomen carry "
              "more, biramous appendages: one branch a gill, the other a leg (p. 527).",
    (28, 67): "The textbook gives about 1,500 scorpion species in North America (p. 531).",
    (28, 72): "Spines from endoskeletal plates (not exoskeletal): echinoderms have an endoskeleton of spiny, "
              "calcium-rich plates called ossicles (p. 532).",
    # ------------------------------------------------------------ Ch 29
    (29, 3): "The nerve cord is protected by vertebrae in vertebrates only; lancelets and sea squirts have none "
             "(p. 537).",
    (29, 12): "Jawed fishes and all the other vertebrates (not invertebrates) are gnathostomes; jawed fishes "
              "dominated the seas by the Silurian period (p. 540).",
    (29, 13): "Nearly 33,000 species of fishes (p. 540).",
    (29, 16): "The jaws evolved from the first pair of gill arches (as 29.3.15 says); the second pair became the "
              "jaws' supports (p. 540–541).",
    (29, 20): "Over 32,000 species: bony fishes are the majority of living vertebrates (p. 542).",
    (29, 28): "Caecilians are often (not always) sightless (p. 544).",
    (29, 44): "The placenta exchanges substances between the mother's blood and the fetus's blood (nutrients to the "
              "fetus, wastes to the mother); the two bloods themselves don't exchange (p. 553).",
    # ------------------------------------------------------------ Ch 30
    (30, 11): "Gorillas and orangutans are hominids, not hominins. Hominins = humans and their closest extinct "
              "relatives; hominids = chimpanzees, gorillas, orangutans and humans (p. 558, 570).",
    (30, 27): "About 100–115 cm tall (p. 563).",
    (30, 29): "The robust southern species is Paranthropus robustus (robust types are genus Paranthropus, 30.2.27). "
              "“Small brain (500 cc), long arms, climbed trees; humanlike pelvis, nose and dentition” describes "
              "A. sediba, the 2-million-year-old species found in 2008 (p. 564).",
    (30, 38): "The slide runs two species together. Homo floresiensis is the dwarf island species that split from H. "
              "erectus in Asia. The rest of the list is Homo heidelbergensis: it replaced H. erectus in Africa about "
              "500,000 years ago, is the most likely lineage that led to modern humans, and had a larger brain, more "
              "advanced tools and social behavior, and the first shelters (p. 566).",
}
# scanning errors in a slide's text: (chapter, slide) -> [(wrong, right)]
TYPO_FIX = {
    (28, 20): [("tubular poly body", "tubular polyp body")],
    (28, 22): [("Lophophorus (", "Lophophorans ("), ("Protozoans (", "Trochozoans (")],
    (28, 33): [("are segmented partitions (septa); divide the",
                "are segmented worms: partitions (septa) divide the")],
    (29, 18): [("Galeocerdovi cuer", "Galeocerdo cuvier")],
    (30, 16): [("Africa Arabia joined", "Africarabia (Africa plus the Arabian Peninsula) joined")],
    (30, 39): [("lineage evolved in “Denisovans”", "lineage evolved into “Denisovans”")],
    (30, 43): [("H. florensiensis", "H. floresiensis")],
    (30, 47): [("Used and could control probably helped", "Used and could control fire, which probably helped")],
}
SLIDE_TEXT = {}
FIG_FIX = {
    (28, 6): [("Earliest animals (sponges):", ""),   # each panel's heading, folded into its evidence line
              ("Evidence: Sponges contain choanocyte",
               "Traditional view (colonial flagellate hypothesis), ending in the earliest animals (sponges). "
               "Evidence: Sponges contain choanocyte"),
              ("The data leads to each other as follows:", "Steps:"),
              ("Evidence: Sponges contain archaeocyte",
               "Alternative hypothesis, ending in the earliest animals (sponges). Evidence: Sponges contain "
               "archaeocyte"),
              ("The details leads to each other as follows:", "Steps:")],
    (28, 12): [("The data for cleavage in protostomes and deuterostomes are as follows:", ""),
               ("The data for fate of blastopore in protostomes and deuterostomes are as follows:", ""),
               ("The data for fate of coelom formation in protostomes and deuterostomes are as follows:", "")],
    (28, 41): [("The head has an two eyespots", "The head has two eyespots")],
    (29, 11): [("A lateral rip is developed", "A lateral rib is developed")],
    (29, 36): [("(a)Green sea turtle", "a) Green sea turtle")],
    (30, 6): [("The details of hands are as follows:", ""), ("short thumb and nails; and", "short thumb and nails.")],
    (30, 36): [("parts of a 10-year old skeleton of Homo erectus boy", "parts of the skeleton of a 10-year-old Homo "
                                                                    "erectus boy")],
    (28, 14): [("inner surface of osculum, central cavity and pores through which water oozes out.",
                "central cavity and osculum: water enters through the pores and leaves through the osculum.")],
    (28, 23): [("trophophore", "trochophore")],
    (28, 49): [("germovitellariumon", "germovitellarium on")],
    (28, 55): [("connected at the edges of joins extending into thicker extensor muscle",
                "and a thicker extensor muscle across the joint"),
               ("epicuticle (first layer of skin), exocuticle (second layer of skin), endocuticle (second layer of "
                "skin)", "epicuticle (outer waxy layer), exocuticle (middle layer, hardened by calcium carbonate), "
                "endocuticle (inner layer)")],
    (28, 57): [("and four walking legs.", "and walking legs (decapods: five pairs).")],
    (28, 59): [("cray fish", "crayfish")],
    (28, 60): [("The digestive system of male cray fish consists of green irregularly ovular gland",
                "Internal anatomy of the male crayfish: green gland (excretory)")],
    (28, 66): [("Thorax: It consists of cylindrical tympanum in the center.",
                "Thorax: three pairs of legs and two pairs of wings (forewings and hindwings)."),
               ("Abdomen: It consists of a pair of forewings and hindwings with ovipositor projection",
                "Abdomen: tympanum (on the first abdominal segment), ovipositor projection"),
               ("The digestive system of female grasshopper consists of",
                "Internal anatomy of the female grasshopper:")],
    (28, 68): [("a pair of four walking legs", "four pairs of walking legs")],
    (29, 18): [("Galeocaredo cuvier", "Galeocerdo cuvier")],
    (29, 25): [("passing through other capillaries.c. The four-chambered heart of some reptiles (birds and mammals)",
                "passing through other capillaries. c. The four-chambered heart of some reptiles (crocodilians and "
                "birds) and mammals")],
    (30, 13): [("(anthropods)", "(anthropoids)"),
               ("The data ranges from 70 (million years ago) to present is as follows:",
                "Groups still on the main line in each time span (million years ago):")],
    (30, 21): [("Australopithecus sediba: 1.9 to 2.0", "Australopithecus sediba: about 2.0"),
               ("Homo neanderthalensis: 0.15 to 0.35", "Homo neanderthalensis: 0.35 to 0.03"),
               ("Homo sapiens: 0 to 2.", "Homo sapiens: about 0.2 to 0 (the present).")],
    (30, 52): [("an Eskimo in the Arctic", "an Inuit person near the Arctic Circle"),
               ("a Masai tribesman", "a Maasai man")],
}
# garbled descriptions replaced by the textbook figure's (each is on the slide-errors list)
FIG_TEXT = {
    (29, 8): "The tree starts from an ancestral chordate; each branch point adds a new characteristic. Notochord: "
             "chordates, which split into lancelets and tunicates (sea squirts) on one side and the vertebrates on "
             "the other. Vertebrae: vertebrates; jawless fishes branch off first. Jaws: gnathostomes; cartilaginous "
             "fishes branch off. Bony skeleton: ray-finned fishes branch off. Lungs: lobe-finned fishes branch off. "
             "4 limbs: tetrapods; amphibians branch off. Amniotic egg: amniotes, which split into reptiles "
             "(including birds) and mammals (mammary glands) (textbook Fig. 29.4).",
    (29, 34): "The ancestral amniote (extinct) lived in the Carboniferous period (from 359 million years ago) and "
              "split into three lineages, told apart by the openings behind the eye socket (orbit). Synapsid skull "
              "(one opening): pelycosaurs and then therapsids (both extinct), leading to the mammals. Anapsid skull "
              "(no opening): the turtles. Diapsid skull (two openings): the lizards, snakes and tuataras, and the "
              "thecodonts (extinct), which led to the archosaurs: crocodilians, dinosaurs (extinct) and birds. The "
              "time axis runs through the Permian, Triassic, Jurassic and Cretaceous periods (Mesozoic era) to the "
              "present. This is the classical view; a modern view puts the turtles among the archosaurs (textbook "
              "Fig. 29.16).",
    (29, 43): "The ancestral amniote (extinct) led, through the pelycosaurs, to a therapsid ancestor (extinct) "
              "around the Permian-Triassic boundary (about 251 million years ago); the line to the other amniotes "
              "branches off. Hair and mammary glands mark the mammals. The monotremes (egg-laying) branch off "
              "first, the oldest group. Live birth and a true uterus mark the marsupials and placentals, which "
              "evolved in the early Cretaceous. The placenta of placentals is more complex and specialized than "
              "the marsupials' (textbook Fig. 29.20).",
}

# ---------------------------------------------------------------- lookup pages
# ======================================================================== Ch 28
TABLES = [
    {"ch": 28, "title": "Animal groups at a glance", "head": ["Group", "Body plan", "Key features (examples)"],
     "rows": [
         (["Sponges (Porifera)", "asymmetrical; no true tissues (cellular level); pores, no mouth",
           "sessile filter feeders; collar cells (choanocytes) beat flagella; water in through pores, out the "
           "osculum; spicules; oldest lineage (Parazoa)"], s28(13, 14)),
         (["Comb jellies (Ctenophora)", "radial; 2 germ layers; body of mesoglea",
           "rows of cilia (largest animals moved by cilia); colloblasts catch prey; some bioluminescent"], s28(15)),
         (["Cnidarians", "radial; 2 layers (epidermis + inner layer) around a gastrovascular cavity; one opening",
           "cnidocytes with nematocysts; polyp (mouth up) and medusa (mouth down); nerve net (hydra, sea anemones, "
           "corals, jellyfish)"], s28(16, 18, 20)),
         (["Lophophorans", "bilateral; 3 germ layers; protostome",
           "lophophore: a crown of ciliated tentacles around the mouth (bryozoans, brachiopods, phoronids)"],
          s28(22, 23)),
         (["Mollusks", "bilateral; reduced coelom (around the heart); open circulation",
           "visceral mass, mantle, foot; radula (not in bivalves); trochophore larva (clams, snails, squids)"],
          s28(24, 25, 26)),
         (["Annelids", "bilateral; segmented; large coelom divided by septa (hydrostatic skeleton); closed "
                       "circulation", "setae; ventral solid nerve cord; nephridia (earthworms, polychaetes, "
                                    "leeches)"], s28(33, 35)),
         (["Flatworms", "bilateral; no body cavity; one opening (sac body plan)",
           "no circulatory or respiratory organs; flame cells (planarians, flukes, tapeworms)"], s28(40, 41)),
         (["Rotifers", "bilateral; microscopic", "corona: a crown of cilia like a spinning wheel; mostly freshwater"],
          s28(48)),
         (["Roundworms (Nematoda)", "nonsegmented; pseudocoelom; cuticle, molts",
           "many parasites (Ascaris, Trichinella, filarial worms); C. elegans"], s28(51, 52)),
         (["Arthropods", "segmented (head, thorax, abdomen); jointed chitin exoskeleton, molts",
           "brain + ventral nerve cord; gills, book lungs or tracheae; metamorphosis (crustaceans, insects, "
           "chelicerates)"], s28(54)),
         (["Echinoderms", "radial (5 parts) as adults, bilateral larvae; deuterostome",
           "endoskeleton of calcium plates with spines; water vascular system with tube feet (sea stars, sea "
           "urchins)"], s28(69)),
     ], "wide": True},
    {"ch": 28, "title": "Protostomes vs deuterostomes", "head": ["", "Protostomes", "Deuterostomes"],
     "rows": [
         (["Cleavage", "spiral (most; not ecdysozoans), determinate", "radial, indeterminate"], s28(11, 12)),
         (["Blastopore", "becomes the mouth", "becomes the anus; the mouth forms second"], s28(9, 11, 12)),
         (["Coelom forms by", "splitting of the mesoderm", "outpocketing of the primitive gut"], s28(11, 12)),
         (["Groups", "lophotrochozoans (mollusks, annelids, flatworms...) and ecdysozoans (roundworms, arthropods)",
           "echinoderms and chordates"], s28(22, 50, 69)),
     ]},
    {"ch": 28, "title": "Cnidarians", "head": ["Example", "Form and features"],
     "rows": [
         (["Sea anemones", "sessile polyps on a substrate; upward oral disk with mouth and tentacles"], s28(18)),
         (["Corals", "like sea anemones in calcium carbonate; colonies build reefs (Great Barrier Reef)"], s28(18)),
         (["Portuguese man-of-war", "a colony of modified polyps and medusae (textbook caption)"], s28(19)),
         (["Hydra", "freshwater polyp, about 1/4 inch; nerve net; reproduces sexually and asexually (buds)"],
          s28(20, 21)),
         (["True jellyfish", "the medusa is the main stage; the polyp stays small"], s28(20)),
     ]},
    {"ch": 28, "title": "Mollusk classes", "head": ["Class", "Features (examples)"],
     "rows": [
         (["Bivalves", "two hinged shells; no head, no radula; ciliated gills filter food; freshwater clams: "
                       "separate sexes, internal fertilization (clams, oysters, mussels, scallops)"], s28(27, 28)),
         (["Gastropods", "largest class; elongated flat foot; most have a one-piece coiled shell; head with "
                         "eyes on tentacles (snails, slugs, conchs, nudibranchs)"], s28(29, 30)),
         (["Cephalopods", "“head-footed”; jet propulsion from the mantle cavity; arms with suckers; beak; good "
                          "senses; octopuses learn (squids, octopuses, nautilus)"], s28(31, 32)),
     ]},
    {"ch": 28, "title": "Annelids", "head": ["Group", "Features"],
     "rows": [
         (["Earthworms (oligochaetes)", "few setae, in pairs; crop, gizzard, intestine with typhlosole; "
                                        "hermaphrodites; clitellum; no larva"], s28(34, 36)),
         (["Polychaetes", "most annelids; marine; setae in bundles on parapodia; clam worms (Nereis) are "
                          "predators; sex organs only in breeding season"], s28(38)),
         (["Leeches", "freshwater; no setae; two suckers; hirudin in saliva stops clotting"], s28(38)),
     ]},
    {"ch": 28, "title": "Parasites", "head": ["Parasite (group)", "Hosts and disease"],
     "rows": [
         (["Schistosoma (blood fluke)", "human (primary: adults in gut blood vessels) and snail (secondary); "
                                        "larvae enter through the skin"], s28(44, 45)),
         (["Clonorchis sinensis (liver fluke)", "a fluke; textbook: cats, dogs, pigs, humans; snail and fish as "
                                                "secondary hosts; raw fish"], s28(44)),
         (["Taenia solium (pork tapeworm)", "human (primary) and pig (secondary: bladder worms in muscle); "
                                            "undercooked pork"], s28(46, 47)),
         (["Ascaris (roundworm)", "intestinal; over 200,000 eggs a day"], s28(52)),
         (["Trichinella (roundworm)", "trichinosis, from rare pork with encysted larvae"], s28(52, 53)),
         (["Filarial worms (roundworms)", "heartworm, fatal in dogs; Wuchereria: elephantiasis, spread by "
                                          "mosquitoes"], s28(52)),
     ]},
    {"ch": 28, "title": "Arthropod groups", "head": ["Group", "Features (examples)"],
     "rows": [
         (["Crustaceans", "crusty exoskeleton (calcium carbonate + chitin); compound eyes; 5 pairs of head "
                          "appendages; mostly aquatic (decapods: crabs, crayfish, lobsters, shrimp; copepods, krill; "
                          "barnacles)"], s28(56, 57)),
         (["Crayfish", "cephalothorax under a carapace; 5 pairs of walking legs; swimmerets; gills; open "
                       "circulation; green glands excrete"], s28(58, 59)),
         (["Centipedes / millipedes", "one pair of legs per segment, venomous jaws / two pairs on abdominal "
                                      "segments, cylindrical"], s28(61)),
         (["Insects", "head, thorax (3 pairs of legs, 0–2 pairs of wings), abdomen; tracheae; metamorphosis"],
          s28(63)),
         (["Grasshopper", "jumping 3rd legs; tympanum; Malpighian tubules; spiracles → tracheae; incomplete "
                          "metamorphosis"], s28(64)),
         (["Chelicerates", "chelicerae (feeding, defense) and pedipalps; all appendages on the cephalothorax "
                           "(spiders, scorpions, ticks, mites, horseshoe crabs)"], s28(67, 68)),
     ]},
    {"ch": 28, "title": "Look-alikes", "head": ["These", "The difference"],
     "rows": [
         (["radial vs bilateral symmetry", "identical halves from many cuts through the center vs one left-right "
                                           "cut"], s28(8, 10)),
         (["diploblastic vs triploblastic", "2 germ layers vs 3"], s28(9)),
         (["protostomes vs deuterostomes", "first opening becomes the mouth vs the anus"], s28(9, 11)),
         (["spiral vs radial cleavage", "protostomes vs deuterostomes"], s28(11)),
         (["coelom vs pseudocoelom", "fully lined by mesoderm vs incompletely lined"], s28(11, 51)),
         (["polyp vs medusa", "mouth up, attached vs mouth down, bell-shaped swimmer"], s28(16)),
         (["cnidocyte vs nematocyst", "the stinging cell vs its fluid-filled capsule"], s28(16)),
         (["comb jellies vs cnidarians", "cilia rows, colloblasts vs cnidocytes"], s28(15, 16)),
         (["lophophore vs trochophore", "feeding tentacle crown vs ciliated larva"], s28(22, 23)),
         (["mantle vs visceral mass vs foot", "may secrete the shell vs holds the organs vs moves, attaches, "
                                              "captures"], s28(24)),
         (["bivalves vs gastropods vs cephalopods", "two shells vs coiled shell, flat foot vs head-footed"],
          s28(27, 29, 31)),
         (["oligochaetes vs polychaetes", "few setae vs many"], s28(33)),
         (["flukes vs tapeworms", "trematodes vs cestodes"], s28(44)),
         (["primary vs secondary host", "has the adult vs the larvae"], s28(46, 47)),
         (["scolex vs proglottids", "attachment head vs egg-filled units"], s28(46)),
         (["chelicerae vs pedipalps", "first pair vs second pair"], s28(67)),
         (["complete vs incomplete metamorphosis", "body reorganized vs gradual change"], s28(63, 64)),
         (["spiracles vs tracheae", "openings vs air tubes"], s28(64)),
         (["Malpighian tubules vs green glands", "insect vs crayfish excretion"], s28(58, 64)),
     ]},
]

SEQUENCES = [
    {"ch": 28, "title": "Colonial flagellate hypothesis", "slides": s28(5, 6),
     "note": "choanoflagellate-like ancestral cell → aggregation into a hollow sphere → some cells specialize → "
             "infolding gives two tissue layers → earliest animals (sponges)"},
    {"ch": 28, "title": "Water through a sponge", "slides": s28(13, 14),
     "note": "flagella of the collar cells beat → water in through the pores → central cavity → out through the "
             "osculum; collar cells trap food particles"},
    {"ch": 28, "title": "Earthworm digestive tract", "slides": s28(34, 37),
     "note": "mouth → muscular pharynx → crop (storage) → gizzard (grinding) → long intestine with typhlosole "
             "(digestion, absorption) → anus"},
    {"ch": 28, "title": "Blood fluke (Schistosoma)", "slides": s28(45),
     "note": "larvae penetrate human skin, mature in the liver → adults copulate in gut blood vessels → eggs "
             "passed in feces → miracidia hatch in water, enter a snail → sporocysts → cercariae leave the snail → "
             "back to human skin"},
    {"ch": 28, "title": "Pork tapeworm (Taenia)", "slides": s28(47),
     "note": "human eats meat with bladder worms → tapeworm matures in the intestine → proglottids fill with eggs → "
             "eggs leave in feces → pig eats them → larvae encyst in muscle as bladder worms → undercooked meat"},
    {"ch": 28, "title": "Sea star movement", "slides": s28(72),
     "note": "water in through the sieve plate → canals → ampulla contracts → water into the tube foot → foot "
             "expands and grips; alternating tube feet → slow movement"},
]

PLOIDY = []

USES = [
    {"ch": 28, "title": "", "slides": s28(38, 51, 63), "head": ["Animal", "Use (and why)"],
     "rows": [
         (["Leeches", "hirudin in their saliva keeps blood flowing (an anticoagulant)"], s28(38)),
         (["Caenorhabditis elegans", "model animal in genetics and developmental biology"], s28(51)),
         (["Insects", "food for other animals and carnivorous plants"], s28(63)),
     ]},
]

CLUES = [
    ("Animal origins and body plans", [
        ("closest living relatives of animals (single cells with a collar)", "choanoflagellates", s28(5)),
        ("animals evolved from a hollow colony of flagellated cells", "colonial flagellate hypothesis", s28(5)),
        ("genes that may explain the body plans present by the Cambrian", "Hox (homeotic) genes", s28(7)),
        ("brain and sense organs at the front end", "cephalization", s28(8)),
        ("first tissue layers in the embryo", "germ layers", s28(9)),
        ("two germ layers / three germ layers", "diploblastic / triploblastic", s28(9)),
        ("cell division without growth", "cleavage", s28(11)),
        ("first embryonic opening becomes the mouth", "protostomes", s28(9, 11)),
        ("first opening becomes the anus", "deuterostomes", s28(9, 11)),
        ("coelom forms by an outpocketing of the gut", "deuterostomes", s28(11)),
    ]),
    ("Sponges, comb jellies, cnidarians", [
        ("no true tissues; pores; sessile filter feeder", "sponge", s28(13)),
        ("sponge cells whose flagella move the water", "collar cells (choanocytes)", s28(14)),
        ("sponge's upper opening, where water leaves", "osculum", s28(13)),
        ("transparent, bioluminescent, moved by rows of cilia", "comb jellies (ctenophores)", s28(15)),
        ("sticky cells that catch a comb jelly's prey", "colloblasts", s28(15)),
        ("stinging cell / its capsule", "cnidocyte / nematocyst", s28(16)),
        ("jellylike substance between the two layers", "mesoglea", s28(15, 21)),
        ("cnidarian form with mouth up / mouth down", "polyp / medusa", s28(16)),
        ("interconnected nerve cells of a hydra", "nerve net", s28(20)),
    ]),
    ("Lophotrochozoans", [
        ("crown of ciliated tentacles around the mouth", "lophophore", s28(22, 23)),
        ("free-swimming larva with bands of cilia", "trochophore", s28(23)),
        ("mollusk part that may secrete the shell", "mantle", s28(24)),
        ("tonguelike organ with rows of teeth", "radula", s28(25)),
        ("cavity that the open circulation pumps hemolymph into", "hemocoel", s28(26)),
        ("two hinged shells, no head, filter feeder", "bivalve", s28(27)),
        ("largest mollusk class; coiled shell, flat foot", "gastropods", s28(29)),
        ("head-footed; jet propulsion; beak", "cephalopods", s28(31)),
        ("bristles that help annelids move", "setae", s28(33)),
        ("fold in the earthworm intestine that adds surface", "typhlosole", s28(34)),
        ("fused midbody segment that secretes mucus", "clitellum", s28(36)),
        ("paddlelike appendages with bundles of setae", "parapodia", s28(38)),
        ("anticoagulant in leech saliva", "hirudin", s28(38)),
        ("ciliated cells of the flatworm excretory system", "flame cells", s28(41)),
        ("planarian's ladder nervous system brain", "paired ganglia", s28(42)),
        ("tapeworm head / reproductive units", "scolex / proglottids", s28(46)),
        ("crown of cilia like a turning wheel", "corona (rotifer)", s28(48)),
    ]),
    ("Ecdysozoans and echinoderms", [
        ("outer covering that is shed by molting", "cuticle", s28(50)),
        ("body cavity incompletely lined by mesoderm", "pseudocoelom", s28(51)),
        ("roundworm used as a model animal", "Caenorhabditis elegans", s28(51)),
        ("limbs swell to a monstrous size; spread by mosquitoes", "Wuchereria (elephantiasis)", s28(52)),
        ("exoskeleton polysaccharide", "chitin", s28(54)),
        ("air tubes of land arthropods / spider lungs", "tracheae / book lungs", s28(54)),
        ("larva and adult with different food and form", "metamorphosis", s28(54)),
        ("fused head and thorax under a carapace", "cephalothorax", s28(58)),
        ("crayfish excretory organs", "green glands", s28(58)),
        ("“hundred legs”, venomous first trunk appendages", "centipede", s28(61)),
        ("two pairs of legs on abdominal segments", "millipede", s28(61)),
        ("grasshopper's sound receiver", "tympanum", s28(64)),
        ("insect excretory tubules", "Malpighian tubules", s28(64)),
        ("openings in the insect exoskeleton", "spiracles", s28(64)),
        ("first pair of chelicerate appendages / second pair", "chelicerae / pedipalps", s28(67)),
        ("canals and tube feet for moving and feeding", "water vascular system", s28(69)),
        ("where water enters a sea star", "sieve plate (madreporite)", s28(72)),
        ("contracts to push water into a tube foot", "ampulla", s28(72)),
    ]),
]

# ======================================================================== Ch 29
TABLES += [
    {"ch": 29, "title": "Chordate characteristics", "head": ["Trait", "What it is; what happens to it"],
     "rows": [
         (["Notochord", "dorsal supporting rod below the nerve cord; replaced by the vertebral column in "
                        "vertebrates"], s29(3, 9, 11)),
         (["Dorsal tubular nerve cord", "front end becomes the brain in most; protected by vertebrae in "
                                        "vertebrates"], s29(3)),
         (["Pharyngeal pouches", "become gills in aquatic vertebrates; only in embryos in most vertebrates; "
                                 "modified on land"], s29(3)),
         (["Postanal tail", "extends past the anus; disappears in the human embryo"], s29(3)),
     ]},
    {"ch": 29, "title": "Nonvertebrate chordates", "slides": s29(5, 6, 7),
     "head": ["", "Lancelets", "Sea squirts (tunicates)"],
     "rows": [
         ["Group", "cephalochordates", "urochordates"],
         ["Adult", "all four traits; segmented; filter feeder in shallow seas",
          "tunic; only gill slits remain; filter feeder"],
         ["Note", "notochord never replaced by vertebrae", "larva may be the vertebrates' ancestor"],
     ]},
    {"ch": 29, "title": "Vertebrate groups", "head": ["Group", "Key traits (examples)"],
     "rows": [
         (["Jawless fishes (agnathans)", "no jaws; cartilage; ostracoderms were the earliest vertebrate fossils "
                                         "(lampreys, hagfishes)"], s29(13)),
         (["Placoderms", "extinct jawed fishes of the Devonian; thought to be ancestral to sharks and bony "
                         "fishes"], s29(15)),
         (["Cartilaginous fishes (Chondrichthyes)", "cartilage skeleton; no gill cover; sense electric currents; "
                                                    "lateral line (sharks, rays, skates, chimaeras)"], s29(17)),
         (["Ray-finned fishes", "most bony fishes; fins supported by thin rays; operculum; swim bladder"],
          s29(20, 21)),
         (["Lobe-finned fishes", "fleshy fins with bones; gave rise to amphibians (lungfishes, coelacanth)"],
          s29(20, 22)),
         (["Amphibians", "limbs; smooth moist skin; lungs in most adults; 3-chambered heart; aquatic "
                         "reproduction, metamorphosis (salamanders, frogs, caecilians)"], s29(24, 28)),
         (["Reptiles", "thick scaly skin; lungs + rib cage; septum in the ventricle; internal fertilization; "
                       "shelled amniotic egg (turtles, lizards, snakes, tuataras, crocodilians, birds)"],
          s29(31, 35)),
         (["Birds (reptiles)", "feathers; keeled sternum, fused bones; lungs with air sacs; endothermy"],
          s29(37)),
         (["Mammals", "hair; mammary glands; differentiated teeth; 4-chambered heart; internal development in "
                      "most"], s29(41)),
     ]},
    {"ch": 29, "title": "Circulatory pathways", "head": ["Animals", "Heart and pathway"],
     "rows": [
         (["Fishes", "2 chambers (atrium, ventricle); single loop: heart → gills → body"], s29(25)),
         (["Amphibians, most reptiles", "3 chambers; double loop (lungs and body); some mixing of blood"],
          s29(24, 25)),
         (["Crocodilians, birds, mammals", "4 chambers; oxygen-poor blood to the lungs, oxygen-rich blood to the "
                                           "body"], s29(25, 41)),
     ]},
    {"ch": 29, "title": "Amniote skulls", "head": ["Skull", "Openings behind the eye socket (group)"],
     "rows": [
         (["Anapsid", "none (turtles; may be specialized diapsids, still debated)"], s29(33)),
         (["Diapsid", "two (all other reptiles, including birds)"], s29(33)),
         (["Synapsid", "one (mammals)"], s29(33, 42)),
     ]},
    {"ch": 29, "title": "Mammal lineages", "slides": s29(44, 45, 46),
     "head": ["", "Monotremes", "Marsupials", "Placentals"],
     "rows": [
         ["Young", "hatch from hard-shelled amniotic eggs", "develop in the female's pouch",
          "develop inside, fed through the placenta"],
         ["Feature", "cloaca: one urogenital opening", "pouch", "placenta: exchange of nutrients and wastes"],
         ["Examples", "duckbill platypus", "koala, opossum", "the orders in the table at 29.6.46"],
     ]},
    {"ch": 29, "title": "Look-alikes", "head": ["These", "The difference"],
     "rows": [
         (["notochord vs vertebral column", "embryonic rod vs the vertebrae that replace it"], s29(3, 9)),
         (["lancelets vs sea squirts", "cephalochordates, all 4 traits vs urochordates, tunic"], s29(5)),
         (["chordates vs vertebrates", "all 4 traits at some stage vs also a vertebral column and skull"],
          s29(3, 9)),
         (["gnathostomes vs tetrapods vs amniotes", "jaws vs four limbs vs amniotic egg"], s29(8, 12)),
         (["agnathans vs placoderms", "jawless vs extinct jawed fishes"], s29(13, 15)),
         (["cartilaginous vs bony fishes", "Chondrichthyes vs Osteichthyes"], s29(17, 20)),
         (["ray-finned vs lobe-finned", "thin bony rays vs fleshy fins with bones"], s29(20, 22)),
         (["operculum vs swim bladder", "gill cover vs gas sac for buoyancy"], s29(20)),
         (["ectothermy vs endothermy", "heat from the environment vs from the body"], s29(15, 37)),
         (["anapsid vs diapsid vs synapsid", "0 vs 2 vs 1 skull opening"], s29(33)),
         (["monotremes vs marsupials vs placentals", "eggs vs pouch vs placenta"], s29(44)),
         (["Artiodactyla vs Perissodactyla", "even-toed vs odd-toed hoofed mammals"], s29(46)),
         (["Rodentia vs Lagomorpha", "one pair vs two pairs of ever-growing incisors"], s29(46)),
     ]},
]

SEQUENCES += [
    {"ch": 29, "title": "Vertebrate innovations, in order", "slides": s29(8, 12),
     "note": "notochord (chordates) → vertebrae (vertebrates) → jaws (gnathostomes) → bony skeleton → lungs → "
             "four limbs (tetrapods) → amniotic egg (amniotes) → mammary glands (mammals)"},
    {"ch": 29, "title": "Geologic order", "slides": s29(12, 15, 33, 42),
     "note": "chordates at the start of the Cambrian → jawless and jawed fishes by the end of the Ordovician → "
             "jawed fishes (Silurian) → placoderms; amphibians from bony fishes (Devonian) → amniotes from "
             "amphibians (Carboniferous) → first true mammals (Triassic, with the dinosaurs)"},
    {"ch": 29, "title": "Vertebral column forms", "slides": s29(11),
     "note": "notochord under the neural tube → vertebral body grows around the notochord, arch around the neural "
             "tube → vertebra with ribs replaces the notochord"},
]

USES += [
    {"ch": 29, "title": "", "slides": s29(13, 30), "head": ["Source", "Use (and why)"],
     "rows": [
         (["Snake venom", "pain medications (textbook caption)"], s29(30)),
         (["Goats", "make drugs in their milk (genetically engineered)"], s29(30)),
         (["Pig hearts", "genetically altered pigs as a supply of hearts for transplants"], s29(30)),
     ]},
]

CLUES += [
    ("Chordates and fishes", [
        ("dorsal rod below the nerve cord", "notochord", s29(3)),
        ("become gills in aquatic vertebrates", "pharyngeal pouches", s29(3)),
        ("tail that extends beyond the anus", "postanal tail", s29(3)),
        ("chordate with all four traits as an adult, segmented", "lancelet (cephalochordate)", s29(5)),
        ("sessile adult with a tunic; only gill slits remain", "sea squirt (urochordate)", s29(5, 7)),
        ("animals with jaws", "gnathostomes", s29(12)),
        ("vertebrates with four limbs", "tetrapods", s29(12)),
        ("egg that surrounds the embryo in fluid", "amniotic egg (amniotes)", s29(12)),
        ("earliest vertebrate fossils", "ostracoderms", s29(13)),
        ("parasite that wiped out Great Lakes trout", "sea lamprey", s29(13)),
        ("depend on the environment for body heat", "ectothermy", s29(15)),
        ("jaws came from these", "gill arches", s29(15, 16)),
        ("extinct Devonian jawed fishes", "placoderms", s29(15)),
        ("pressure-sensing system of sharks", "lateral line", s29(17)),
        ("bony fish gill cover", "operculum", s29(20)),
        ("gas sac that changes buoyancy", "swim bladder", s29(20)),
        ("fish caught in 1938, thought extinct", "coelacanth (Latimeria)", s29(22, 23)),
        ("fish with lungs as well as gills", "lungfish", s29(22)),
    ]),
    ("Amphibians to mammals", [
        ("fossil between lobe-finned fishes and tetrapods", "Tiktaalik roseae", s29(26)),
        ("legless, worm-shaped amphibians", "caecilians", s29(28)),
        ("amphibian heart", "three chambers, double loop", s29(24)),
        ("skull with no opening behind the eye socket", "anapsid (turtles)", s29(33)),
        ("skull with two openings / one opening", "diapsid / synapsid", s29(33)),
        ("reptile with a third eye, ancient lineage", "tuatara", s29(35)),
        ("snakes lost their limbs for this", "burrowing", s29(35)),
        ("modified reptilian scale", "feather", s29(37)),
        ("breastbone ridge for flight muscles", "keel of the sternum", s29(37, 38)),
        ("bird lungs connect to these", "air sacs", s29(37)),
        ("hair and milk-producing glands", "mammals", s29(41)),
        ("earliest mammal group; lays eggs", "monotremes", s29(42, 44)),
        ("single urogenital opening", "cloaca", s29(44)),
        ("females have a pouch", "marsupials", s29(44)),
        ("only North American marsupial", "opossum", s29(45)),
        ("even-toed ungulates, ruminants", "Artiodactyla", s29(46)),
        ("fly with membranous wings; some echolocate", "Chiroptera (bats)", s29(46)),
        ("scaly armor, no teeth", "Pholidota (pangolins)", s29(46)),
    ]),
]

# ======================================================================== Ch 30
TABLES += [
    {"ch": 30, "title": "Primate trends", "head": ["Trend", "What it gives"],
     "rows": [
         (["Mobile limbs, grasping hands", "prehensile hands and feet; flat nails, sensitive pads; opposable thumb "
                                           "(powerful, precise grip); grasp tree limbs and bring food to the "
                                           "mouth"], s30(3, 5)),
         (["Flattened face, stereoscopic vision", "3-D imaging with depth perception; judges distances between "
                                                  "branches"], s30(3, 7, 8)),
         (["Color vision", "cone cells (bright light, color) besides rod cells (dim light, gray); humans and apes "
                           "have 3 kinds of cones"], s30(7)),
         (["Large, complex brain", "smaller smell area, larger sight area; hand-eye coordination; "
                                   "communication for social groups"], s30(9)),
         (["Reduced reproductive rate", "later maturity, longer life; long gestation; one offspring at a time; "
                                        "long dependency and learning"], s30(10)),
     ]},
    {"ch": 30, "title": "Primate groups", "head": ["Group", "Who (features)"],
     "rows": [
         (["Prosimians", "lemurs, tarsiers; the first primates to diverge"], s30(13, 17)),
         (["Anthropoids", "hominids, gibbons, Old World monkeys, New World monkeys"], s30(12, 13)),
         (["Old World monkeys", "Africa and Asia; no prehensile tail; protruding nose (baboons, rhesus)"], s30(12)),
         (["New World monkeys", "South America; often long prehensile tails; flat nose (spider monkey, "
                                "capuchin)"], s30(12)),
         (["Hominids", "chimpanzees, gorillas, orangutans and humans (textbook)"], s30(11, 13)),
         (["Hominins", "humans and species very closely related to them"], s30(11)),
     ]},
    {"ch": 30, "title": "Fossil apes", "head": ["Fossil", "Features"],
     "rows": [
         (["Proconsul", "about 35 MYA link between monkeys, gibbons and early hominids; baboon-sized, 165 cc brain; "
                        "no tail; walked on top of limbs like monkeys; probably ancestral to the dryopithecines"],
          s30(14, 15, 16)),
         (["Dryopithecus", "9.5 MYA, Spain; tree dweller that swung from branch to branch like gibbons"], s30(16)),
     ]},
    {"ch": 30, "title": "Hominins", "head": ["Species", "When (MYA)", "Features"],
     "rows": [
         (["Sahelanthropus tchadensis", "7.1–6.07", "on the timeline only (textbook: possibly bipedal, "
                                                     "chimp-sized brain)"], s30(21)),
         (["Ardipithecus kadabba", "5.8–5.2", "only teeth and bone bits"], s30(22)),
         (["Ardipithecus ramidus (Ardi)", "4.4", "Ethiopia; bipedal but often in trees; opposable big toe; "
                                                  "300–350 cc; no sharp canines"], s30(22, 23, 25)),
         (["Australopithecus afarensis (Lucy)", "3.9–3.02", "East Africa; bipedal; large canines; arms longer "
                                                             "than legs; closest to early Homo"], s30(28, 29)),
         (["A. africanus, A. sediba", "3.25–2.1; about 2.0", "southern Africa; gracile; sediba may be an ancestor "
                                                              "of Homo"], s30(21, 29)),
         (["Paranthropus robustus, P. boisei", "1.9–1.25; 2.25–1.25", "robust: massive jaws, large grinding teeth"],
          s30(21, 27)),
         (["Homo habilis, H. rudolfensis", "2.4–1.4", "maybe one species; “handyman”; maybe the first stone tools; "
                                                       "scavengers; omnivores"], s30(21, 31)),
         (["Homo erectus (H. ergaster)", "1.9–0.2", "taller (males 1.8 m); larger brain; projecting nose; first "
                                                     "out of Africa; fire"], s30(21, 32, 33)),
         (["Homo heidelbergensis", "0.75–0.2", "replaced H. erectus in Africa; first shelters; split into the "
                                                "lines of modern humans, Denisovans and Neanderthals"],
          s30(21, 38, 39)),
         (["Homo floresiensis", "–", "dwarf island species from H. erectus"], s30(38)),
         (["Homo neanderthalensis", "0.4–0.03", "Europe and Asia; brain 1,400 cc; heavily muscled; tools, fire, "
                                                 "burials"], s30(44, 45, 47)),
         (["Homo sapiens (Cro-Magnons)", "0.2–now", "brain 1,590 cc; compound tools, language, art; entered Asia "
                                                     "and Europe 100,000 years ago"], s30(37, 48, 50)),
     ], "wide": True},
    {"ch": 30, "title": "Brain sizes (cc)", "head": ["Who", "Brain"],
     "rows": [
         (["Proconsul", "165"], s30(14)),
         (["Ardi", "300–350"], s30(25)),
         (["Chimpanzee", "400"], s30(20)),
         (["Australopithecines", "370–515"], s30(27)),
         (["Early Homo", "600 or more"], s30(30)),
         (["Modern humans", "1,360"], s30(20, 45)),
         (["Neanderthals", "1,400"], s30(45)),
         (["Cro-Magnons", "1,590"], s30(48)),
     ]},
    {"ch": 30, "title": "Replacement vs multiregional", "slides": s30(40, 41, 43),
     "head": ["", "Replacement (out of Africa)", "Multiregional continuity"],
     "rows": [
         ["Claim", "modern humans evolved from archaic humans only in Africa, then replaced the early Homo "
                   "species in Asia and Europe", "modern humans arose from earlier Homo the same way in Africa, "
                                                 "Asia and Europe"],
         ["Evidence", "earliest modern humans found only in Africa; African mitochondrial DNA is the most diverse",
          "new species (H. floresiensis, H. naledi, Denisovans) revive it"],
     ]},
    {"ch": 30, "title": "Look-alikes", "head": ["These", "The difference"],
     "rows": [
         (["hominins vs hominids", "humans and close relatives vs also chimpanzees, gorillas, orangutans"], s30(11)),
         (["prosimians vs anthropoids", "lemurs and tarsiers vs monkeys, apes, humans"], s30(12, 17)),
         (["Old World vs New World monkeys", "no prehensile tail, protruding nose vs prehensile tail, flat nose"],
          s30(12)),
         (["rod cells vs cone cells", "dim light, gray vs bright light, color"], s30(7)),
         (["Proconsul vs Dryopithecus", "walked on top of limbs vs swung from branch to branch"], s30(14, 16)),
         (["bipedal vs quadrupedal", "two feet vs all fours"], s30(20)),
         (["gracile vs robust", "slender (Australopithecus) vs massive jaws (Paranthropus)"], s30(27)),
         (["Ardi vs Lucy", "Ardipithecus, 4.4 MYA vs Australopithecus afarensis"], s30(22, 29)),
         (["H. habilis vs H. erectus", "“handyman”, scavenger vs taller, migrated, fire"], s30(31, 33)),
         (["Denisovans vs Neanderthals", "Asian vs European lineage of H. heidelbergensis"], s30(39)),
         (["Bergmann's vs Allen's rule", "bulkier bodies vs shorter limbs, digits, ears in the cold"], s30(53)),
         (["replacement vs multiregional", "Africa only vs everywhere alike"], s30(40, 43)),
     ]},
]

SEQUENCES += [
    {"ch": 30, "title": "Primate groups split off (oldest first)", "slides": s30(13, 17),
     "note": "lemurs → tarsiers (prosimians) → New World monkeys → Old World monkeys → gibbons → orangutans → "
             "gorillas → chimpanzees and humans (5–7 MYA)"},
    {"ch": 30, "title": "Hominin evolution", "slides": s30(21, 22, 27, 30, 39, 48),
     "note": "Sahelanthropus → ardipithecines (Ardi, 4.4 MYA) → australopithecines (4–1.5 MYA; Lucy) → early Homo "
             "(about 2.5 MYA: H. habilis, then H. erectus, out of Africa) → H. heidelbergensis → three lineages: "
             "H. sapiens (Africa), Denisovans (Asia), Neanderthals (Europe) → Cro-Magnons → agriculture"},
]

USES += [
    {"ch": 30, "title": "", "slides": s30(12), "head": ["Animal", "Use"],
     "rows": [
         (["Baboons, rhesus monkeys", "medical research (Old World monkeys)"], s30(12)),
     ]},
]

CLUES += [
    ("Primates", [
        ("living in trees", "arboreal", s30(3)),
        ("adapted for grasping and holding", "prehensile", s30(5)),
        ("thumb that can touch each other finger", "opposable thumb", s30(5)),
        ("3-D imaging with good depth perception", "stereoscopic vision", s30(7)),
        ("light-sensitive cells for color in bright light", "cone cells", s30(7)),
        ("humans and very close relatives", "hominins", s30(11)),
        ("humans and chimpanzees shared an ancestor then", "5–7 MYA", s30(11)),
        ("tails that grasp, flat noses, South America", "New World monkeys", s30(12)),
        ("“organ grinder's monkey”", "capuchin", s30(12)),
        ("baboon-sized 35-MYA link, no tail", "Proconsul", s30(14)),
        ("swung from branch to branch, Spain, 9.5 MYA", "Dryopithecus", s30(16)),
        ("first primates to diverge; lemurs and tarsiers", "prosimians", s30(17)),
        ("ancestor of all primates resembled this", "tree shrews", s30(17)),
        ("human chromosome made of two chimp chromosomes", "chromosome 2", s30(18, 19)),
        ("mobile DNA elements in the same places in humans and chimps", "transposons (Alu)", s30(18, 19)),
    ]),
    ("Hominins", [
        ("standing erect, walking on two feet", "bipedalism", s30(20)),
        ("4.4-MYA female skeleton from Ethiopia", "Ardi (Ardipithecus ramidus)", s30(22)),
        ("bipedal but with an opposable big toe", "Ardi", s30(23)),
        ("different body parts evolving at different rates", "mosaic evolution", s30(27)),
        ("slender australopiths / massive-jawed ones", "gracile / robust (Paranthropus)", s30(27)),
        ("famous A. afarensis female", "Lucy", s30(28, 29)),
        ("2-MYA South African species, maybe ancestral to Homo", "A. sediba", s30(29)),
        ("“handyman”", "Homo habilis", s30(31)),
        ("first to leave Africa; knew fire", "Homo erectus", s30(32, 33)),
        ("dwarf island species", "Homo floresiensis", s30(38)),
        ("replaced H. erectus in Africa; first shelters", "Homo heidelbergensis", s30(38)),
        ("Asian lineage of H. heidelbergensis", "Denisovans", s30(39)),
        ("modern humans evolved in Africa only, then replaced others", "replacement (out-of-Africa) model",
         s30(40)),
        ("modern humans arose alike in Africa, Asia, Europe", "multiregional continuity hypothesis", s30(43)),
        ("brain 1,400 cc; massive brow ridges; Ice Age Europe", "Neanderthals", s30(45)),
        ("oldest fossils called H. sapiens", "Cro-Magnons", s30(48)),
        ("large mammals hunted to extinction", "Pleistocene overkill", s30(49)),
        ("culture shaped by natural selection", "biocultural evolution", s30(51)),
        ("bulkier bodies in cold regions", "Bergmann's rule", s30(53)),
        ("shorter limbs, digits, ears in the cold", "Allen's rule", s30(53)),
        ("most variation within, not between, groups", "Lewontin's 17 genes", s30(54)),
    ]),
]
