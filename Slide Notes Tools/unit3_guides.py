"""Unit 3 quick guides (Ch 28-30), merged into quick_guides.QUICK_GUIDE.

Same format as quick_guides.py, plus these items (Unit 3 on):
    {"big": "..."}                                          the section's big idea, printed first ("Big idea: ...")
    {"fig": (chapter, slide), "caption": "..."}             the picture on that slide (reading copy)
    {"book": page, "clip": (x0, y0, x1, y1), "caption": ...}  a textbook figure: book page, crop in PDF points
    {"check": [(question, answer), ...]}                    self-test with answers (reading copy only)
**term** prints the term in bold where it is defined.
The printable copy leaves the figures and self-tests out and turns every slide code into chapter.page.slide.

How they are written (the user's requests, Nov 4, and the research in PRINTED_NOTES.md, "Writing the quick guides"):
easy to understand for someone who hasn't read the chapter; big idea first; the concept in plain words before its
name; word roots that make a term memorable; a concrete example for each idea; the "why"; analogies only where
they fit, with their limit; look-alikes side by side; common mistakes stated and corrected; short sentences;
diagrams next to the text they explain; a few self-test questions per section.
"""

QUICK_GUIDE = {}

# ======================================================================== Ch 28
QUICK_GUIDE[28] = {
    "intro": [
        "**What this chapter is about.** A tour of the **invertebrates**, animals without a backbone (28.1.3). "
        "It first sets up the four features biologists use to sort animals. Then it visits the groups in "
        "evolutionary order, from sponges, the simplest, to sea stars, the invertebrates closest to us.",
        "**What makes an animal.** An animal is made of many cells (multicellular). It can't make its own food, so "
        "it eats other living things (heterotrophic). Fungi also take in food from outside, but they digest it "
        "outside the body and absorb it; animals swallow food and digest it inside (28.1.3). Animal cells have no "
        "cell walls, and most animals can move, using nerves and muscles (28.1.4; textbook Fig. 28.1). Many "
        "reproduce sexually, some asexually, some both, and many have a diploid life cycle (28.1.3).",
        "**One family.** Animals descend from a single common ancestor. They split into invertebrates and "
        "vertebrates, animals that at some stage have a spinal cord (backbone) (28.1.3). Use the family tree below "
        "as your map: each group in this chapter is one branch of it.",
        {"book": 510, "clip": (196, 58, 582, 432),
         "caption": "The animal family tree (textbook Fig. 28.3, not on the slides). Read it from left to right: each "
                    "label on a branch is a new feature that the groups to its right share. Sponges branch off "
                    "first; then tissue layers appear (comb jellies, cnidarians); then bilateral symmetry, 3 tissue "
                    "layers and a body cavity (Bilateria). These split into protostomes (lophotrochozoans with "
                    "spiral cleavage, and ecdysozoans, which molt a cuticle) and deuterostomes (echinoderms and "
                    "chordates)."},
    ],
    "sections": {
        1: [
            {"big": "Four features sort animals into groups: body symmetry, the number of tissue layers in the "
                    "embryo, the body cavity, and which embryo opening becomes the mouth. The later sections use "
                    "them, so learn them first."},
            ("Where animals came from", [
                "Picture a hollow ball of cells, each with a flagellum, a whip-like tail for swimming. The "
                "**colonial flagellate hypothesis** says animals descend from an ancestor like that (28.1.5).",
                "**Choanoflagellates** are single-celled protists (not animals) with a flagellum. Among protists, "
                "they look most like the last single-celled ancestor of animals (28.1.5).",
                "The proposed steps: a few flagellated cells clump into a hollow sphere; some cells specialize; "
                "cells fold inward, making two tissue layers (28.1.5, 28.1.6).",
                "The evidence: sponges have choanocytes, cells that look like choanoflagellates (28.1.6).",
                "An alternative hypothesis: the ancestor was a cell whose life cycle already had several cell "
                "types. Its evidence is sponges' archaeocytes, cells that can turn into other cell types (28.1.6).",
                "Today's body plans were already present by the Cambrian period. Small changes in DNA and in "
                "**Hox genes**, genes that lay out the body during development, may explain the differences "
                "(28.1.7).",
            ]),
            {"fig": (28, 6), "caption": "Two hypotheses for how the first animals (sponges) arose from single cells: "
                                        "follow the three numbered steps in each column."},
            ("Symmetry: the body's shape pattern", [
                "Word root: symmetry is Greek for “together” + “measure” (textbook).",
                "No particular body shape is **asymmetry** (sponges) (28.1.8).",
                "A body arranged around a center, like a wheel, has **radial symmetry**: any cut through the center "
                "gives identical halves (jellyfish). Why it helps: the animal can reach out in all directions from "
                "its center (28.1.8, 28.1.10).",
                "A body with a definite right and left half has **bilateral symmetry**: only one cut, down the "
                "middle, works (a turtle) (28.1.8).",
                "Why it matters: bilateral animals tend to be active and move head first, so the brain and sense "
                "organs gather at the front. That is **cephalization** (Greek kephale, “head”) (28.1.8).",
            ]),
            {"fig": (28, 10), "caption": "Radial symmetry (jellyfish: many planes) vs bilateral symmetry (turtle: "
                                         "one plane). Count the cutting planes in each."},
            ("Germ layers: the embryo's first tissue layers", [
                "The first tissue layers in an embryo are its **germ layers**; the organs grow from them (28.1.9).",
                "Two layers (ectoderm outside, endoderm inside) make an animal **diploblastic**: comb jellies and "
                "cnidarians. A third, middle layer, the mesoderm, makes it **triploblastic**, with organs: the "
                "rest of this chapter's groups, from the lophotrochozoans on (28.1.9; textbook p. 511).",
            ]),
            ("Protostomes vs deuterostomes: how the embryo develops", [
                "Word roots: protostome = “first mouth” and deuterostome = “second mouth” (textbook). The names say "
                "which embryo opening becomes the mouth (28.1.9).",
                "Step 1, **cleavage**: the egg divides without growing. In protostomes it is spiral (new cells "
                "sit at an angle) and determinate (each cell's fate is fixed). In deuterostomes it is radial (new "
                "cells sit on top) and indeterminate (a separated cell can still become a whole embryo) (28.1.11, "
                "28.1.12).",
                "Step 2, the **blastula**, a hollow ball of cells, folds in to make the first opening, the "
                "**blastopore**. In protostomes it becomes the mouth. In deuterostomes it becomes the anus, and the "
                "mouth forms second (28.1.11, 28.1.12).",
                "Step 3, the body cavity. A cavity completely lined by mesoderm is a true **coelom** (Greek koiloma, "
                "“cavity”). Some protostomes have one, and so do the deuterostomes. Protostomes: it forms by a "
                "splitting of the mesoderm. Deuterostomes: by pouches pushing out of the primitive gut (28.1.11).",
                "Most invertebrates are protostomes (mollusks, annelids, arthropods...). The deuterostomes are the "
                "echinoderms and the chordates, including us (28.5.69; textbook p. 511).",
            ]),
            {"fig": (28, 12), "caption": "Protostomes vs deuterostomes, compared row by row: cleavage, fate of the "
                                         "blastopore, and how the coelom forms."},
            ("Traps", [
                "Protostome: the blastopore becomes the mouth. Deuterostome: it becomes the anus. Don't swap them.",
                "Not the same thing: radial cleavage (deuterostome embryos) and radial symmetry (jellyfish).",
                "Germ layers are embryo tissue layers; the coelom is a body cavity.",
            ]),
            {"check": [
                ("A jellyfish can be cut into identical halves through its center in many directions; a turtle only "
                 "one way. Name both symmetries.", "Radial; bilateral (28.1.8)."),
                ("In an embryo, the first opening becomes the anus. Protostome or deuterostome? Name a group.",
                 "Deuterostome: echinoderms or chordates (28.1.11, 28.5.69)."),
                ("Which embryos have cells whose fate is fixed early?", "Protostomes: spiral, determinate cleavage "
                 "(28.1.12)."),
            ]},
        ],
        2: [
            {"big": "The simplest animals. Sponges have no true tissues. Comb jellies and cnidarians have two tissue "
                    "layers around a central cavity and radial bodies; cnidarians sting."},
            ("Sponges (phylum Porifera: “pore bearers”)", [
                "No true tissues: just a few cell types working together, a cellular level of organization "
                "(28.2.13).",
                "How a sponge feeds: **collar cells (choanocytes)** beat their flagella. That pulls water in through "
                "the pores, into the central cavity, and out the **osculum**, the opening at the top (28.2.13, "
                "28.2.14).",
                "The sponge stays attached in one place (**sessile**) and strains food out of that water: a "
                "**filter feeder** (28.2.13).",
                "Its skeleton: **spicules**, small needle-like pieces, plus spongin fibers. Amoebocytes carry "
                "nutrients from cell to cell (28.2.14; textbook p. 513).",
                "Reproduction: asexual, by fragmentation or budding; sexual, making a flagellated larva that swims "
                "to a new place. Sponges regenerate a whole body from a small part (28.2.13).",
            ]),
            {"fig": (28, 14), "caption": "Sponge anatomy: follow the water in through the pores and out the osculum; "
                                         "the collar cells (d) drive it and trap food."},
            ("Comb jellies (phylum Ctenophora)", [
                "Solitary, free-swimming sea animals: small, transparent, sometimes **bioluminescent**, making "
                "their own light (28.2.15).",
                "The body is mostly **mesoglea**, a jellylike substance. Rows of beating cilia (tiny hairs) move "
                "them: they are the largest animals moved this way. Sticky cells, **colloblasts**, catch prey "
                "(28.2.15).",
                "Their DNA looks older than sponges', so they may be the oldest animal lineage. This is still "
                "debated (28.2.15; textbook p. 514).",
            ]),
            ("Cnidarians (phylum Cnidaria): the stingers", [
                "Hydras, sea anemones, corals and jellyfish, mostly in shallow seas (28.2.16, 28.2.18).",
                "Named for their stinging cells, **cnidocytes**. Each holds a **nematocyst** (Greek “thread” + "
                "“bladder”): a fluid-filled capsule with a coiled thread that fires to trap or poison prey, like a "
                "tiny harpoon (28.2.16).",
                "The body is a two-layered sac. Outside: a protective epidermis. Inside: a layer that digests food "
                "in the **gastrovascular cavity** (Greek gastros, “stomach”), whose one opening is both mouth and "
                "anus, like a bag (28.2.16, 28.2.20). Mesoglea lies between the two layers (28.2.21).",
                "Two body forms. A tube with its mouth up is a **polyp** (hydra, sea anemone). A bell with its mouth "
                "down is a **medusa** (jellyfish) (28.2.16).",
                "Sea anemones are sessile polyps. Corals are like sea anemones in a calcium carbonate case; their "
                "colonies build reefs, such as the Great Barrier Reef (28.2.18).",
                "Hydra: a small freshwater polyp, about a quarter of an inch long. Its nerve cells form a "
                "**nerve net**, a web with no brain. It reproduces sexually, and asexually by budding (28.2.20, "
                "28.2.21).",
                "True jellyfish: the medusa is the main stage, and the polyp stays small (28.2.20).",
            ]),
            {"fig": (28, 19), "caption": "Cnidarian diversity: a sea anemone (solitary polyp), corals (colonial "
                                         "polyps), the Portuguese man-of-war (a colony) and a jellyfish (medusa)."},
            {"fig": (28, 21), "caption": "Hydra: a polyp with tentacles (a), a bud (b), and its two tissue layers "
                                         "with mesoglea between them and cnidocytes (c)."},
            ("Traps", [
                "Sponges have no true tissues; comb jellies and cnidarians have two tissue layers (diploblastic).",
                "Cnidocyte = the stinging cell; nematocyst = the capsule inside it.",
                "Colloblasts (comb jellies) stick; nematocysts (cnidarians) sting.",
                "Polyp = mouth up; medusa = mouth down.",
                "Myth: the Portuguese man-of-war is a jellyfish. Fact: it is a colony of polyps and medusae "
                "(28.2.19).",
            ]),
            {"check": [
                ("Which cells move the water through a sponge, and where does it leave?",
                 "Collar cells (choanocytes); the osculum (28.2.13–14)."),
                ("What is the difference between a cnidocyte and a nematocyst?",
                 "The cnidocyte is the stinging cell; the nematocyst is the capsule inside it (28.2.16)."),
                ("A cnidarian with its mouth facing down is a ...?", "Medusa (28.2.16)."),
            ]},
        ],
        3: [
            {"big": "The lophotrochozoans, a big protostome group with three tissue layers and organs: mollusks, "
                    "segmented worms (annelids), flatworms and rotifers. Watch how each solves moving, feeding and "
                    "circulating blood."},
            ("Lophotrochozoans: two kinds", [
                "Bilaterally symmetrical, three germ layers, organs; some have a true coelom (28.3.22).",
                "**Lophophorans** (bryozoans, brachiopods, phoronids) feed with a **lophophore**: a crown of "
                "ciliated tentacles around the mouth (28.3.22, 28.3.23).",
                "**Trochozoans** have a **trochophore**, a tiny swimming larva with bands of cilia: mollusks and "
                "annelids, plus flatworms and rotifers (28.3.22, 28.3.23).",
            ]),
            {"fig": (28, 23), "caption": "The lophophore (a), a feeding crown, and the trochophore larva (b), with its "
                                         "bands of cilia."},
            ("Mollusks (phylum Mollusca)", [
                "Snails, clams, squids and their relatives: over 150,000 species (28.3.24; textbook p. 516).",
                "A three-part body. The **visceral mass** holds the internal organs. The **mantle** covers it and "
                "may secrete a shell or help form gills or lungs. The **foot** is a muscle for moving, attaching or "
                "catching food (28.3.24).",
                "Many have a **radula**: a tongue covered in rows of teeth, used like a file to scrape food "
                "(28.3.25).",
                "Nerves: several **ganglia** (clusters of nerve cells) joined by nerve cords. The coelom is "
                "reduced, mostly around the heart (28.3.26).",
                "Circulation is open: the heart pumps the blood (**hemolymph**) out of vessels into open spaces "
                "around the organs, the **hemocoel** (Greek “blood” + “cavity”) (28.3.26). In a closed system, by "
                "contrast, blood stays inside vessels, like water in pipes.",
            ]),
            {"fig": (28, 25), "caption": "The mollusk body plan: find the visceral mass, mantle and foot; the radula's "
                                         "teeth are shown in (b)."},
            ("The three mollusk classes", [
                "**Bivalves** (clams, oysters, mussels, scallops): a shell of two hinged parts; no head and no "
                "radula. Cilia on the gills draw water into the mantle cavity, and the gills filter out food "
                "(28.3.27).",
                "Freshwater clams have separate sexes and internal fertilization (28.3.27).",
                "**Gastropods** (Greek “stomach” + “foot”: snails, slugs, conchs, nudibranchs): the largest class. "
                "A flat foot to creep on, a one-piece coiled shell in most, and a head with eyes on tentacles "
                "(28.3.29).",
                "**Cephalopods** (“head-footed”: squids, octopuses, nautilus): they squeeze water out of the mantle "
                "cavity for jet propulsion. Arms with suckers catch prey; a beak tears it. Senses are "
                "well developed, and octopuses can learn (28.3.31).",
            ]),
            {"fig": (28, 28), "caption": "Bivalves: a scallop, mussels, and the inside of a clam (Anodonta). Follow the "
                                         "water: in the incurrent siphon, over the gills, out the excurrent siphon."},
            ("Annelids (phylum Annelida, Latin “little ring”): segmented worms", [
                "The body is a row of ring-like segments separated by **septa** (partitions) (28.3.33).",
                "The fluid-filled coelom is a **hydrostatic skeleton**: muscles push against the fluid, a bit like "
                "squeezing a water balloon. Unlike one balloon, the septa divide it, so each segment can move on its "
                "own (28.3.33; textbook p. 518).",
                "Closed circulation (blood stays in vessels), a ventral (belly-side) solid nerve cord, and "
                "**setae** (Latin “bristle”), which grip the ground. **Oligochaetes** have few setae, "
                "**polychaetes** many (28.3.33).",
                "Earthworm digestion: mouth → muscular pharynx → crop (stores food) → gizzard (grinds it) → long "
                "intestine → anus. The intestine's fold, the **typhlosole**, adds surface for absorption (28.3.34).",
                "Segmentation shows inside too: each segment has its own ganglia, excretory tubes "
                "(**nephridia**, Greek nephros, “kidney”) and blood-vessel branches (28.3.35).",
                "Earthworms are **hermaphrodites**: each has both male and female organs. Two worms lie side by "
                "side, facing opposite ways. A thickened band, the **clitellum**, secretes mucus that keeps the "
                "sperm from drying out. There is no larva (28.3.36).",
                "Polychaetes are mostly marine, with setae in bundles on **parapodia** (Greek “beside” + “foot”), "
                "paddle-like flaps. Clam worms (Nereis) are predators (28.3.38).",
                "Leeches live mostly in fresh water, have no setae and two suckers. Their saliva holds hirudin, "
                "which stops blood from clotting (28.3.38).",
            ]),
            {"fig": (28, 37), "caption": "Earthworm: the digestive tract along the body, and a cross section (find the "
                                         "coelom, setae, nephridium, typhlosole and ventral nerve cord)."},
            ("Flatworms (phylum Platyhelminthes)", [
                "Flat bodies with no circulatory or respiratory organs; a sac body plan with one opening; no body "
                "cavity (28.3.40). How they cope without them: the branched digestive cavity delivers nutrients and "
                "oxygen to the cells (textbook p. 521).",
                "Planarians (Dugesia) live free in fresh water. The head has **auricles** (side flaps that sense "
                "chemicals and touch) and two light-sensitive **eyespots** (28.3.42).",
                "Feeding: a tube, the pharynx, comes out of the mouth on the underside and sucks food into a "
                "branched gastrovascular cavity (28.3.41).",
                "Excretion: **flame cells**, whose beating cilia move fluid into canals; they also control water "
                "balance (28.3.41, 28.3.43). The name: the beating cilia reminded an early investigator of a "
                "flickering flame (textbook p. 521).",
                "Nerves: two nerve cords joined by cross nerves, like a ladder, with paired ganglia as a primitive "
                "brain: a **ladder-type nervous system**. Three muscle layers (28.3.42).",
                "Planarians are hermaphrodites that cross-fertilize, and they also reproduce asexually by "
                "regeneration (28.3.43).",
            ]),
            {"fig": (28, 41), "caption": "Planarian: the branched digestive cavity, the excretory canals with flame "
                                         "cells, and the hermaphrodite reproductive system."},
            ("Parasitic flatworms", [
                "**Flukes (trematodes)** and **tapeworms (cestodes)** live inside a host (28.3.44).",
                "Why their heads changed: they don't hunt, so they have lost cephalization. Hooks or suckers replace "
                "the head, and they need no well-developed nervous system or gut (28.3.44).",
                "Two hosts. The **primary host** carries the adult worm; the **secondary host** carries the larvae "
                "and passes them on (28.3.44, 28.3.46).",
                "Blood fluke Schistosoma, in steps: larvae burrow through human skin and mature in the liver. Adults "
                "live in blood vessels of the gut. Eggs leave in feces and hatch in water. Larvae grow in a snail "
                "(the secondary host), then swim off to find a human (28.3.45).",
                "Clonorchis sinensis, the Chinese liver fluke, is the other fluke named; textbook: people usually "
                "catch it by eating raw fish (28.3.44; textbook p. 523).",
                "A tapeworm has a **scolex**, a head with hooks and suckers, then a chain of **proglottids**: "
                "segments, each with male and female sex organs, that fill with eggs (28.3.46).",
                "Pork tapeworm Taenia solium: humans (primary host) eat undercooked pork with bladder worms, larvae "
                "in cysts. The tapeworm grows in the intestine, and eggs leave in feces. Pigs (secondary host) eat "
                "them, and the larvae encyst in muscle. Tapeworms interfere with the host's nutrient absorption "
                "(28.3.46, 28.3.47).",
            ]),
            {"fig": (28, 45), "caption": "Blood fluke life cycle: follow steps 1–6 between the human (primary host) "
                                         "and the snail (secondary host)."},
            {"fig": (28, 47), "caption": "Pork tapeworm life cycle: follow steps 1–6 between the human (primary host) "
                                         "and the pig (secondary host)."},
            ("Rotifers (phylum Rotifera)", [
                "Microscopic animals named for the **corona**, a crown of cilia that looks like a turning wheel. It "
                "moves the animal and sweeps food to the mouth. About 2,000 species, mostly freshwater (28.3.48).",
            ]),
            {"fig": (28, 49), "caption": "A rotifer: the corona of cilia at the front end, the digestive tract and "
                                         "flame bulbs."},
            ("Traps", [
                "Lophophore = feeding crown; trochophore = larva.",
                "Mollusks: open circulation, reduced coelom. Annelids: closed circulation, large divided coelom.",
                "Bivalves have no radula and no head.",
                "Oligochaetes = few setae (earthworms); polychaetes = many (marine).",
                "Primary host = adult worm; secondary host = larvae.",
                "Flame cells are excretory cells, not nerve or digestive cells.",
            ]),
            {"check": [
                ("Which mollusk class has two hinged shells and no radula?", "Bivalves (28.3.27)."),
                ("An annelid with no setae whose saliva stops blood clotting?", "A leech (hirudin) (28.3.38)."),
                ("In the pork tapeworm cycle, which host carries the bladder worms?",
                 "The pig, the secondary host (28.3.47)."),
                ("Why have parasitic flatworms lost cephalization?",
                 "They don't hunt; they hold on with hooks or suckers (28.3.44)."),
            ]},
        ],
        4: [
            {"big": "The ecdysozoans, protostomes that molt: roundworms and arthropods. Arthropods, with jointed "
                    "armor, segments, good senses, varied breathing organs and metamorphosis, are the most "
                    "successful animal group."},
            ("Ecdysozoans (Greek ecdysis, “stripping off”)", [
                "Roundworms and arthropods build a **cuticle**, an outer covering that protects and supports them. "
                "They shed it (**molting**) to grow (28.4.50).",
            ]),
            ("Roundworms (phylum Nematoda)", [
                "Nonsegmented worms (28.4.51).",
                "Their body cavity is lined by mesoderm on the body wall but not around the gut: a "
                "**pseudocoelom** (“false cavity”). It holds the organs and works as a hydrostatic skeleton "
                "(28.4.51; textbook p. 525).",
                "Caenorhabditis elegans, a free-living roundworm, is a model animal for genetics and development "
                "(28.4.51).",
                "Parasites of humans and pets (28.4.52, 28.4.53):",
                "Ascaris: intestinal worm, over 200,000 eggs a day.",
                "Trichinella: trichinosis, from eating rare pork.",
                "Filarial worms: heartworm, fatal in dogs; Wuchereria, carried by mosquitoes, blocks lymph "
                "vessels so the limbs swell (elephantiasis).",
            ]),
            {"fig": (28, 53), "caption": "Roundworm parasites: Ascaris, Trichinella larvae encysted in muscle, and "
                                         "elephantiasis caused by a filarial worm."},
            ("Arthropods (Greek “jointed foot”): five keys to success", [
                "**Exoskeleton**: a rigid, jointed outer skeleton of **chitin**, a tough polysaccharide. Why they "
                "molt: like a suit of armor, it can't grow. So a bigger, soft one forms underneath, and the animal "
                "climbs out of the old one; this is molting (28.4.54, 28.4.55; textbook p. 526).",
                "Segmentation, with segments fused into a head, thorax and abdomen (28.4.54).",
                "A well-developed nervous system: brain, ventral nerve cord, and simple or compound eyes (28.4.54).",
                "Varied breathing organs: gills (in water), book lungs (spiders) or **tracheae** (Latin “windpipe”), "
                "air tubes (insects) (28.4.54).",
                "**Metamorphosis** (Greek “change of form”): larva and adult look different and eat different food, "
                "so they don't compete (28.4.54).",
            ]),
            {"fig": (28, 55), "caption": "Arthropod exoskeleton: a joint moved by flexor and extensor muscles (a), "
                                         "the cuticle's layers (b), and a dragonfly molting (c)."},
            ("Crustaceans (“crusty” shells)", [
                "A crusty exoskeleton of chitin plus calcium carbonate, compound eyes, five pairs of head "
                "appendages; mostly aquatic (28.4.56).",
                "Decapods (“ten feet”: crabs, crayfish, lobsters, shrimp) are the most familiar. Copepods and krill "
                "are small swimmers that eat algae. Barnacles live attached, e.g. to wharf pilings (28.4.56).",
                "Crayfish: head and thorax fused into a **cephalothorax** (“head” + “breastplate”) under a "
                "**carapace**, a shield (28.4.58).",
                "Crayfish body: five pairs of walking legs, the first with claws; swimmerets on the abdomen; gills; "
                "open circulation; a reduced coelom; green glands excrete wastes; a well-developed nervous system; "
                "separate sexes (28.4.58, 28.4.59).",
            ]),
            {"fig": (28, 59), "caption": "Male crayfish: the cephalothorax with five pairs of walking legs, and the "
                                         "abdomen with swimmerets, uropods and telson."},
            ("Centipedes and millipedes", [
                "Centipedes (“hundred legs”): one pair of walking legs per segment. The first trunk appendages are "
                "venomous jaws for killing prey (28.4.61).",
                "Millipedes: one pair of legs on each of four thoracic segments, two pairs on each abdominal "
                "segment; cylindrical bodies (28.4.61).",
            ]),
            ("Insects", [
                "Mostly on land; they breathe through tracheae (28.4.63).",
                "Three body parts: the head (sense organs, mouthparts); the thorax (three pairs of legs and, in "
                "many, one or two pairs of wings); the abdomen (most internal organs) (28.4.63).",
                "**Complete metamorphosis** (butterflies): larva → pupa → adult, with the body completely "
                "reorganized. **Incomplete metamorphosis** (grasshoppers): a gradual change (28.4.63, 28.4.64; "
                "textbook p. 528 for the pupa).",
                "Grasshopper body: jumping third legs; a **tympanum** (eardrum) on the first abdominal segment; the "
                "female's ovipositor lays eggs (28.4.64).",
                "Grasshopper systems: food is stored in the crop, then ground in the gizzard. **Malpighian tubules** "
                "excrete. Air enters **spiracles** (openings) and flows through tracheae. The heart is slender and "
                "tubular (28.4.64).",
                "Insect orders differ in wings and mouthparts: beetles (hard forewings, chewing), wasps (narrow "
                "waist, stinger), lice (wingless, piercing-sucking), dragonflies (28.4.65).",
            ]),
            {"fig": (28, 65), "caption": "Insect orders: compare the wings and mouthparts (mealybug, beetle, "
                                         "leafhopper, head louse, wasp, dragonfly)."},
            {"fig": (28, 66), "caption": "Female grasshopper: outside (a), with the legs and wings on the thorax and "
                                         "the tympanum on the abdomen, and inside (b)."},
            ("Chelicerates", [
                "Spiders, scorpions, ticks, mites and horseshoe crabs (28.4.67).",
                "The appendages are on the cephalothorax, none on the abdomen. First pair: **chelicerae**, for "
                "feeding and defense. Second pair: **pedipalps**, for feeding or sensing (28.4.67, 28.4.68).",
            ]),
            {"fig": (28, 68), "caption": "Chelicerates: horseshoe crab, scorpion (chelicerae, pedipalps, stinger) "
                                         "and black widow spider (cephalothorax, abdomen, four pairs of legs)."},
            ("Traps", [
                "Cuticle = the covering that is molted; chitin = what the arthropod exoskeleton is made of.",
                "Pseudocoelom (roundworms) is incompletely lined by mesoderm; a true coelom is lined completely.",
                "Tracheae (air tubes) start at spiracles (openings).",
                "Complete metamorphosis has a pupa; incomplete (grasshopper) doesn't.",
                "Chelicerae come first, pedipalps second.",
                "Legs and wings are on the thorax; the tympanum is on the abdomen. The slide's grasshopper figure text has "
                "it backwards (28.4.63, 28.4.64).",
            ]),
            {"check": [
                ("Why must arthropods molt?", "Their exoskeleton can't grow (28.4.54)."),
                ("Air enters an insect through ... and travels in ...", "Spiracles; tracheae (28.4.64)."),
                ("How does a pseudocoelom differ from a true coelom?",
                 "It is incompletely lined by mesoderm (28.4.51)."),
                ("Which chelicerate appendages come first?", "The chelicerae (28.4.67)."),
            ]},
        ],
        5: [
            {"big": "Echinoderms are deuterostomes, so they are our relatives despite their star shape. Their "
                    "water-filled tube feet do the work that other animals' legs, gills and blood vessels do."},
            ("Echinoderms (Greek echinos, “spiny”, + derma, “skin”)", [
                "Sea stars, sea urchins, sea cucumbers and sand dollars: marine deuterostomes, related to chordates "
                "(28.5.69).",
                "Radial symmetry (in five parts) as adults, but bilateral symmetry as larvae: a sign that they "
                "descend from bilateral ancestors (28.5.69; textbook p. 532).",
                "An **endoskeleton** (inside skeleton) of calcium-rich plates with spines; a central nerve ring with "
                "branches (28.5.69).",
                "The **water vascular system**: water-filled canals ending in **tube feet**. It does locomotion, "
                "feeding, gas exchange and sensing (28.5.69).",
            ]),
            ("Sea star", [
                "How it moves: water enters through the **sieve plate (madreporite)** and runs through canals. An "
                "**ampulla**, a bulb, contracts and pushes water into its tube foot, which extends and grips. "
                "Expanding and contracting the tube feet in turn produces movement (28.5.72).",
                "Think of each tube foot as a small suction cup worked by water pressure (textbook p. 533: the "
                "center pulls back, giving suction).",
                "Tube feet pull open clams and oysters (bivalves) for food (28.5.72).",
                "Echinoderms have no respiratory, excretory or circulatory system; fluids in the coelom and water "
                "vascular system do those jobs (28.5.72; textbook p. 533). They reproduce sexually and asexually "
                "(28.5.72).",
            ]),
            {"fig": (28, 70), "caption": "Sea star anatomy: trace the water vascular system (sieve plate, radial canal, "
                                         "tube feet); also the stomachs, gonads and endoskeletal plates."},
            ("Traps", [
                "Echinoderms are deuterostomes, like us, not protostomes.",
                "Their skeleton is internal (endoskeletal plates), not an exoskeleton.",
                "Radial adults, bilateral larvae.",
                "Myth: a starfish is a fish. Fact: it is an echinoderm, an invertebrate (28.5.69).",
            ]),
            {"check": [
                ("Name the parts a sea star uses to move, in order.",
                 "Sieve plate → canals → ampulla → tube foot (28.5.72)."),
                ("Echinoderm larvae are ... symmetrical; adults are ...", "Bilateral; radial (28.5.69)."),
            ]},
        ],
    },
    "look_up": [
        "Species counts (sponges, mollusks, rotifers, spiders, scorpions) and sizes: the slides.",
        "Parasites and their hosts: the Parasites table.",
        "Labels on anatomy figures (clam, earthworm, crayfish, grasshopper, rotifer, sea star): the slides' figure "
        "descriptions.",
        "Which insect order is which: 28.4.65.",
    ],
}

