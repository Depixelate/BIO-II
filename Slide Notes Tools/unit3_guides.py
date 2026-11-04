"""Unit 3 quick guides (Ch 28-30), merged into quick_guides.QUICK_GUIDE.

Same format as quick_guides.py, plus figures for the illustrated reading copy: an item can also be
    {"fig": (chapter, slide), "caption": "..."}            the picture on that slide
    {"book": page, "clip": (x0, y0, x1, y1), "caption": "..."}   a textbook figure: book page, crop in PDF points
The printable copy leaves the figures out and turns every slide code into chapter.page.slide (main-notes pages).
Unit 3 guides are fuller than Unit 2's (the user's request, Nov 4): written for someone who hasn't read the chapter,
every term explained where it first appears, every organism placed in its group, and the diagrams that the concepts
need.
"""

QUICK_GUIDE = {}

# ======================================================================== Ch 28
QUICK_GUIDE[28] = {
    "intro": [
        "This chapter is a tour of the invertebrates: animals without a backbone (28.1.3). It first explains what "
        "makes an animal and the few features biologists use to sort animals into groups. Then it visits the groups "
        "in evolutionary order, from the simplest (sponges) to the sea stars, the invertebrates most closely related "
        "to us.",
        "Animals are multicellular and heterotrophic: they must get food from outside, and unlike fungi (which digest "
        "food outside the body and absorb it), animals eat their food and digest it inside (28.1.3). Many reproduce "
        "sexually, some asexually, some both; many have a diploid life cycle (28.1.3). Animals descend from a single "
        "common ancestor; they split into invertebrates and vertebrates, animals that at some stage have a spinal "
        "cord (backbone) (28.1.3).",
        "Four features sort the groups, so learn them first: symmetry (the body's shape pattern), germ layers (how "
        "many tissue layers the embryo makes), the body cavity (coelom), and protostome vs deuterostome development "
        "(which embryo opening becomes the mouth) (28.1.8, 28.1.9, 28.1.11).",
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
            ("Where animals came from", [
                "The colonial flagellate hypothesis: animals descend from an ancestor that looked like a hollow ball "
                "of cells, each with a flagellum (a whip-like tail for moving) (28.1.5).",
                "Choanoflagellates are single-celled protists (not animals) with a flagellum; among protists they "
                "look most like the last single-celled ancestor of animals (28.1.5).",
                "The steps: a few flagellated cells clumped together into a hollow sphere, some cells specialized, "
                "and two tissue layers formed when cells folded inward (28.1.5, 28.1.6). The evidence: sponges have "
                "choanocytes, cells that look like choanoflagellates (28.1.6).",
                "An alternative hypothesis: the ancestor was a cell whose life cycle already had several cell "
                "types; sponges' archaeocytes, cells that can become other cell types, are its evidence (28.1.6).",
                "Today's body plans were already present by the Cambrian period. Small changes in DNA and in Hox "
                "(homeotic) genes, genes that control how the body is laid out during development, may explain the "
                "differences (28.1.7).",
            ]),
            {"fig": (28, 6), "caption": "Two hypotheses for how the first animals (sponges) arose from single cells."},
            ("Symmetry", [
                "Asymmetry: no particular body shape (sponges) (28.1.8).",
                "Radial symmetry: the body is arranged around a center like a wheel, so any cut through the center "
                "gives identical halves (jellyfish). It lets the animal reach out in all directions from one center "
                "(28.1.8, 28.1.10).",
                "Bilateral symmetry: a definite right and left half, so only one cut works (a turtle). These animals "
                "tend to be active and move forward head first, so the brain and sense organs gather at the front: "
                "cephalization (28.1.8).",
            ]),
            {"fig": (28, 10), "caption": "Radial symmetry (jellyfish: many planes) vs bilateral symmetry (turtle: "
                                         "one plane)."},
            ("Germ layers", [
                "Germ layers are the first tissue layers in an embryo; they give rise to the organs (28.1.9).",
                "Diploblastic animals have two (ectoderm outside, endoderm inside): comb jellies and cnidarians. "
                "Triploblastic animals add a middle layer, the mesoderm, and build organs: the remaining groups in "
                "this chapter, from the lophotrochozoans on (28.1.9; textbook p. 511).",
            ]),
            ("Protostomes vs deuterostomes", [
                "Triploblastic animals are either protostomes (“first mouth”) or deuterostomes (“second mouth”) "
                "(28.1.9).",
                "Cleavage, cell division without growth, comes first. Protostomes: spiral cleavage, new cells sit "
                "at an angle; determinate, each cell has a fixed fate. Deuterostomes: radial cleavage, new cells "
                "sit on top; indeterminate, a separated cell can still become a whole embryo (28.1.11, 28.1.12).",
                "The blastula is the hollow ball of cells; it indents to make the first opening, the blastopore. In "
                "protostomes it becomes the mouth; in deuterostomes it becomes the anus and the mouth forms second "
                "(28.1.11, 28.1.12).",
                "The coelom is a body cavity completely lined by mesoderm (a “true coelom”). Some protostomes and "
                "the deuterostomes have one. Protostomes: it forms by a splitting of the mesoderm. Deuterostomes: "
                "by an outpocketing (pouches) of the primitive gut (28.1.11).",
                "Most invertebrates are protostomes (mollusks, annelids, arthropods...); the deuterostomes are the "
                "echinoderms and the chordates, including us (28.5.69; textbook p. 511).",
            ]),
            {"fig": (28, 12), "caption": "Protostomes vs deuterostomes: cleavage, fate of the blastopore, and how "
                                         "the coelom forms."},
            ("Traps", [
                "Protostome = blastopore becomes the mouth; deuterostome = it becomes the anus. Don't swap them.",
                "Spiral = protostomes, radial = deuterostomes: radial cleavage is not radial symmetry.",
                "Germ layers (embryo tissue layers) are not the coelom (a body cavity).",
            ]),
        ],
        2: [
            ("Sponges (phylum Porifera)", [
                "The simplest animals: no true tissues, only a cellular level of organization with a few cell types "
                "(28.2.13).",
                "The saclike body is full of pores. Collar cells (choanocytes) beat their flagella, pulling water "
                "in through the pores, into the central cavity and out the osculum, the opening at the top (28.2.13, "
                "28.2.14).",
                "A sponge is a sessile filter feeder: it stays attached in one place and strains food out of that "
                "water (28.2.13).",
                "Spicules, small needle-like pieces, and spongin fibers form its skeleton; amoebocytes carry "
                "nutrients from cell to cell (28.2.14; textbook p. 513).",
                "Reproduction: asexual by fragmentation or budding; sexual, making a flagellated larva that swims "
                "to a new place. Sponges regenerate a whole body from a small part (28.2.13).",
            ]),
            {"fig": (28, 14), "caption": "Sponge anatomy: water enters the pores and leaves by the osculum; collar "
                                         "cells (d) drive it and trap food."},
            ("Comb jellies (phylum Ctenophora)", [
                "Solitary, free-swimming marine animals: small, transparent, sometimes bioluminescent (they make "
                "their own light) (28.2.15).",
                "The body is mostly mesoglea, a jellylike substance. They are the largest animals moved by beating "
                "cilia (rows of tiny hairs), and they catch prey with colloblasts, sticky cells (28.2.15).",
                "Their DNA looks older than sponges', so they may be the oldest animal lineage, but this is still "
                "debated (28.2.15; textbook p. 514).",
            ]),
            ("Cnidarians (phylum Cnidaria)", [
                "Tubular animals, mostly in shallow seas: hydras, sea anemones, corals and jellyfish (28.2.16, "
                "28.2.18).",
                "Named for cnidocytes, stinging cells. Each holds a nematocyst, a fluid-filled capsule with a "
                "coiled thread that fires to trap or poison prey (28.2.16).",
                "The body is a two-layered sac: an outer epidermis and an inner layer that digests food in the "
                "gastrovascular cavity, the central cavity with one opening that is both mouth and anus (28.2.16, "
                "28.2.20). Mesoglea lies between the layers (28.2.21).",
                "Two body forms: the polyp, a tube with its mouth up (hydra, sea anemone), and the medusa, a bell "
                "with its mouth down (jellyfish) (28.2.16).",
                "Sea anemones are sessile polyps; corals are like sea anemones in a calcium carbonate case and live "
                "in colonies that build reefs, such as the Great Barrier Reef (28.2.18).",
                "Hydra: a small freshwater polyp, about a quarter of an inch long, with a nerve net (a web of "
                "connected nerve cells, no brain); it reproduces sexually and asexually, by budding (28.2.20, "
                "28.2.21).",
                "True jellyfish: the medusa is the main stage and the polyp stays small (28.2.20). The Portuguese "
                "man-of-war looks like a jellyfish but is a colony of polyps and medusae (28.2.19).",
            ]),
            {"fig": (28, 21), "caption": "Hydra: a polyp with tentacles (a), a bud (b), and its two tissue layers "
                                         "with mesoglea between them and cnidocytes (c)."},
            ("Traps", [
                "Sponges have no true tissues; comb jellies and cnidarians have two layers (diploblastic).",
                "Cnidocyte = the stinging cell; nematocyst = the capsule inside it.",
                "Colloblasts (comb jellies) are sticky; nematocysts (cnidarians) sting.",
                "Polyp = mouth up; medusa = mouth down.",
            ]),
        ],
        3: [
            ("Lophotrochozoans", [
                "A large protostome group: bilaterally symmetrical, three germ layers, organs; some have a true "
                "coelom (28.3.22).",
                "Lophophorans (bryozoans, brachiopods, phoronids) feed with a lophophore, a crown of ciliated "
                "tentacles around the mouth (28.3.22, 28.3.23).",
                "Trochozoans have a trochophore, a tiny swimming larva with bands of cilia: mollusks and annelids, "
                "plus flatworms and rotifers (28.3.22, 28.3.23).",
            ]),
            {"fig": (28, 23), "caption": "The lophophore (a) and the trochophore larva (b)."},
            ("Mollusks (phylum Mollusca)", [
                "Snails, clams, squids and their relatives, over 150,000 species (28.3.24; textbook p. 516).",
                "Three-part body: the visceral mass holds the internal organs; the mantle covers it and may secrete "
                "a shell or help form gills or lungs; the foot is a muscle for moving, attaching or catching food "
                "(28.3.24).",
                "Many have a radula, a tongue-like organ with rows of teeth for scraping food (28.3.25).",
                "Nervous system: several ganglia (clusters of nerve cells) joined by nerve cords. The coelom is "
                "reduced, mostly around the heart. Circulation is open: the heart pumps hemolymph (the blood) "
                "into the hemocoel, open spaces around the organs (28.3.26).",
            ]),
            {"fig": (28, 25), "caption": "The mollusk body plan: visceral mass, mantle, foot; radula teeth (b)."},
            ("The three mollusk classes", [
                "Bivalves (clams, oysters, mussels, scallops): a shell of two hinged parts; no head and no radula. "
                "Cilia on the gills draw water into the mantle cavity, and the gills filter out food (filter "
                "feeders) (28.3.27). Freshwater clams have separate sexes and internal fertilization (28.3.27).",
                "Gastropods (snails, slugs, conchs, nudibranchs): the largest class; a flat foot to creep on, a "
                "one-piece coiled shell in most, and a head with eyes on tentacles (28.3.29).",
                "Cephalopods (squids, octopuses, nautilus): “head-footed”. They squeeze water out of the mantle "
                "cavity for jet propulsion, catch prey with arms and suckers, tear it with a beak, have "
                "well-developed senses, and octopuses can learn (28.3.31).",
            ]),
            {"fig": (28, 28), "caption": "Bivalves: scallop, mussels, and the inside of a clam (Anodonta): water in "
                                         "the incurrent siphon, over the gills, out the excurrent siphon."},
            ("Annelids (phylum Annelida): segmented worms", [
                "The body is a row of segments separated by septa (partitions). The fluid-filled coelom works as a "
                "hydrostatic skeleton: muscles push against the fluid (28.3.33).",
                "Closed circulation (blood stays in vessels), a ventral solid nerve cord, and setae, bristles that "
                "grip the ground. Oligochaetes have few setae, polychaetes many (28.3.33).",
                "Earthworm digestion: mouth → muscular pharynx → crop (stores food) → gizzard (grinds it) → long "
                "intestine, whose fold, the typhlosole, adds surface for absorption → anus (28.3.34).",
                "Segmentation shows inside too: each segment has its own ganglia, nephridia (excretory tubes) and "
                "blood vessel branches (28.3.35).",
                "Earthworms are hermaphrodites (each has both sexes). Two worms lie side by side, head to tail; the "
                "clitellum, a thickened band, secretes mucus that keeps the sperm from drying. There is no larva "
                "(28.3.36).",
                "Polychaetes are mostly marine, with setae in bundles on parapodia (paddle-like flaps); clam worms "
                "(Nereis) are predators (28.3.38).",
                "Leeches live mostly in fresh water, have no setae and two suckers, and their saliva holds hirudin, "
                "which stops blood clotting (28.3.38).",
            ]),
            {"fig": (28, 37), "caption": "Earthworm: the digestive tract along the body, and a cross section "
                                         "(coelom, setae, nephridium, typhlosole, ventral nerve cord)."},
            ("Flatworms (phylum Platyhelminthes)", [
                "Flat bodies with no circulatory or respiratory organs; a sac body plan with one opening; no body "
                "cavity (28.3.40).",
                "Planarians (Dugesia) are free-living in fresh water. The head has auricles (side flaps that sense "
                "chemicals and touch) and two light-sensitive eyespots (28.3.42).",
                "Planarian feeding: a pharynx (tube) comes out of the mouth on the underside and sucks food into a "
                "branched gastrovascular cavity (28.3.41).",
                "Excretion by flame cells, cells whose beating cilia (like a flickering flame) move fluid into "
                "canals; this also controls water balance (28.3.41, 28.3.43).",
                "A ladder-type nervous system: two nerve cords joined by cross nerves, with paired ganglia as a "
                "primitive brain. Three muscle layers (28.3.42).",
                "Planarians are hermaphrodites that cross-fertilize, and they also reproduce asexually by "
                "regeneration (28.3.43).",
            ]),
            {"fig": (28, 41), "caption": "Planarian: digestive system, excretory system with flame cells, and "
                                         "reproductive system."},
            ("Parasitic flatworms", [
                "Flukes (trematodes) and tapeworms (cestodes) live inside a host. They have lost cephalization; the "
                "head is replaced by hooks or suckers for attachment, and they don't need a well-developed nervous "
                "system or gut (28.3.44).",
                "They use a primary host, which carries the adult worm, and a secondary host, which carries the "
                "larvae and passes them on (28.3.44, 28.3.46).",
                "Blood fluke Schistosoma: larvae burrow through human skin, mature in the liver, and adults live in "
                "blood vessels of the gut; eggs leave in feces, hatch in water, develop in a snail (secondary host), "
                "and swim off to find a human (28.3.45).",
                "Tapeworms have a scolex, a head with hooks and suckers, followed by proglottids, segments each with "
                "male and female sex organs that fill with eggs (28.3.46).",
                "Pork tapeworm Taenia solium: humans (primary host) eat undercooked pork with bladder worms (larvae "
                "in cysts); the tapeworm grows in the intestine; eggs leave in feces; pigs (secondary host) eat "
                "them, and the larvae encyst in muscle (28.3.46, 28.3.47).",
            ]),
            {"fig": (28, 45), "caption": "Blood fluke life cycle: human (primary host) and snail (secondary host)."},
            {"fig": (28, 47), "caption": "Pork tapeworm life cycle: human (primary host) and pig (secondary host)."},
            ("Rotifers (phylum Rotifera)", [
                "Microscopic animals named for the corona, a crown of cilia that looks like a turning wheel; it "
                "moves the animal and sweeps food to the mouth. About 2,000 species, mostly freshwater (28.3.48).",
            ]),
            ("Traps", [
                "Lophophore = feeding crown; trochophore = larva.",
                "Mollusks have open circulation and a reduced coelom; annelids have closed circulation and a large, "
                "divided coelom.",
                "Bivalves have no radula and no head.",
                "Oligochaetes = few setae (earthworms); polychaetes = many (marine).",
                "Primary host = adult worm; secondary host = larvae.",
                "Flame cells excrete; they aren't nerve or digestive cells.",
            ]),
        ],
        4: [
            ("Ecdysozoans", [
                "Ecdysis means “stripping off”. These protostomes, the roundworms and arthropods, build a cuticle, "
                "an outer covering that protects and supports them and is shed (molted) as they grow (28.4.50).",
            ]),
            ("Roundworms (phylum Nematoda)", [
                "Nonsegmented worms. They have a pseudocoelom, a “false” body cavity lined by mesoderm on the body wall "
                "but not around the gut (textbook p. 525), which holds the organs and works as a hydrostatic skeleton (28.4.51).",
                "Caenorhabditis elegans, a free-living roundworm, is a model animal for genetics and development "
                "(28.4.51).",
                "Parasites of humans: Ascaris (intestinal worm, over 200,000 eggs a day); Trichinella, which causes "
                "trichinosis when people eat rare pork; filarial worms such as heartworm, fatal in dogs; and "
                "Wuchereria, carried by mosquitoes, which blocks lymph vessels so the limbs swell (elephantiasis) "
                "(28.4.52, 28.4.53).",
            ]),
            ("Arthropods (phylum Arthropoda): five keys to success", [
                "Exoskeleton: a rigid, jointed outer skeleton of chitin (a tough polysaccharide); it can't grow, so "
                "they molt (28.4.54, 28.4.55).",
                "Segmentation, with segments fused into a head, thorax and abdomen (28.4.54).",
                "A well-developed nervous system: brain, ventral nerve cord, simple or compound eyes (28.4.54).",
                "Varied respiratory organs: gills (water), book lungs (spiders) or tracheae, air tubes (insects) "
                "(28.4.54).",
                "Metamorphosis, a change of form from larva to adult; larva and adult eat different food, so they "
                "don't compete (28.4.54).",
            ]),
            {"fig": (28, 55), "caption": "Arthropod exoskeleton: a joint moved by flexor and extensor muscles (a), "
                                         "the cuticle's layers (b), and a dragonfly molting (c)."},
            ("Crustaceans", [
                "A crusty exoskeleton (chitin plus calcium carbonate), compound eyes and five pairs of head "
                "appendages; mostly aquatic (28.4.56).",
                "Decapods (“ten feet”: crabs, crayfish, lobsters, shrimp) are the most familiar. Copepods and krill "
                "are small swimmers that eat algae. Barnacles live attached to things like wharf pilings (28.4.56).",
                "Crayfish: the head and thorax are fused into a cephalothorax under a carapace (shield); five pairs "
                "of walking legs, the first with claws; swimmerets on the abdomen; gills; open circulation; green "
                "glands excrete wastes (28.4.58, 28.4.59).",
            ]),
            {"fig": (28, 59), "caption": "Male crayfish: cephalothorax with five pairs of walking legs; abdomen with "
                                         "swimmerets, uropods and telson."},
            ("Centipedes and millipedes", [
                "Centipedes (“hundred legs”): one pair of walking legs per segment; the first trunk appendages are "
                "venomous jaws for killing prey (28.4.61).",
                "Millipedes: one pair of legs on each of four thoracic segments, two pairs on abdominal segments; "
                "cylindrical bodies (28.4.61).",
            ]),
            ("Insects", [
                "Mostly on land; they breathe by tracheae (28.4.63).",
                "Three body parts: the head (sense organs, mouthparts), the thorax (three pairs of legs and, in "
                "many, one or two pairs of wings), and the abdomen (most internal organs) (28.4.63).",
                "Complete metamorphosis (butterflies): larva → pupa → adult, with the body completely reorganized. "
                "Incomplete metamorphosis (grasshoppers): a gradual change (28.4.63, 28.4.64).",
                "Grasshopper: jumping third legs; a tympanum (eardrum) on the first abdominal segment; the female's "
                "ovipositor lays eggs; food stored in the crop, then ground in the gizzard; Malpighian tubules "
                "excrete; air enters spiracles (openings) and flows through tracheae; a tubular heart (28.4.64).",
                "Insect orders differ in wings and mouthparts: beetles (hard forewings, chewing), wasps (narrow "
                "waist, stinger), lice (wingless, piercing-sucking), dragonflies (28.4.65).",
            ]),
            {"fig": (28, 66), "caption": "Female grasshopper: outside (a) and inside (b)."},
            ("Chelicerates", [
                "Spiders, scorpions, ticks, mites and horseshoe crabs. The appendages are on the cephalothorax, none on "
                "the abdomen: the first pair, chelicerae, for feeding and defense; the second, pedipalps, for feeding or sensing "
                "(28.4.67, 28.4.68).",
            ]),
            ("Traps", [
                "Cuticle = the covering that is molted; chitin = what the arthropod exoskeleton is made of.",
                "Pseudocoelom (roundworms) is incompletely lined by mesoderm; a true coelom is lined completely.",
                "Tracheae (air tubes) start at spiracles (openings).",
                "Complete metamorphosis has a pupa; incomplete (grasshopper) doesn't.",
                "Chelicerae come first, pedipalps second.",
            ]),
        ],
        5: [
            ("Echinoderms (phylum Echinodermata)", [
                "Sea stars, sea urchins, sea cucumbers and sand dollars: marine deuterostomes, so they are related "
                "to chordates (28.5.69).",
                "Radial symmetry (in five parts) as adults but bilateral symmetry as larvae, a sign that they "
                "descend from bilateral ancestors (28.5.69; textbook p. 532).",
                "An endoskeleton (inside skeleton) of calcium-rich plates with spines; a central nerve ring with "
                "branches (28.5.69).",
                "The water vascular system, a network of water-filled canals ending in tube feet, does locomotion, "
                "feeding, gas exchange and sensing (28.5.69).",
            ]),
            ("Sea star", [
                "Water enters through the sieve plate (madreporite) and runs through canals; an ampulla (a bulb) "
                "contracts and pushes water into its tube foot, which extends and grips; alternating tube feet "
                "move the animal (28.5.72).",
                "Tube feet pull open clams and oysters (bivalves) for food (28.5.72).",
                "Echinoderms have no respiratory, excretory or circulatory system; fluids in the coelom and water "
                "vascular system do those jobs (28.5.72; textbook p. 533). They reproduce sexually "
                "and asexually (28.5.72).",
            ]),
            {"fig": (28, 70), "caption": "Sea star anatomy: water vascular system (sieve plate, radial canal, tube "
                                         "feet), stomachs, gonads, endoskeletal plates."},
            ("Traps", [
                "Echinoderms are deuterostomes, like us, not protostomes.",
                "Their skeleton is internal (endoskeletal plates), not an exoskeleton.",
                "Radial adults, bilateral larvae.",
            ]),
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
        "This chapter follows the chordates, our own phylum, from small sea creatures without a backbone to the "
        "mammals. The story is a series of new features, each one opening a new way of life: a backbone, then "
        "jaws, then lungs and limbs for land, then an egg that doesn't need water, then hair and milk (29.1.8, "
        "29.2.12).",
        "Chordates are deuterostomes, like the echinoderms of Ch 28 (textbook p. 537). Most chordates are "
        "vertebrates, animals with a vertebral column (backbone); a few are not (29.1.5).",
        {"fig": (29, 8), "caption": "The chordate family tree. Each mark on a branch is a new feature shared by "
                                    "the groups above it: notochord → vertebrae → jaws → bony skeleton → lungs → "
                                    "4 limbs → amniotic egg → mammary glands."},
    ],
    "sections": {
        1: [
            ("The four chordate characteristics (at some stage of life)", [
                "Notochord: a stiff supporting rod along the back, just below the nerve cord (29.1.3).",
                "Dorsal tubular nerve cord: a hollow nerve cord along the back (insects' cord runs along the belly); "
                "its front end becomes the brain in most chordates, and in vertebrates the vertebrae protect it "
                "(29.1.3).",
                "Pharyngeal pouches: pockets in the throat region; they become gills in aquatic vertebrates, appear "
                "only in the embryo in most vertebrates, and are reshaped for other uses on land (29.1.3). "
                "Textbook: in humans the first pair becomes the auditory tubes (p. 537).",
                "Postanal tail: a tail that extends past the anus; in humans it disappears in the embryo (29.1.3).",
            ]),
            {"fig": (29, 4), "caption": "The four chordate characteristics."},
            ("Nonvertebrate chordates", [
                "In these, the notochord stays and is never replaced by a vertebral column (29.1.5).",
                "Lancelets (cephalochordates): small, segmented filter feeders in shallow seas; adults keep all "
                "four characteristics (29.1.5, 29.1.6).",
                "Sea squirts (urochordates, also called tunicates): marine filter feeders whose adults have a thick "
                "covering, the tunic. The larva has all four traits, but the adult keeps only the gill slits "
                "(29.1.5, 29.1.7).",
                "Many biologists think sea squirts are directly related to the vertebrates: a sea squirt larva may "
                "have become sexually mature without turning into the adult form, and evolved into a fishlike "
                "vertebrate (29.1.5).",
            ]),
            {"fig": (29, 6), "caption": "Lancelet: notochord, dorsal tubular nerve cord, gill slits; water exits by "
                                        "the atriopore."},
            ("Traps", [
                "Notochord (the rod) vs nerve cord (the nerves above it).",
                "Lancelets = cephalochordates; sea squirts = urochordates (tunicates).",
                "Chordate is not the same as vertebrate: lancelets and sea squirts are chordates without a backbone.",
            ]),
        ],
        2: [
            ("What vertebrates add", [
                "A vertebral column that replaces the embryo's notochord; the separate vertebrae show the body is "
                "segmented (29.2.9, 29.2.11).",
                "A skull that encloses the brain, with a high degree of cephalization and complex sense organs "
                "(29.2.9).",
                "An endoskeleton (inside skeleton) of living tissue that grows with the animal, protects organs, "
                "anchors muscles, and bears paired appendages (fins or limbs) (29.2.9).",
                "A large coelom, a complete digestive tract (mouth and anus), closed circulation, gills or lungs, "
                "kidneys that regulate water, and separate sexes with sexual reproduction (29.2.10).",
            ]),
            {"fig": (29, 11), "caption": "The vertebrae grow around the notochord and neural tube and replace the "
                                         "notochord."},
            ("Vertebrate evolution, in order", [
                "Chordates appear at the start of the Cambrian period, 542 MYA (million years ago). By the end of "
                "the Ordovician there were jawless and jawed fishes, the earliest vertebrates (29.2.12).",
                "Jaws, for catching prey: gnathostomes (“jaw mouths”) are the jawed fishes plus the other "
                "vertebrates descended from them (29.2.12).",
                "Lungs and a bony skeleton prepared fishes for land; tetrapods (“four feet”) have four limbs; "
                "amphibians evolved from bony fishes by the Devonian (29.2.12).",
                "Amniotes lay an amniotic egg, which surrounds the embryo in amniotic fluid, so they can "
                "reproduce on land (29.2.12).",
            ]),
            ("Traps", [
                "Gnathostomes = jaws; tetrapods = four limbs; amniotes = amniotic egg.",
                "The notochord is replaced by the vertebral column, not the nerve cord.",
            ]),
        ],
        3: [
            ("Fishes", [
                "The largest group of vertebrates: aquatic, breathe with gills, usually fins and scales (29.3.13).",
                "Jawless fishes (agnathans): ostracoderms were the earliest vertebrate fossils. Today's lampreys and "
                "hagfishes have no bony skeleton. The parasitic sea lamprey nearly wiped out the whitefish and "
                "trout of the Great Lakes (29.3.13, 29.3.14).",
                "Jawed fishes are ectotherms (their body temperature depends on the environment) with gills, a "
                "cartilage or bone endoskeleton, and scales (29.3.15).",
                "Jaws evolved from the first pair of gill arches (the supports between the gill slits) of jawless "
                "fishes; the second pair became supports for the jaws (29.3.15, 29.3.16).",
                "Placoderms: extinct, armored jawed fishes of the Devonian, thought to be the ancestors of sharks "
                "and bony fishes (29.3.15).",
            ]),
            {"fig": (29, 16), "caption": "Jaws evolved from gill arches."},
            ("Cartilaginous fishes (Chondrichthyes)", [
                "Sharks, rays, skates and chimaeras: a skeleton of cartilage, not bone, and no gill cover (29.3.17).",
                "They sense electric currents in water, and sharks and rays have a lateral line system, "
                "pressure-sensing cells along the sides (29.3.17; textbook p. 541).",
                "Some are filter feeders, some predators. Rays and skates have huge winglike pectoral fins and "
                "bodies flattened top to bottom (29.3.17, 29.3.19).",
            ]),
            ("Bony fishes (Osteichthyes)", [
                "A skeleton of bone; the majority of living vertebrates (29.3.20; textbook p. 542).",
                "Most are ray-finned fishes, with fins held up by thin bony rays (29.3.20, 29.3.21).",
                "Lobe-finned fishes are a small group with fleshy fins supported by central bones (29.3.20).",
                "No external gill slits: an operculum, a bony flap, covers the gills. The swim bladder, a gas-filled "
                "sac, changes the fish's buoyancy (29.3.20).",
                "Separate sexes; most use external fertilization (eggs and sperm meet in the water) (29.3.20).",
                "Lobe-finned fishes gave rise to today's lobe-finned fishes and to the amphibians. Living ones: "
                "lungfishes, which have lungs as well as gills, and the coelacanth, caught in 1938 after being "
                "thought extinct (29.3.22, 29.3.23).",
            ]),
            {"fig": (29, 21), "caption": "A typical ray-finned fish (soldierfish) and the variety of ray-finned "
                                         "fishes."},
            ("Traps", [
                "Agnathans = jawless; placoderms = extinct jawed fishes.",
                "Cartilaginous fishes have no operculum; bony fishes do.",
                "Ray-finned = most fishes; lobe-finned = the line that led to amphibians.",
            ]),
        ],
        4: [
            ("Amphibians", [
                "Frogs, toads, salamanders, newts and caecilians: most are tetrapods with limbs (29.4.24).",
                "Smooth, nonscaly skin; lungs in most adults; a double-loop circulation with a three-chambered "
                "heart; sense organs tuned for land; ectotherms (29.4.24).",
                "Reproduction is in water, followed by metamorphosis (a tadpole with gills becomes an air-breathing "
                "adult) (29.4.24).",
            ]),
            ("Circulation compared", [
                "Fishes: a single loop with a two-chambered heart; blood goes heart → gills → body → back (29.4.25).",
                "Amphibians and most reptiles: a double loop, one to the lungs and one to the body, with a "
                "three-chambered heart (29.4.25).",
                "Crocodilians, birds and mammals: a four-chambered heart sends oxygen-poor blood to the lungs and "
                "oxygen-rich blood to the body, without mixing (29.4.25).",
            ]),
            {"fig": (29, 25), "caption": "Single loop (fishes), double loop with a three-chambered heart, and the "
                                         "four-chambered heart."},
            ("From fins to legs", [
                "Two hypotheses: lobe-finned fishes could move (pond to pond on their fins), or the food on land and "
                "the absence of predators favored life on land (29.4.26).",
                "Tiktaalik roseae, a transitional fossil, is intermediate between lobe-finned fishes and tetrapods "
                "with limbs; it shows how legs arose (29.4.26). The same bones (humerus, radius, ulna; femur, tibia, "
                "fibula) appear in the fins and in the limbs (29.4.27).",
            ]),
            {"fig": (29, 27), "caption": "Fin bones of a transitional form compared with the limb bones of an "
                                         "ancestral amphibian."},
            ("Living amphibians: three groups", [
                "Salamanders and newts: tails; salamanders use internal fertilization (29.4.28).",
                "Frogs and toads: no tail as adults (29.4.28).",
                "Caecilians: legless, often blind, worm-shaped burrowers (29.4.28, 29.4.29).",
            ]),
            ("Animals in medicine (29.4.30)", [
                "Snake venom gives pain medications; goats engineered to make drugs in their milk; pigs altered to "
                "supply hearts for transplants (29.4.30).",
            ]),
            ("Traps", [
                "Three-chambered heart = amphibians (and most reptiles); four = crocodilians, birds, mammals.",
                "Tiktaalik is a fossil fish-tetrapod, not a living amphibian.",
            ]),
        ],
        5: [
            ("Reptiles (class Reptilia), birds included", [
                "More than 20,000 species. Paired limbs; thick, scaly skin that water can't pass through; lungs "
                "with an expandable rib cage; a ventricle partly or fully divided by a septum (a wall); "
                "well-developed kidneys; ectotherms (29.5.31).",
                "Reproduction fit for land: internal fertilization and a shelled amniotic egg (29.5.31).",
                "The amniotic egg's membranes: the amnion holds fluid around the embryo (no drying out), the chorion "
                "exchanges gases, the allantois stores wastes, and the yolk sac feeds the embryo (29.5.36 caption; "
                "textbook Fig. 29.15).",
            ]),
            {"fig": (29, 36), "caption": "Living reptiles, and the amniotic egg (f)."},
            ("Three amniote lineages, told apart by skull openings", [
                "Amniotes evolved from amphibian ancestors by the Carboniferous period (29.5.33).",
                "Anapsid skull (no opening behind the eye socket): turtles. A modern view makes them specialized "
                "diapsids; this is still debated (29.5.33).",
                "Diapsid skull (two openings): the other reptiles, birds included (29.5.33).",
                "Synapsid skull (one opening): mammals (29.5.33).",
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
            ("Birds", [
                "Birds evolved from dinosaurs, as a plentiful fossil record shows (29.5.37).",
                "Feathers, modified reptilian scales; a skeleton with fused bones (the collarbone included) and a "
                "keel on the sternum (breastbone) for the flight muscles; lungs connected to air sacs; endothermy "
                "(the body makes its own heat); acute vision (29.5.37, 29.5.38).",
                "Most fly (eagles, geese); some are flightless (emus, penguins, kiwis, ostriches). Birds are "
                "classified by beak and foot type, habitat and behavior (29.5.39, 29.5.40).",
            ]),
            {"fig": (29, 38), "caption": "Bird anatomy (air sacs, crop, gizzard) and an eagle skeleton with the keeled "
                                         "sternum."},
            ("Traps", [
                "Anapsid = 0 openings (turtles), diapsid = 2 (other reptiles, birds), synapsid = 1 (mammals).",
                "Birds are reptiles, and endotherms; other reptiles are ectotherms.",
                "Amnion = the fluid sac; the shell isn't the amnion.",
            ]),
        ],
        6: [
            ("Mammals (class Mammalia)", [
                "Hair and milk-producing mammary glands (29.6.41).",
                "A skull that holds a larger brain for the body's size, and differentiated teeth (different shapes "
                "for different jobs) (29.6.41).",
                "Efficient breathing and circulation: a double loop with a four-chambered heart; kidneys that save "
                "water; a highly developed nervous system; internal development in most (29.6.41).",
            ]),
            ("Mammal evolution", [
                "Mammals share an amniote ancestor with reptiles; their immediate ancestors had a synapsid skull "
                "(29.6.42).",
                "The first true mammals appeared in the Triassic and lived alongside the dinosaurs. The common "
                "ancestor of all mammal groups lived about 220 MYA (29.6.42).",
                "Monotremes are the earliest group. After the dinosaurs, placental mammals spread into the habitats "
                "the dinosaurs had held (adaptive radiation) (29.6.42).",
            ]),
            {"fig": (29, 43), "caption": "The mammal family tree: monotremes branch off first; marsupials and "
                                         "placentals share live birth and a true uterus."},
            ("The three living lineages", [
                "Monotremes (duckbill platypus): lay hard-shelled amniotic eggs; a single urogenital opening, the "
                "cloaca (29.6.44, 29.6.45).",
                "Marsupials (koala, opossum): the female has a pouch, where the tiny newborn keeps developing "
                "(29.6.44, 29.6.45).",
                "Placental mammals: the placenta passes nutrients and wastes between the mother's blood and the "
                "fetus's blood (29.6.44; textbook p. 553).",
                "Placental orders are in the table at 29.6.46: e.g. Cetacea (whales), Artiodactyla (even-toed: "
                "cattle, deer), Perissodactyla (odd-toed: horses), Chiroptera (bats), Rodentia (one pair of "
                "ever-growing incisors), Lagomorpha (rabbits: two pairs), Primates (opposable thumb) (29.6.46).",
            ]),
            ("Traps", [
                "Monotremes = eggs; marsupials = pouch; placentals = placenta.",
                "The placenta exchanges substances; the mother's and fetus's blood don't mix.",
                "Rodents have one pair of ever-growing incisors, rabbits two.",
            ]),
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
        "This chapter places humans among the primates and then follows the fossils from the first upright-walking "
        "ancestors to modern humans. Two ideas carry it: primates are built for life in trees, and the human line "
        "is marked by walking upright first and by a bigger brain later (30.1.3, 30.2.20).",
        "Group names matter here. Primates: lemurs, monkeys, apes and humans. Hominids: the great apes "
        "(orangutans, gorillas, chimpanzees) and humans. Hominins: humans and species very closely related to them "
        "(our extinct close relatives) (30.1.3, 30.1.11; textbook p. 570).",
    ],
    "sections": {
        1: [
            ("Primates and their trends", [
                "Primates are an order of mammals: prosimians, monkeys, apes and humans. Most are arboreal (live in "
                "trees) (30.1.3).",
                "Their evolution trends toward mobile limbs, grasping hands, a flattened face, stereoscopic vision, "
                "a large complex brain and a reduced reproductive rate (30.1.3).",
            ]),
            {"fig": (30, 4), "caption": "Primate diversity: prosimian, New and Old World monkeys, Asian and African "
                                        "apes, hominins."},
            ("Limbs and hands", [
                "Prehensile hands and feet, adapted for grasping; most have flat nails instead of claws and "
                "sensitive pads on fingers and toes (30.1.5).",
                "Many have an opposable thumb, which can touch each other finger, for a powerful and precise grip. "
                "Except for humans, primates with opposable thumbs also have opposable toes (30.1.5).",
                "Mobile limbs and clawless digits let primates grasp and release branches and bring food to the "
                "mouth (30.1.5).",
            ]),
            {"fig": (30, 6), "caption": "From a tree shrew's claws to the human hand's long, opposable thumb."},
            ("Vision", [
                "Stereoscopic vision: both eyes face forward and see the same scene from slightly different angles, "
                "giving 3-D images with good depth perception, needed to judge the distance to the next branch "
                "(30.1.7, 30.1.8).",
                "Color vision comes from cone cells (need bright light, sharp color image), alongside rod cells "
                "(work in dim light, blurry gray image). Humans and apes have three kinds of cones: greens, blues, "
                "reds (30.1.7).",
            ]),
            ("Brain and reproduction", [
                "A larger, more complex brain: in apes and humans the smell area is smaller, the sight area larger, "
                "more brain controls the hands (hand-eye coordination), and more handles communication for living "
                "in social groups (30.1.9).",
                "Reduced reproductive rate: later maturity, longer lives, long pregnancy (time for the forebrain to "
                "develop), usually one baby at a time, and a long childhood of learning (30.1.10).",
            ]),
            ("Who is related to whom", [
                "Humans' closest relatives are the chimpanzees; the two shared a common ancestor 5–7 MYA. Humans "
                "did not descend from chimpanzees, monkeys or apes: we share ancestors with them (30.1.11).",
                "Anthropoids are the hominids, gibbons, Old World monkeys and New World monkeys (30.1.12).",
                "Old World monkeys (Africa, Asia): no grasping tail, protruding noses (baboons, rhesus monkeys, used "
                "in medical research). New World monkeys (South America): often long prehensile tails, flat noses "
                "(spider monkey, capuchin) (30.1.12).",
                "Prosimians (lemurs, tarsiers) were the first primates to branch off. The common ancestor of all "
                "primates lived about 55 MYA and may have looked like today's tree shrews (30.1.17).",
            ]),
            {"fig": (30, 13), "caption": "The primate family tree: prosimians branch off first, then New World "
                                         "monkeys, Old World monkeys, gibbons, orangutans, gorillas, and last "
                                         "chimpanzees and humans."},
            ("Fossil apes", [
                "Primate fossils like monkeys appear in Africa about 45 MYA; New World monkeys' ancestors reached "
                "South America about 40 MYA, though how they crossed the Atlantic is uncertain (30.1.14).",
                "Proconsul (about 35 MYA) is the best link between monkeys, gibbons and early hominids: "
                "baboon-sized, with a 165 cc brain and no tail; it walked on all fours on top of branches like a "
                "monkey (30.1.14, 30.1.15).",
                "Proconsul probably led to the dryopithecines. About 10 MYA Africa and Arabia joined Asia, and apes "
                "spread into Europe and Asia. Dryopithecus (9.5 MYA, Spain) swung from branch to branch like "
                "today's gibbons (30.1.16).",
            ]),
            {"fig": (30, 15), "caption": "Monkey vs Proconsul: Proconsul mixes monkeylike and apelike features."},
            ("Genes: humans vs chimpanzees", [
                "Different chromosome numbers (textbook: chimpanzees 48, humans 46), yet close relatives: human "
                "chromosome 2 is a fusion of two chimpanzee chromosomes (30.1.18, 30.1.19).",
                "Similar patterns of transposons (jumping DNA pieces, such as Alu) and pseudogenes (broken gene "
                "copies); the DNA base sequences differ by only 1.5% (30.1.18, 30.1.19).",
                "Differences in noncoding DNA kept by each species may explain the differences in anatomy "
                "(30.1.18).",
            ]),
            {"fig": (30, 19), "caption": "Human chromosome 2 = chimpanzee chromosomes 2A + 2B fused; Alu elements in "
                                         "the same places in both."},
            ("Traps", [
                "Hominins (humans and close extinct relatives) vs hominids (also the great apes).",
                "Stereoscopic vision = depth perception; color vision = cone cells.",
                "Proconsul walked on top of branches; Dryopithecus swung below them.",
                "Humans and chimpanzees share an ancestor; humans didn't descend from chimpanzees.",
            ]),
        ],
        2: [
            ("How to recognize a hominin fossil", [
                "Bipedalism: standing and walking on two feet (apes walk on all fours). Early humanlike hominins "
                "aren't in the genus Homo, but walking upright puts them on our side; it also frees the hands for "
                "tools (30.2.20).",
                "The skull: modern humans have a flatter face, a more pronounced chin, a shorter jaw and smaller "
                "teeth than apes, and a bigger brain (chimpanzee about 400 cc, modern human 1,360 cc) (30.2.20).",
            ]),
            {"fig": (30, 21), "caption": "Timeline of hominins: how long each species lasted (million years ago, MYA)."},
            ("Ardipithecines: Ardi", [
                "Two species: Ardipithecus kadabba (5.8–5.2 MYA, only teeth and bits) and A. ramidus (4.4 MYA, over "
                "100 skeletons, Ethiopia); in 2009 a female skeleton, Ardi, was reconstructed (30.2.22).",
                "Ardi walked upright but spent a lot of time in trees. Upright features: the spine leaves the "
                "center of the skull, the femurs angle in toward the knees, a broad pelvis, knees built to carry "
                "the weight, and a foot bone that apes lack (30.2.23, 30.2.24).",
                "Apelike features: an opposable big toe and flexible wrists for moving carefully along branches; "
                "chimpanzee-sized, a 300–350 cc brain, a forward-projecting face, small teeth with no sharp "
                "canines (soft plant food) (30.2.23, 30.2.25).",
                "Ardi lived in woods, not grassland, so bipedalism didn't start with a switch to grassland. It may "
                "have helped carry infants and helped males forage on the forest floor (30.2.26).",
            ]),
            {"fig": (30, 24), "caption": "Adaptations for walking erect, in a modern human and in Ardi."},
            ("Australopithecines (australopiths)", [
                "Lived in Africa from 4 MYA to 1.5 MYA. A small, apelike brain (370–515 cc) but an upright, "
                "humanlike walk: mosaic evolution, where body parts change at different rates and times (30.2.27).",
                "Gracile (slender) types are genus Australopithecus; robust (powerful) types, with massive jaws and "
                "big grinding teeth, are genus Paranthropus. Males were larger than females (30.2.27).",
                "Some ate meat and used stone tools to scrape it from bones (30.2.27).",
                "East Africa: Australopithecus afarensis, including Lucy (bipedal, low forehead, large canines, "
                "small brain, arms longer than legs). It is considered closer to early Homo than the southern "
                "species (30.2.28, 30.2.29).",
                "Southern Africa: A. africanus, Paranthropus robustus, and A. sediba, which may have been a direct "
                "ancestor of Homo (30.2.29).",
            ]),
            {"fig": (30, 28), "caption": "Lucy (Australopithecus afarensis) and fossil footprints left by bipedal "
                                         "walkers."},
            ("Traps", [
                "Bipedalism came before the big brain (mosaic evolution).",
                "Gracile = Australopithecus; robust = Paranthropus.",
                "Ardi (Ardipithecus, 4.4 MYA) is older than Lucy (Australopithecus afarensis).",
            ]),
        ],
        3: [
            ("Early Homo", [
                "Appears about 2.5 MYA: brains of 600 cc or more, jaws and teeth like ours, and tool use (30.3.30).",
                "Homo habilis (“handyman”) and H. rudolfensis may be one species. They may have been the first "
                "hominins to use stone tools; socially organized scavengers; small cheek teeth, so they ate both "
                "meat and plants (omnivores) (30.3.31).",
            ]),
            ("Homo erectus (with H. ergaster)", [
                "Often treated as one species, H. erectus; first in Africa about 1.9 MYA, from H. habilis or an "
                "earlier ancestor (30.3.32).",
                "A larger brain, rounder jaw, big brow ridges and a projecting nose, which keeps water in the body in "
                "a hot, dry climate (30.3.32).",
                "Much taller (males 1.8 m), walked like us; the size of the birth canal shows babies were born "
                "premature and needed a long period of care (30.3.33).",
                "The first species to migrate into Europe and Asia (between 2.5 and 1 MYA), knew fire, and may have "
                "been the first to cook meat (30.3.33, 30.3.34).",
                "When it died out is debated: most estimates say several hundred thousand years ago, newer evidence "
                "100,000 years ago (30.3.35).",
            ]),
            {"fig": (30, 34), "caption": "Homo erectus leaves Africa: dates of the earliest fossils in each region."},
            ("Traps", [
                "H. habilis = handyman, first stone tools, scavenger; H. erectus = migration, fire, tall.",
            ]),
        ],
        4: [
            ("Toward modern humans", [
                "Most researchers think Homo sapiens evolved from an H. erectus line in Africa, but they disagree "
                "on when (30.4.37).",
                "Homo heidelbergensis replaced H. erectus in Africa about 500,000 years ago: a larger brain, better "
                "tools and social behavior, and probably the first shelters; it is the most likely line to modern "
                "humans (30.4.38, 30.4.39).",
                "Between 700,000 and 200,000 years ago H. heidelbergensis split into three lines: Africa → modern H. "
                "sapiens; Asia → the Denisovans; Europe → the Neanderthals. Some modern humans carry DNA from all "
                "three (30.4.39).",
                "Homo floresiensis, a dwarf species from an island, is one of the lines that split off H. erectus "
                "in Asia (30.4.38).",
            ]),
            ("Two hypotheses", [
                "Replacement (out-of-Africa) model, the main one: modern humans evolved from archaic humans only in "
                "Africa, then migrated to Asia and Europe and replaced the earlier Homo species about 100,000 years "
                "BP (before the present) (30.4.40).",
                "Its evidence: the earliest modern human remains are in Africa (Asia not until 100,000 years BP, "
                "Europe 60,000), and African mitochondrial DNA is the most diverse, as expected if humans have "
                "lived there longest (30.4.40, 30.4.41).",
                "Multiregional continuity hypothesis: modern humans arose from earlier Homo in the same way in "
                "Africa, Asia and Europe, with genetic continuity in each region. New finds (H. floresiensis, H. "
                "naledi, the Denisovans) bring it back into discussion, maybe as a mix of both models (30.4.43).",
            ]),
            {"fig": (30, 42), "caption": "The replacement model: modern humans spread from Africa and replace the "
                                         "earlier species in Asia and Europe."},
            ("Neanderthals (Homo neanderthalensis)", [
                "Lived from over 400,000 to 30,000 years ago in Europe and Asia; descended from H. heidelbergensis "
                "migrants out of Africa (30.4.44, 30.4.46).",
                "A slightly larger brain than ours (1,400 cc vs 1,360 cc), massive brow ridges, wide flat noses, a "
                "receding jaw; short, thick bones and heavy muscles, a sturdy build that saved heat in the Ice Age "
                "(30.4.45).",
                "Culturally advanced: caves or shelters, stone spear points, scrapers and knives, hunting large "
                "animals, control of fire, and burials with flowers and tools (30.4.47).",
                "Why they died out is debated: conflict with H. sapiens, diseases brought by H. sapiens, losing "
                "the competition for food, or unrelated causes (30.4.46).",
            ]),
            ("Cro-Magnons", [
                "The oldest fossils classified as H. sapiens. They left Africa for Asia and Europe about 100,000 "
                "years ago, interbred with Neanderthals and Denisovans, and reached western Europe 40,000 years ago "
                "(30.4.48).",
                "Modern-looking: lighter bones, a high flat forehead, a domed skull with a 1,590 cc brain, small "
                "teeth, a distinct chin (30.4.48).",
                "Hunter-gatherers with compound tools, blades and spears that killed from a distance; they may have "
                "caused the Pleistocene overkill, the extinction of many large mammals (30.4.49).",
                "Their brain may have allowed a full language; their art (sculptures, cave paintings) shows the "
                "symbolic thinking that speech needs (30.4.50).",
                "Agriculture: full dependence on crops and domestic animals came about 4,500 years ago, perhaps "
                "forced by the loss of big game and climate change. It sped up biocultural evolution, in which "
                "natural selection acts on cultural achievements (30.4.51).",
            ]),
            ("Human variation", [
                "Some differences are adaptations to local conditions (30.4.53).",
                "Skin color: dark skin protects against strong UV light; light skin still makes vitamin D where UV "
                "is weak (30.4.53).",
                "Bergmann's rule: animals in colder regions have bulkier bodies. Allen's rule: shorter limbs, "
                "fingers and ears in the cold. Both change the surface-area-to-volume ratio, which controls heat "
                "loss (30.4.53). Example: the slim, long-limbed Maasai of East Africa vs the stockier Inuit of the "
                "Arctic (30.4.52 caption).",
                "The replacement model also explains ethnic groups: all modern humans share a recent common "
                "ancestor (Cro-Magnon) who evolved in Africa; modern populations vary less than archaic ones did "
                "(30.4.54).",
                "Mitochondrial DNA points to a common ancestor no more than a million years ago, and Lewontin's "
                "study of 17 genes in seven groups found that most genetic variation is within groups, not "
                "between them (30.4.54).",
            ]),
            ("Traps", [
                "Replacement = Africa only, then spread; multiregional = everywhere in parallel.",
                "Neanderthal brains were slightly larger than ours, not smaller.",
                "Denisovans = Asian line; Neanderthals = European line; H. sapiens = African line.",
                "Bergmann = bulkier body; Allen = shorter limbs and ears.",
            ]),
        ],
    },
    "look_up": [
        "Each species' dates and brain size: the Hominins and Brain sizes tables.",
        "Migration dates: 30.3.34 and 30.4.42.",
        "Proconsul's monkeylike and apelike features: 30.1.15.",
    ],
}