# ======================================================================== Ch 29
QUICK_GUIDE[29] = {
    "intro": [
        "**What this chapter is about.** The chordates, our own phylum, from small sea creatures with no backbone "
        "up to the mammals. Read it as a story of new features. Each one opened a new way of life: a backbone, then "
        "jaws, then lungs and limbs for land, then an egg that doesn't need water, then hair and milk (29.1.8, "
        "29.2.12).",
        "**Where it fits.** Chordates are deuterostomes, like the echinoderms of Ch 28 (textbook p. 537). Most "
        "chordates are **vertebrates**, animals with a backbone (vertebral column); a few are not (29.1.5).",
        {"fig": (29, 8), "caption": "The chordate family tree, your map for the chapter. Each mark on a branch is a "
                                    "new feature shared by the groups above it: notochord → vertebrae → jaws → bony "
                                    "skeleton → lungs → 4 limbs → amniotic egg → mammary glands."},
    ],
    "sections": {
        1: [
            {"big": "Every chordate has four features at some stage of life. Sea squirts and lancelets keep them "
                    "without ever growing a backbone, which makes them clues to what the first chordates were like."},
            ("The four chordate characteristics", [
                "A stiff supporting rod along the back, just below the nerve cord: the **notochord** (Greek “back” + "
                "“string”) (29.1.3).",
                "A hollow nerve cord along the back: the **dorsal tubular nerve cord** (an arthropod's runs along the "
                "belly instead). Its front end becomes the brain in most chordates; in vertebrates the vertebrae "
                "protect it (29.1.3).",
                "Pockets in the throat region: **pharyngeal pouches**. They become gills in aquatic vertebrates, "
                "appear only in the embryo in most vertebrates, and are reshaped for other uses on land (29.1.3). "
                "Textbook: in humans the first pair becomes the auditory tubes (p. 537).",
                "A tail that extends past the anus: the **postanal tail**. In humans it disappears in the embryo "
                "(29.1.3).",
            ]),
            {"fig": (29, 4), "caption": "The four chordate characteristics: find the notochord, the nerve cord above "
                                        "it, the pharyngeal pouches and the tail past the anus."},
            ("Nonvertebrate chordates", [
                "In these, the notochord stays and is never replaced by a vertebral column (29.1.5).",
                "**Lancelets** (cephalochordates, Greek kephalo, “head”): small, segmented filter feeders in shallow "
                "seas. Adults keep all four characteristics (29.1.5, 29.1.6).",
                "**Sea squirts** (urochordates, also called tunicates): marine filter feeders whose adults have a "
                "thick covering, the **tunic**. The larva has all four traits, but the adult keeps only the gill "
                "slits (29.1.5, 29.1.7).",
                "Why they matter: many biologists think sea squirts are directly related to the vertebrates. A sea "
                "squirt larva may have become sexually mature without turning into the adult form, and evolved into "
                "a fishlike vertebrate (29.1.5).",
            ]),
            {"fig": (29, 6), "caption": "Lancelet: notochord, dorsal tubular nerve cord, gill slits; water exits by "
                                        "the atriopore."},
            {"fig": (29, 7), "caption": "Adult sea squirt: incurrent and excurrent siphons, tunic; the gill slits are "
                                        "its only chordate trait left."},
            ("Traps", [
                "Notochord = the rod; nerve cord = the nerves above it.",
                "Lancelets = cephalochordates; sea squirts = urochordates (tunicates).",
                "Myth: every chordate has a backbone. Fact: lancelets and sea squirts are chordates without one "
                "(29.1.5).",
            ]),
            {"check": [
                ("Name the four chordate characteristics.",
                 "Notochord, dorsal tubular nerve cord, pharyngeal pouches, postanal tail (29.1.3)."),
                ("Which chordate keeps only its gill slits as an adult?", "The sea squirt (29.1.7)."),
                ("What becomes of the pharyngeal pouches in a fish?", "Gills (29.1.3)."),
            ]},
        ],
        2: [
            {"big": "Vertebrates add a backbone and a skull to the chordate plan. Their history is a sequence of new "
                    "features, each opening a new way of life: jaws, then lungs and limbs, then the amniotic egg."},
            ("What vertebrates add", [
                "A **vertebral column** replaces the embryo's notochord. Its separate vertebrae show the body is "
                "segmented (29.2.9, 29.2.11).",
                "A skull encloses the brain, with a high degree of cephalization (brain and sense organs in the "
                "head) and complex sense organs (29.2.9).",
                "An endoskeleton (inside skeleton) of living tissue. Unlike an arthropod's exoskeleton, it grows with "
                "the animal. It protects organs, anchors muscles, and bears paired appendages: fins (a shark's "
                "pectoral and pelvic fins) or limbs (29.2.9, 29.3.18).",
                "A large coelom, a complete digestive tract (mouth and anus), closed circulation, gills or lungs, "
                "kidneys that regulate water, and separate sexes with sexual reproduction (29.2.10).",
            ]),
            {"fig": (29, 11), "caption": "The vertebrae grow around the notochord and neural tube and replace the "
                                         "notochord: compare the stages left to right."},
            ("Vertebrate evolution, in order", [
                "Chordates appear at the start of the Cambrian period, 542 MYA (million years ago). By the end of "
                "the Ordovician there were jawless and jawed fishes, the earliest vertebrates (29.2.12).",
                "Jaws, for catching prey: the **gnathostomes** (“jaw mouths”) are the jawed fishes plus the other "
                "vertebrates descended from them (29.2.12).",
                "Lungs and a bony skeleton prepared fishes for land. **Tetrapods** (Greek “four feet”) have four "
                "limbs; amphibians evolved from bony fishes by the Devonian (29.2.12).",
                "**Amniotes** lay an **amniotic egg**, which surrounds the embryo in fluid. Why it matters: they can "
                "reproduce on land, away from water (29.2.12).",
            ]),
            ("Traps", [
                "Gnathostomes = jaws; tetrapods = four limbs; amniotes = amniotic egg.",
                "The vertebral column replaces the notochord, not the nerve cord.",
            ]),
            {"check": [
                ("What replaces the notochord in a vertebrate embryo?", "The vertebral column (29.2.9)."),
                ("Put in order: amniotic egg, jaws, four limbs.", "Jaws → four limbs → amniotic egg (29.2.12)."),
                ("Why does the amniotic egg matter?", "Animals can reproduce on land (29.2.12)."),
            ]},
        ],
        3: [
            {"big": "Fishes are the first vertebrates. Jaws came from gill arches; then fishes split into cartilage "
                    "skeletons (sharks, rays) and bone skeletons. One small bony group, the lobe-finned fishes, led "
                    "to land animals."},
            ("Fishes", [
                "The largest group of vertebrates: aquatic, breathe with gills, usually have fins and scales "
                "(29.3.13).",
                "Fishes with no jaws are **agnathans**. **Ostracoderms** were the earliest vertebrate fossils. Today's "
                "lampreys and hagfishes have no bony skeleton. The parasitic sea lamprey nearly wiped out the "
                "whitefish and trout of the Great Lakes (29.3.13, 29.3.14).",
                "Jawed fishes are **ectotherms** (Greek “outer” + “heat”): their body temperature depends on the "
                "environment. They have gills, a cartilage or bone endoskeleton, and scales (29.3.15).",
                "Jaws evolved from the first pair of **gill arches**, the supports between the gill slits of jawless "
                "fishes; the second pair became supports for the jaws (29.3.15, 29.3.16).",
                "**Placoderms**: extinct, armored jawed fishes of the Devonian, thought to be the ancestors of sharks "
                "and bony fishes (29.3.15).",
            ]),
            {"fig": (29, 14), "caption": "A lamprey, a jawless fish: a toothed oral disk instead of jaws, and seven "
                                         "pairs of gill slits."},
            {"fig": (29, 16), "caption": "Jaws evolved from gill arches: compare the 1st and 2nd gill arches with the "
                                         "jaws."},
            ("Cartilaginous fishes (Chondrichthyes)", [
                "Sharks, rays, skates and chimaeras: a skeleton of cartilage, not bone, and no gill cover (29.3.17).",
                "Senses for hunting: they detect electric currents in water, and sharks and rays have a **lateral "
                "line**, pressure-sensing cells along the sides that feel nearby movement (29.3.17; textbook "
                "p. 541).",
                "Some are filter feeders, some predators. Rays and skates have huge, winglike pectoral fins and "
                "bodies flattened from back to belly (29.3.17, 29.3.19).",
            ]),
            {"fig": (29, 19), "caption": "Blue-spotted stingray: pectoral fins enlarged into wings along a flattened "
                                         "body; spiracles behind the eyes; a spined tail."},
            ("Bony fishes (Osteichthyes)", [
                "A skeleton of bone; the majority of living vertebrates (29.3.20; textbook p. 542).",
                "Most are **ray-finned fishes**, with fins held up by thin bony rays (29.3.20, 29.3.21).",
                "**Lobe-finned fishes** are a small group with fleshy fins supported by central bones (29.3.20).",
                "A bony flap, the **operculum**, covers the gills, so there are no external gill slits. A gas-filled "
                "sac, the **swim bladder**, changes the fish's buoyancy, so it can float higher or lower, like an "
                "adjustable float (29.3.20).",
                "Separate sexes; most use **external fertilization**, where eggs and sperm meet in the water (29.3.20).",
                "Why lobe-finned fishes matter: they gave rise to the amphibians. Living ones: lungfishes, with "
                "lungs as well as gills, and the coelacanth, caught in 1938 after being thought extinct (29.3.22, "
                "29.3.23).",
            ]),
            {"fig": (29, 21), "caption": "A typical ray-finned fish (soldierfish, with the swim bladder and lateral "
                                         "line labeled) and the variety of ray-finned fishes."},
            ("Traps", [
                "Agnathans = jawless; placoderms = extinct jawed fishes.",
                "Cartilaginous fishes have no operculum; bony fishes do.",
                "Ray-finned = most fishes; lobe-finned = the line that led to amphibians.",
                "Myth: the coelacanth is extinct. Fact: one was caught in 1938 (29.3.22).",
            ]),
            {"check": [
                ("Jaws evolved from which structures?", "The first pair of gill arches (29.3.15)."),
                ("A fish with a cartilage skeleton and no gill cover belongs to which group?",
                 "Cartilaginous fishes (Chondrichthyes) (29.3.17)."),
                ("What does a swim bladder do?", "Changes buoyancy (29.3.20)."),
                ("Which fishes gave rise to amphibians?", "Lobe-finned fishes (29.3.22)."),
            ]},
        ],
        4: [
            {"big": "Amphibians are the first vertebrates on land, but only halfway: they breathe air as adults yet "
                    "still return to water to reproduce. Their hearts also show the step from one blood loop to two."},
            ("Amphibians (Greek amphibios, “living both on land and in water”)", [
                "Frogs, toads, salamanders, newts and caecilians; most are tetrapods with limbs (29.4.24).",
                "Smooth, nonscaly skin; lungs in most adults; a double-loop circulation with a three-chambered "
                "heart; sense organs tuned for land; ectotherms (29.4.24).",
                "Reproduction in water, then metamorphosis: a tadpole with gills becomes an air-breathing adult "
                "(29.4.24; textbook p. 544).",
            ]),
            ("Circulation compared", [
                "Fishes: a **single loop** with a two-chambered heart. Blood goes heart → gills → body → back to the "
                "heart (29.4.25).",
                "Amphibians and most reptiles: a **double loop**, one circuit to the lungs and one to the body, with a "
                "three-chambered heart (29.4.25).",
                "Crocodilians, birds and mammals: a **four-chambered heart** sends oxygen-poor blood to the lungs and "
                "oxygen-rich blood to the body, without mixing (29.4.25).",
            ]),
            {"fig": (29, 25), "caption": "Single loop (fishes), double loop with a three-chambered heart, and the "
                                         "four-chambered heart: follow the colors for oxygen-rich and oxygen-poor "
                                         "blood."},
            ("From fins to legs", [
                "Two hypotheses: lobe-finned fishes could move pond to pond on their fins, or food on land and no "
                "predators favored life on land (29.4.26).",
                "A fossil intermediate between two groups is a **transitional fossil**. Tiktaalik roseae sits "
                "between lobe-finned fishes and tetrapods with limbs, and shows how legs arose (29.4.26).",
                "The same bones (humerus, radius, ulna; femur, tibia, fibula) appear in the fins and in the limbs "
                "(29.4.27).",
            ]),
            {"fig": (29, 27), "caption": "Fin bones of a transitional form compared with the limb bones of an "
                                         "ancestral amphibian: match each bone."},
            ("Living amphibians: three groups", [
                "Salamanders and newts: tails; salamanders use internal fertilization (29.4.28).",
                "Frogs and toads: no tail as adults (29.4.28).",
                "Caecilians: legless, often blind, worm-shaped burrowers (29.4.28, 29.4.29).",
            ]),
            ("Animals in medicine", [
                "Snake venom gives pain medications; goats engineered to make drugs in their milk; pigs altered to "
                "supply hearts for transplants (29.4.30).",
            ]),
            ("Traps", [
                "Three-chambered heart = amphibians (and most reptiles); four = crocodilians, birds, mammals.",
                "Tiktaalik is a fossil fish-tetrapod, not a living amphibian.",
                "Myth: caecilians are worms or snakes. Fact: they are legless amphibians (29.4.28).",
            ]),
            {"check": [
                ("Why are amphibians only partly adapted to land?",
                 "Most reproduce in water, and their young (tadpoles) have gills (29.4.24; textbook p. 544)."),
                ("How many chambers does an amphibian heart have, and how many loops?", "Three; two (29.4.24)."),
                ("What does Tiktaalik show?",
                 "A transitional fossil between lobe-finned fishes and tetrapods: how legs arose (29.4.26)."),
            ]},
        ],
        5: [
            {"big": "Reptiles, birds included, are fully adapted to land: waterproof skin, efficient lungs, and the "
                    "shelled amniotic egg. Skull openings sort the amniotes into three lines, one of which leads to "
                    "mammals."},
            ("Reptiles (class Reptilia), birds included", [
                "More than 20,000 species. Paired limbs; thick, scaly skin that water can't pass through; lungs "
                "with an expandable rib cage; well-developed kidneys; ectotherms (29.5.31).",
                "A ventricle partly or fully divided by a **septum**, a wall that reduces or stops the mixing of "
                "oxygen-rich and oxygen-poor blood (29.5.31; textbook pp. 546–547).",
                "Reproduction fit for land: internal fertilization and a shelled amniotic egg (29.5.31).",
                "Inside the egg, the **amnion** holds fluid around the embryo, a “private pond” that keeps it from "
                "drying out. The chorion exchanges gases, the allantois stores wastes, and the yolk sac feeds the "
                "embryo (29.5.36 caption; textbook p. 547, Fig. 29.15).",
            ]),
            {"fig": (29, 36), "caption": "Living reptiles, and the amniotic egg (f): find the amnion, chorion, "
                                         "allantois and yolk sac."},
            ("Three amniote lineages, told apart by skull openings", [
                "Amniotes evolved from amphibian ancestors by the Carboniferous period (29.5.33).",
                "Count the openings behind the eye socket (orbit):",
                "No opening, an **anapsid** skull: turtles. A modern view makes them specialized diapsids; this is "
                "still debated (29.5.33).",
                "Two openings, a **diapsid** skull: the other reptiles, birds included (29.5.33).",
                "One opening, a **synapsid** skull: mammals (29.5.33).",
            ]),
            {"fig": (29, 34), "caption": "The amniote family tree: synapsids (to mammals), anapsids (turtles), "
                                         "diapsids (lizards, snakes, tuataras, crocodilians, dinosaurs, birds)."},
            ("Living reptiles", [
                "Turtles and tortoises: ribs and thoracic vertebrae fused into a heavy shell; a sharp beak, no teeth "
                "(29.5.35).",
                "Lizards: most have four clawed feet; carnivores (29.5.35).",
                "Snakes: lost their limbs as an adaptation for burrowing; carnivores; some venomous (29.5.35).",
                "Tuataras: a “third eye”; the last member of an ancient group that included the ancestor of lizards "
                "and snakes (29.5.35).",
                "Crocodilians: long, powerful jaws; a muscular tail used as a weapon and a paddle (29.5.35).",
            ]),
            ("Birds: reptiles built for flight", [
                "Birds evolved from dinosaurs, as a plentiful fossil record shows (29.5.37).",
                "Feathers are modified reptilian scales (29.5.37).",
                "A light, rigid skeleton: fused bones (the collarbone included) and a **keel** on the sternum "
                "(breastbone), where the flight muscles attach (29.5.37, 29.5.38).",
                "Lungs connected to air sacs; **endothermy**, a body that makes its own heat; acute vision and "
                "instinctual behavior (29.5.37).",
                "Most fly (eagles, geese); some are flightless (emus, penguins, kiwis, ostriches). Birds are "
                "classified by beak and foot type, habitat and behavior (29.5.39, 29.5.40).",
            ]),
            {"fig": (29, 38), "caption": "Bird anatomy (air sacs, crop, gizzard) and an eagle skeleton with the keeled "
                                         "sternum."},
            {"fig": (29, 40), "caption": "Beaks fit the food: tearing prey (eagle), chiseling wood (woodpecker), "
                                         "prying open nuts (macaw), cracking seeds (cardinal)."},
            ("Traps", [
                "Anapsid = 0 openings (turtles), diapsid = 2 (other reptiles, birds), synapsid = 1 (mammals).",
                "Myth: birds aren't reptiles. Fact: they are reptiles, descended from dinosaurs; unlike other "
                "reptiles they are endotherms (29.5.31, 29.5.37).",
                "Amnion = the fluid sac around the embryo, not the shell.",
            ]),
            {"check": [
                ("A skull with two openings behind the eye socket belongs to which amniotes?",
                 "Diapsids: reptiles other than turtles, including birds (29.5.33)."),
                ("What part of the amniotic egg keeps the embryo from drying out?", "The amnion (29.5.36)."),
                ("Where do a bird's flight muscles attach?", "The keel of the sternum (29.5.37)."),
            ]},
        ],
        6: [
            {"big": "Mammals add hair and milk. They lived alongside the dinosaurs as a minor group and spread out "
                    "after them. Three living lines differ in how the young develop: eggs, a pouch, or a placenta."},
            ("Mammals (class Mammalia)", [
                "Hair and milk-producing **mammary glands** (29.6.41).",
                "A skull that holds a larger brain for the body's size, and **differentiated teeth**: different shapes "
                "for different jobs (29.6.41).",
                "Efficient breathing and circulation: a double loop with a four-chambered heart. Kidneys that save "
                "water; a highly developed nervous system; internal development in most (29.6.41).",
            ]),
            ("Mammal evolution", [
                "Mammals share an amniote ancestor with reptiles; their immediate ancestors had a synapsid skull "
                "(29.6.42).",
                "The first true mammals appeared in the Triassic and lived alongside the dinosaurs. The common "
                "ancestor of all mammal groups lived about 220 MYA (29.6.42).",
                "Monotremes are the earliest group. Placental mammals later spread into the habitats the dinosaurs "
                "had held, an **adaptive radiation**: many new species evolving from one ancestor into new habitats "
                "(29.6.42).",
            ]),
            {"fig": (29, 43), "caption": "The mammal family tree: monotremes branch off first; marsupials and "
                                         "placentals share live birth and a true uterus."},
            ("The three living lineages", [
                "**Monotremes** (Greek “one hole”), e.g. the duckbill platypus: lay hard-shelled amniotic eggs; one "
                "urogenital opening, the **cloaca** (29.6.44, 29.6.45).",
                "**Marsupials** (Greek marsupium, “pouch”), e.g. koala, opossum: the tiny newborn keeps developing in "
                "the female's pouch (29.6.44, 29.6.45).",
                "**Placental mammals**: the **placenta** passes nutrients and wastes between the mother's blood and "
                "the fetus's blood (29.6.44; textbook p. 553).",
                "Placental orders are in the table at 29.6.46. Examples: Cetacea (whales), Artiodactyla (even-toed: "
                "cattle, deer), Perissodactyla (odd-toed: horses), Chiroptera (bats), Rodentia (one pair of "
                "ever-growing incisors), Lagomorpha (rabbits: two pairs), Primates (opposable thumb) (29.6.46).",
            ]),
            {"fig": (29, 45), "caption": "A monotreme (duckbill platypus) and two marsupials (koala, opossum)."},
            ("Traps", [
                "Monotremes = eggs; marsupials = pouch; placentals = placenta.",
                "Myth: in the placenta the mother's and fetus's blood mix. Fact: substances pass between them; the "
                "bloods don't mix (29.6.44; textbook p. 553).",
                "Rodents have one pair of ever-growing incisors, rabbits two.",
            ]),
            {"check": [
                ("Which mammals lay eggs?", "Monotremes, e.g. the duckbill platypus (29.6.44)."),
                ("What does the placenta exchange?",
                 "Nutrients and wastes between the mother's and the fetus's blood (29.6.44)."),
                ("Even-toed hoofed mammals such as cattle belong to which order?", "Artiodactyla (29.6.46)."),
            ]},
        ],
    },
    "look_up": [
        "Species counts and dates (MYA, periods): the slides and the Geologic order sequence.",
        "The placental orders: the table at 29.6.46.",
        "Fish and bird anatomy labels: the figure descriptions.",
    ],
}

# ======================================================================== Ch 30
QUICK_GUIDE[30] = {
    "intro": [
        "**What this chapter is about.** Where humans fit among the primates, then the fossils from the first "
        "upright walkers to modern humans. Two ideas carry it. Primates are built for life in trees. The human line "
        "walked upright first and grew a bigger brain later (30.1.3, 30.2.20).",
        "**Get the group names straight first; questions often turn on them.** **Primates**: lemurs, monkeys, "
        "apes and humans. **Hominids**: the great apes (orangutans, gorillas, chimpanzees) and humans. "
        "**Hominins**: humans and the species very closely related to them, our extinct close relatives (30.1.3, "
        "30.1.11; textbook p. 570). Each group is nested inside the one before.",
    ],
    "sections": {
        1: [
            {"big": "Primate features are adaptations for life in trees: grasping hands, forward-facing eyes, a big "
                    "brain, few babies. DNA shows chimpanzees are our closest living relatives, cousins rather than "
                    "ancestors."},
            ("Primates (Latin primus, “first”) and their trends", [
                "Primates are an order of mammals: prosimians, monkeys, apes and humans. Most live in trees "
                "(**arboreal**) (30.1.3).",
                "Their evolution trends toward mobile limbs, grasping hands, a flattened face, stereoscopic vision, "
                "a large complex brain and a reduced reproductive rate (30.1.3).",
            ]),
            {"fig": (30, 4), "caption": "Primate diversity: prosimian, New and Old World monkeys, Asian and African "
                                        "apes, hominins."},
            ("Limbs and hands: built to grip branches", [
                "Hands and feet adapted for grasping and holding are **prehensile**. Most primates have flat nails "
                "instead of claws, and sensitive pads on the fingers and toes (30.1.5).",
                "A thumb that can touch each of the other fingers is an **opposable thumb**: a grip both powerful and "
                "precise. Many primates have one. Except for humans, primates with opposable thumbs also have "
                "opposable toes (30.1.5).",
                "Why it matters in trees: mobile limbs and clawless digits let primates grasp and release branches "
                "and bring food to the mouth (30.1.5).",
            ]),
            {"fig": (30, 6), "caption": "From a tree shrew's claws to the human hand's long, opposable thumb."},
            ("Vision: judging the jump to the next branch", [
                "Both eyes face forward and see the same scene from slightly different angles. The brain combines "
                "the two views into a 3-D image with good depth perception: **stereoscopic vision** (30.1.7, "
                "30.1.8).",
                "Why it matters: it lets a primate judge the distance and position of the next branch (30.1.7).",
                "Color vision comes from **cone cells** (need bright light; sharp, colored image), alongside **rod "
                "cells** (work in dim light; blurry, gray image). Humans and apes have three kinds of cones: greens, "
                "blues and reds (30.1.7).",
            ]),
            {"fig": (30, 8), "caption": "Stereoscopic vision: with the snout reduced and both eyes at the front, "
                                        "their fields overlap (the binocular field), giving depth perception."},
            ("Brain and reproduction", [
                "A larger, more complex brain. In apes and humans the smell area is smaller and the sight area "
                "larger; more brain controls the hands (hand-eye coordination), and more handles communication for "
                "living in social groups (30.1.9).",
                "A reduced reproductive rate: later maturity, longer lives, a long pregnancy that gives the forebrain "
                "time to develop, usually one baby at a time, and a long childhood of learning (30.1.10).",
                "Why one baby at a time: it is hard to carry and care for several in the trees (textbook p. 558).",
            ]),
            ("Who is related to whom", [
                "Humans' closest relatives are the chimpanzees; the two shared a common ancestor 5–7 MYA (30.1.11).",
                "**Anthropoids** (Greek “human-like”) are the hominids, gibbons, Old World monkeys and New World monkeys "
                "(30.1.12).",
                "Old World monkeys (Africa, Asia): no grasping tail, protruding noses; e.g. baboons and rhesus "
                "monkeys, used in medical research (30.1.12).",
                "New World monkeys (South America): often long prehensile tails, flat noses; e.g. the spider monkey "
                "and the capuchin (30.1.12).",
                "**Prosimians** (Latin “before apes”: lemurs, tarsiers) were the first primates to branch off. The "
                "common ancestor of all primates lived about 55 MYA and may have looked like today's tree shrews "
                "(30.1.17).",
            ]),
            {"fig": (30, 13), "caption": "The primate family tree: prosimians branch off first, then New World "
                                         "monkeys, Old World monkeys, gibbons, orangutans, gorillas, and last "
                                         "chimpanzees and humans."},
            ("Fossil apes", [
                "Primate fossils like monkeys appear in Africa about 45 MYA. New World monkeys' ancestors reached "
                "South America about 40 MYA, though how they crossed the Atlantic is uncertain (30.1.14).",
                "Proconsul (about 35 MYA) is the best link between monkeys, gibbons and early hominids: "
                "baboon-sized, with a 165 cc brain and no tail. It walked on all fours on top of branches, like a "
                "monkey (30.1.14, 30.1.15).",
                "Proconsul probably led to the **dryopithecines**, fossil apes. About 10 MYA, Africa and Arabia joined Asia, and apes "
                "spread into Europe and Asia (30.1.16).",
                "Dryopithecus (9.5 MYA, Spain) swung from branch to branch, like today's gibbons (30.1.16).",
            ]),
            {"fig": (30, 15), "caption": "Monkey vs Proconsul: sort Proconsul's features into monkeylike and "
                                         "apelike."},
            ("Genes: humans vs chimpanzees", [
                "Different chromosome numbers (textbook: chimpanzees 48, humans 46), yet close relatives: human "
                "chromosome 2 is two chimpanzee chromosomes fused end to end (30.1.18, 30.1.19).",
                "Similar patterns of **transposons** (DNA pieces that can move in the genome, such as Alu) and "
                "**pseudogenes** (broken copies of old genes). The DNA base sequences differ by only 1.5% (30.1.18, "
                "30.1.19).",
                "Why shared transposons are evidence: they land in random places, so the same places in two species "
                "point to a shared ancestor (30.1.19; textbook p. 560).",
                "Differences in noncoding DNA kept by each species may explain the differences in anatomy "
                "(30.1.18).",
                "Great apes and humans used to be classified in different families; this genetic evidence is why "
                "they are now grouped together as hominids (30.1.18; textbook p. 560).",
            ]),
            {"fig": (30, 19), "caption": "Human chromosome 2 = chimpanzee chromosomes 2A + 2B fused; Alu elements in "
                                         "the same places in both."},
            ("Traps", [
                "Hominins (humans and close extinct relatives) vs hominids (also the great apes).",
                "Stereoscopic vision = depth perception; color vision = cone cells.",
                "Proconsul walked on top of branches; Dryopithecus swung below them.",
                "Myth: humans evolved from chimpanzees (or monkeys or apes). Fact: we share a common ancestor with "
                "them, 5–7 MYA for chimpanzees (30.1.11).",
            ]),
            {"check": [
                ("What does stereoscopic vision give a primate, and why does it matter in trees?",
                 "Depth perception; judging the distance to the next branch (30.1.7)."),
                ("Are gorillas hominins or hominids?", "Hominids, not hominins (30.1.11)."),
                ("Which fossil walked on top of branches like a monkey but had no tail?", "Proconsul (30.1.14)."),
                ("Which human chromosome is two chimpanzee chromosomes fused?", "Chromosome 2 (30.1.19)."),
            ]},
        ],
        2: [
            {"big": "The first hominins walked upright long before their brains grew. Ardi (4.4 MYA) mixed upright "
                    "walking with tree climbing; the australopiths walked upright with ape-sized brains."},
            ("How to recognize a hominin fossil", [
                "Walking upright on two feet is **bipedalism**; apes walk on all fours (**quadrupedal**). Early "
                "humanlike hominins aren't in the genus Homo, but walking upright places them on our side (30.2.20).",
                "Why upright helps: it frees the hands for tool use (30.2.20).",
                "The skull: modern humans have a flatter face, a more pronounced chin, a shorter jaw, smaller teeth, "
                "and a bigger brain (chimpanzee about 400 cc, modern human 1,360 cc) (30.2.20).",
            ]),
            {"fig": (30, 21), "caption": "Timeline of hominins: how long each species lasted (million years ago, MYA). "
                                         "Notice how several lived at the same time."},
            ("Ardipithecines: Ardi", [
                "Two species: Ardipithecus kadabba (5.8–5.2 MYA, only teeth and bits) and A. ramidus (4.4 MYA, over "
                "100 skeletons, Ethiopia). In 2009 a female skeleton, Ardi, was reconstructed (30.2.22).",
                "Ardi walked upright but spent a lot of time in trees (30.2.23).",
                "Upright features: the spine leaves the center of the skull, the femurs angle in toward the knees, "
                "a broad pelvis, knees built to carry the weight, and a foot bone that apes lack (30.2.23, 30.2.24).",
                "Apelike features: an opposable big toe and flexible wrists for moving carefully along branches; "
                "chimpanzee-sized, a 300–350 cc brain, a forward-projecting face, small teeth with no sharp canines "
                "(soft plant food) (30.2.23, 30.2.25).",
                "About 120 cm (4 ft) tall. Males and females were about the same size, unlike the australopiths, "
                "whose males were larger (30.2.25, 30.2.27).",
                "The old idea was that bipedalism evolved when grassland replaced the forests of East Africa. Ardi "
                "lived in the woods, which questions it. In a forest, walking upright may have helped carry infants "
                "and helped males forage on the forest floor (30.2.26).",
            ]),
            {"fig": (30, 24), "caption": "Adaptations for walking erect, in a modern human and in Ardi: compare the "
                                         "pelvis, the angle of the femurs and the big toe."},
            ("Australopithecines (australopiths)", [
                "Lived in Africa from 4 MYA to 1.5 MYA (30.2.27).",
                "A small, apelike brain (370–515 cc) but an upright, humanlike walk. Body parts that change at "
                "different rates and times show **mosaic evolution** (30.2.27).",
                "Slender (**gracile**) types are genus Australopithecus. Powerful (**robust**) types, with massive "
                "jaws and big grinding teeth, are genus Paranthropus. Males were larger than females (30.2.27).",
                "Some ate meat and used stone tools to scrape it from bones (30.2.27).",
                "East Africa: Australopithecus afarensis, including Lucy (bipedal, low forehead, large canines, small "
                "brain, arms longer than legs). It is considered closer to early Homo than the southern species "
                "(30.2.28, 30.2.29).",
                "Southern Africa: A. africanus, Paranthropus robustus, and A. sediba, which may have been a direct "
                "ancestor of Homo (30.2.29).",
            ]),
            {"fig": (30, 28), "caption": "Lucy (Australopithecus afarensis) and fossil footprints left by bipedal "
                                         "walkers."},
            ("Traps", [
                "Myth: the big brain came first. Fact: upright walking came first; the brain stayed small for "
                "millions of years (mosaic evolution) (30.2.27).",
                "Gracile = Australopithecus; robust = Paranthropus.",
                "Ardi (Ardipithecus, 4.4 MYA) is older than Lucy (Australopithecus afarensis).",
            ]),
            {"check": [
                ("Name two skeleton features that show Ardi walked upright.",
                 "The spine leaves the center of the skull; femurs angle in; broad pelvis; a foot bone apes lack "
                 "(30.2.23)."),
                ("What is mosaic evolution? Give the australopith example.",
                 "Body parts evolving at different rates: a small brain with an upright walk (30.2.27)."),
                ("Gracile or robust: which had massive jaws, and what genus is it?", "Robust; Paranthropus (30.2.27)."),
            ]},
        ],
        3: [
            {"big": "Early Homo had bigger brains (600 cc or more) and used tools. Homo erectus was the first to "
                    "leave Africa."},
            ("Early Homo (Latin homo, “man”)", [
                "Appears about 2.5 MYA: brains of 600 cc or more, jaws and teeth like ours, and tool use (30.3.30).",
                "Homo habilis (“handyman”) and H. rudolfensis may be one species. They may have been the first "
                "hominins to use stone tools (30.3.31).",
                "They were socially organized scavengers. Small cheek teeth show they ate both meat and plants "
                "(omnivores) (30.3.31).",
            ]),
            ("Homo erectus (Latin “upright”), with H. ergaster", [
                "Often treated as one species, H. erectus. First in Africa about 1.9 MYA, from H. habilis or an "
                "earlier ancestor (30.3.32).",
                "A larger brain, rounder jaw and big brow ridges (30.3.32).",
                "A projecting nose: why it helped, it keeps water in the body in a hot, dry climate (30.3.32).",
                "Much taller (males 1.8 m), with a gait like ours. The size of the birth canal shows babies were "
                "born premature and needed a long period of care (30.3.33).",
                "The first species to migrate into Europe and Asia (between 2.5 and 1 MYA). It knew fire and may "
                "have been the first to cook meat (30.3.33, 30.3.34).",
                "When it died out is debated: most estimates say several hundred thousand years ago, newer evidence "
                "100,000 years ago (30.3.35).",
            ]),
            {"fig": (30, 34), "caption": "Homo erectus leaves Africa: dates of the earliest fossils in each region."},
            ("Traps", [
                "H. habilis = handyman, first stone tools, scavenger; H. erectus = migration, fire, tall.",
                "Myth: modern humans were the first to leave Africa. Fact: H. erectus left first (30.3.33).",
            ]),
            {"check": [
                ("Which species first left Africa, and what did it know how to use?", "Homo erectus; fire (30.3.33)."),
                ("What does “habilis” mean, and why the name?",
                 "Handyman; it may have been the first to use stone tools (30.3.31)."),
                ("How did H. erectus's nose suit its climate?",
                 "It keeps water in the body in a hot, dry climate (30.3.32)."),
            ]},
        ],
        4: [
            {"big": "Homo heidelbergensis split into three lines: Africa (us), Asia (Denisovans) and Europe "
                    "(Neanderthals). The main hypothesis, the replacement model, says modern humans arose in Africa "
                    "and replaced the others."},
            ("Toward modern humans", [
                "Most researchers think Homo sapiens (Latin “wise man”) evolved from an H. erectus line in Africa, "
                "but they disagree on when (30.4.37).",
                "Homo heidelbergensis replaced H. erectus in Africa about 500,000 years ago. It had a larger brain, "
                "better tools and social behavior, and probably the first shelters. It is the most likely line to "
                "modern humans (30.4.38, 30.4.39).",
                "Between 700,000 and 200,000 years ago H. heidelbergensis split into three lines: Africa → modern H. "
                "sapiens; Asia → the Denisovans; Europe → the Neanderthals. Some modern humans carry DNA from all "
                "three (30.4.39).",
                "Homo floresiensis, a dwarf species from an island, is one of the lines that split off H. erectus "
                "in Asia (30.4.38).",
            ]),
            ("Two hypotheses", [
                "The **replacement (out-of-Africa) model**, the main one: modern humans evolved from **archaic humans** "
                "(earlier Homo species) only in Africa. Then they migrated to Asia and Europe and replaced the earlier Homo species about "
                "100,000 years BP (before the present) (30.4.40).",
                "Its evidence: the earliest modern human remains are in Africa (in Asia not until 100,000 years BP, "
                "in Europe 60,000). African mitochondrial DNA is the most diverse, as expected if humans have lived "
                "there longest (30.4.40, 30.4.41).",
                "The **multiregional continuity hypothesis**: modern humans arose from earlier Homo in the same way "
                "in Africa, Asia and Europe, with genetic continuity in each region (30.4.43).",
                "New finds (H. floresiensis, H. naledi, the Denisovans) bring it back into discussion, maybe as a mix "
                "of both models (30.4.43).",
                "One way to picture it: in the replacement model, one population spreads out of Africa and takes "
                "over; in the multiregional model, each region's population becomes modern where it lives.",
            ]),
            {"fig": (30, 42), "caption": "The replacement model: modern humans spread from Africa and replace the "
                                         "earlier species in Asia and Europe."},
            ("Neanderthals (Homo neanderthalensis)", [
                "Lived from over 400,000 to 30,000 years ago in Europe and Asia; descended from H. heidelbergensis "
                "migrants out of Africa (30.4.44, 30.4.46).",
                "A slightly larger brain than ours (1,400 cc vs 1,360 cc), massive brow ridges, wide flat noses, a "
                "receding jaw (30.4.45).",
                "Short, thick bones and heavy muscles: a sturdy build that saved heat in the Ice Age (30.4.45).",
                "Culturally advanced: caves or shelters, stone spear points, scrapers and knives, hunting large "
                "animals, control of fire, and burials with flowers and tools (30.4.47).",
                "Why they died out is debated: conflict with H. sapiens, diseases brought by H. sapiens, losing the "
                "competition for food, or unrelated causes (30.4.46).",
            ]),
            ("Cro-Magnons", [
                "The oldest fossils classified as H. sapiens. They left Africa for Asia and Europe about 100,000 "
                "years ago, interbred with Neanderthals and Denisovans, and reached western Europe 40,000 years ago "
                "(30.4.48).",
                "Modern-looking: lighter bones, a high flat forehead, a domed skull with a 1,590 cc brain, small "
                "teeth, a distinct chin (30.4.48).",
                "Hunter-gatherers with compound tools, blades and spears that killed from a distance. They may have "
                "caused the **Pleistocene overkill**, the extinction of many large mammals (30.4.49).",
                "Their brain may have allowed a full language. Their art (sculptures, cave paintings) shows the "
                "symbolic thinking that speech needs (30.4.50).",
                "Agriculture: full dependence on crops and domestic animals came about 4,500 years ago, perhaps "
                "forced by the loss of big game and climate change (30.4.51).",
                "Agriculture sped up **biocultural evolution**, in which natural selection acts on cultural "
                "achievements (30.4.51).",
            ]),
            ("Human variation", [
                "Some differences are adaptations to local conditions (30.4.53).",
                "Skin color: dark skin protects against strong UV light; light skin still makes vitamin D where UV "
                "is weak (30.4.53).",
                "**Bergmann's rule**: animals in colder regions have bulkier bodies. **Allen's rule**: shorter limbs, "
                "fingers and ears in the cold. Why: both change the surface-area-to-volume ratio, and less surface "
                "for the volume loses less heat (30.4.53; textbook p. 569).",
                "Example: the slim, long-limbed Maasai of East Africa vs the stockier Inuit of the Arctic (30.4.52 "
                "caption).",
                "The replacement model also explains ethnic groups: all modern humans share a recent common ancestor "
                "(Cro-Magnon) who evolved in Africa, and modern populations vary less than archaic ones did "
                "(30.4.54).",
                "Mitochondrial DNA points to a common ancestor no more than a million years ago. Lewontin's study of "
                "17 genes in seven groups found that most genetic variation is within groups, not between them "
                "(30.4.54).",
            ]),
            {"fig": (30, 52), "caption": "Ethnic groups: the slim, long-limbed Maasai of East Africa and the stockier "
                                         "Inuit of the Arctic illustrate Bergmann's and Allen's rules."},
            ("Traps", [
                "Replacement = Africa only, then spread; multiregional = in parallel in Africa, Asia and Europe.",
                "Myth: Neanderthals had smaller brains than ours. Fact: slightly larger, 1,400 cc vs 1,360 cc "
                "(30.4.45).",
                "Denisovans = Asian line; Neanderthals = European line; H. sapiens = African line.",
                "Bergmann = bulkier body; Allen = shorter limbs and ears.",
                "Myth: human ethnic groups differ a lot genetically. Fact: most variation is within groups, not "
                "between them (30.4.54).",
            ]),
            {"check": [
                ("What evidence supports the replacement model?",
                 "Earliest modern remains in Africa; African mitochondrial DNA most diverse (30.4.40–41)."),
                ("Which lineage of H. heidelbergensis became the Neanderthals?", "The European one (30.4.39)."),
                ("Bulkier bodies in cold climates: whose rule?", "Bergmann's (30.4.53)."),
                ("What is the Pleistocene overkill?",
                 "The extinction of many large mammals, possibly from Cro-Magnon hunting (30.4.49)."),
            ]},
        ],
    },
    "look_up": [
        "Each species' dates and brain size: the Hominins and Brain sizes tables.",
        "Migration dates: 30.3.34 and 30.4.42.",
        "Proconsul's monkeylike and apelike features: 30.1.15.",
    ],
}
