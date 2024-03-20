import urandom

physical = [
    ("balafré", "balafrée"),
    ("barbu", "barbue"),
    ("beaux yeux", "beaux yeux"),
    ("borgne", "borgne"),
    ("chauve", "chauve"),
    ("costaud", "costaude"),
    ("dégarni", "dégarnie"),
    ("édenté", "édenté"),
    ("effrayant", "effrayante"),
    ("flamboyant", "flamboyante"),
    ("fort", "forte"),
    ("grand", "grande"),
    ("grandes oreils", "grandes oreils"),
    ("imposant", "imposante"),
    ("louche", "louche"),
    ("magnifique", "magnifique"),
    ("maigre", "maigre"),
    ("manchot", "manchot"),
    ("mignon", "mignonne"),
    ("militaire", "militaire"),
    ("moche", "moche"),
    ("musclé", "musclée"),
    ("nez imposant", "nez imposant"),
    ("noble", "noble"),
    ("pauvre", "pauvre"),
    ("propre", "propre"),
    ("obèse", "obèse"),
    ("rabougri", "rabougrie"),
    ("rachitique", "rachitique"),
    ("raffiné", "raffinée"),
    ("répugnant", "répugnante"),
    ("riche", "riche"),
    ("roturier", "roturiere"),
    ("rougeaud", "rougeaude"),
    ("sauvage", "sauvage"),
    ("splendide", "splendide"),
]

mental = [
    ("ambitieux", "ambitieuse"),
    ("arrogant", "arrogante"),
    ("bègue", "bègue"),
    ("comère", "comère"),
    ("colérique", "colérique"),
    ("couard", "couarde"),
    ("courageux", "courageuse"),
    ("cupide", "cupide"),
    ("curieux", "curieuse"),
    ("fier", "fière"),
    ("idéaliste", "idéaliste"),
    ("paresseux", "paresseuse"),
    ("patient", "patiente"),
    ("plaintif", "plaintive"),
    ("rusé", "rusée"),
    ("sage", "sage"),
    ("lettré", "lettrée"),
]

traits = [
    ("craque des doigts", "craque des doigts"),
    ("boiteux", "boiteuse"),
    ("drogué", "droguée"),
    ("hygiène déplorable", "hygiène déplorable"),
    ("louche", "louche"),
    ("muet", "muette"),
    ("parle bas", "parle bas"),
    ("parle fort", "parle fort"),
    ("regard profond", "regard profond"),
    ("sourd", "sourde"),
    ("tic facial", "tic facial"),
    ("tousse", "tousse"),
    ("voix grave", "voix grave"),
    ("voix hâchée", "voix hâchée"),
    ("voix aiguë", "voix aiguë"),
    ("zozote", "zozote"),
]

title_noun = [
    [
        ("Briseur", True, False),
        ("Cendres", True, True),
        ("Fléau", False, False),
        ("Miasmes", True, True),
        ("Mort", True, False),
        ("Nuit", True, False),
        ("Ombre", True, False),
        ("Sang", False, False),
        ("Ténèbres", True, True),
        ("Vénin", False, False),
        ("Ame", True, False),
        ("Aube", True, False),
        ("Eté", False, False),
        ("Héros", False, False),
        ("Roi", False, False),
        ("Nuage", False, False),
        ("Lune", True, False),
        ("Soleil", False, False),
        ("Vérité", True, False),
        ("Parasite", False, False),
    ],
    [
        ("Briseuse", True, False),
        ("Cendres", True, True),
        ("Fléau", False, False),
        ("Miasmes", True, True),
        ("Mort", True, False),
        ("Nuit", True, False),
        ("Ombre", True, False),
        ("Sang", False, False),
        ("Ténèbres", True, True),
        ("Vénin", False, False),
        ("Ame", True, False),
        ("Aube", True, False),
        ("Eté", False, False),
        ("Héroïne", True, False),
        ("Reine", True, False),
        ("Nuage", False, False),
        ("Lune", True, False),
        ("Soleil", False, False),
        ("Vérité", True, False),
        ("Parasite", False, False),
    ],
]
title_adj = [
    ("Brisé", "Brisée"),
    ("Invincible", "Invicible"),
    ("Déchiqueté", "Déchiquetée"),
    ("Fétide", "Fétide"),
    ("Gris", "Grise"),
    ("Mort", "Morte"),
    ("Maudit", "Maudite"),
    ("Noir", "Noire"),
    ("Osseux", "Osseuse"),
    ("Rouge", "Rouge"),
    ("Sombre", "Sombre"),
    ("Ténèbreux", "Ténèbreuse"),
    ("Vil", "Vile"),
    ("Béni", "Bénie"),
    ("Blanc", "Blanche"),
    ("Bleu", "Bleu"),
    ("Courageux", "Courageuse"),
    ("Glorieux", "Glorieuse"),
    ("Juste", "Juste"),
    ("Loyal", "Loyale"),
    ("Lumineux", "Lumineuse"),
    ("Pur", "Pure"),
    ("Vert", "Verte"),
    ("Jaune", "Jaune"),
]

accessories = [
    "aigle",
    "amulette",
    "araignée",
    "arme énorme",
    "armure délabrée",
    "armure",
    "bague",
    "baluchon",
    "bâton de marche",
    "béret",
    "blason",
    "bottes",
    "bougie",
    "bracelet",
    "branche",
    "cache-oeil",
    "canne",
    "casque",
    "ceinture",
    "chapeau",
    "chaudron",
    "chevalière",
    "collier de trophées",
    "collier",
    "corde",
    "coupe de cheveux unique",
    "couronne",
    "croix",
    "cuirasse",
    "cythare",
    "écharpe",
    "écusson",
    "emblème",
    "épaulières",
    "flûte",
    "guitare",
    "hibou",
    "prothèse",
    "insigne",
    "justaucorps",
    "lampe",
    "loup",
    "lyre",
    "manteau",
    "marteau",
    "médaille",
    "médaillon de l'être aimé",
    "nombreux piercings",
    "nombreux tatouages",
    "paire de lunette",
    "parchemin",
    "pentacle",
    "perle",
    "plastron",
    "plume",
    "prothèse",
    "porte bonheur",
    "sac",
    "seau",
    "serpent",
    "tambour",
    "tiare",
    "turban",
    "veste",
    "vêtements de qualité",
    "violon",
]

fantasy_weapons = [
    "Gourdin",
    "Masse",
    "Massue",
    "Matraque",
    "Morgenstern",
    "Discipline",
    "Fléau",
    "Tri-bâton",
    "Maillet",
    "Marteau à deux mains",
    "Marteau de guerre",
    "Piolet",
    "Bouclier de cuir",
    "Bouclier en métal",
    "Pavois",
    "Targe",
    "Bâton",
    "Bâton de guerre",
    "Bâton long",
    "Canne",
    "Chaîne",
    "Chaîne cloutée",
    "Fouet",
    "Bardiche",
    "Hache",
    "Hache de cavalerie",
    "Hache de bataille",
    "Hache double",
    "Hachette",
    "Cimeterre",
    "Coutelas",
    "Sabre",
    "Fleuret",
    "Canne-épée",
    "Rapière",
    "Poignard",
    "Kukri",
    "Crochet",
    "Dague",
    "Dague de poing",
    "Eventail de guerre",
    "Griffe de poing",
    "Main gauche",
    "Rasoir",
    "Serpe",
    "Kama",
    "Stylet",
    "Khopesh",
    "Epée courte",
    "Epée dentelée",
    "Epée bâtarde",
    "Epée longue",
    "Machette",
    "Claymore",
    "Epée double",
    "Espadon",
    "Fauchon",
    "Coutille",
    "Hallebarde",
    "Corsèque",
    "Guisarme",
    "Vouge",
    "Fauchard",
    "Epieu",
    "Fourche",
    "Trident",
    "Lance",
    "Pique",
    "Javelot",
    "Bola",
    "Boomerang",
]

fallout_weapons = [
    "Pistolet .44",
    "Pistolet 10 mm",
    "Pistolet lance-fusées",
    "Fusil d'assault",
    "Fusil de Gauss",
    "Fusil fait-main",
    "Fusil de chasse",
    "Fusil à levier",
    "Fusil au Radium",
    "Fusil à clous",
    "Mitraillette",
    "Fusil à seringues",
    "Carabine de combat",
    "Fusil à deux coups",
    "Pistolet de fortune",
    "Pistolet à verrou",
    "Fat-man",
    "Lance-flammes",
    "Fusil-Harpons",
    "Incinérateur",
    "Junk-Jet",
    "Minigun",
    "Lance-missiles",
    "Laser de l'institut",
    "Mousquet laser",
    "Pistoler laser",
    "Fusil laser",
    "Gatling laser",
    "Pistoler à plasma",
    "Fusil à plasma",
    "Pistolet Gamma",
    "Grenade à fragmentation",
    "Grenade cryogénique",
    "Grenade à gaz",
    "Cocktail Molotov",
    "Grenade à plasma",
    "Grenade à impulsion",
    "Mine à fragmentation",
    "Mine çryogénique",
    "Mine Nuka",
    "Mine à plasma",
    "Mine à impulsion",
    "Couteau de combat",
    "Machette",
    "Scie Buzz de Mister Handy",
    "Épée",
    "Éventreur",
    "Flambeur",
    "Couteau papillon",
    "Batte de baseball",
    "Planche en bois",
    "Tuyau de plomb",
    "Clef anglaise",
    "Queue de billard",
    "Rouleau à patisserie",
    "Masse",
    "Super masse",
    "Clef à pipe",
    "Cane",
    "Gant de boxe",
    "Poing américain",
    "Crochet à viande",
    "Super poing",
]

star_wars_weapons = [
    "pistolet blaster",
    "fusil blaster",
    "vibro-épée",
    "vibro-lame",
    "carabine laser",
    "carabine laser 1",
    "carabine laser 2",
    "carabine laser 3",
    "carabine laser 4",
    "carabine laser 5",
    "carabine laser 6",
    "carabine laser 7",
]


def get_article(noun, gender, plural=False):
    if (
        noun.lower().startswith("e")
        or noun.lower().startswith("é")
        or noun.lower().startswith("a")
        or noun.lower().startswith("â")
        or noun.lower().startswith("u")
        or noun.lower().startswith("o")
        or noun.lower().startswith("i")
        or noun.lower().startswith("h")
    ):
        article = " l'"
    elif plural:
        article = " les "
    else:
        article = [" le ", " la "][gender]
    return article + noun


def get_physical_description(gender):
    return urandom.choice(physical)[gender]


def get_mental_description(gender):
    return urandom.choice(mental)[gender]


def get_trait(gender):
    return urandom.choice(traits)[gender]


def get_title(gender):
    if urandom.random() > 0.5:
        noun, adj_gender, adj_number = urandom.choice(title_noun[gender])
        noun += " "
    else:
        noun, adj_gender, adj_number = "", gender, False
    if noun and urandom.random() < 0.5:
        of_adj, of_gender, of_number = urandom.choice(title_noun[gender])
        if of_number:
            adj = "des " + of_adj
        else:
            adj = "de" + get_article(of_adj, of_gender, False)
            adj = adj.replace("de le", "du")
    else:
        adj = urandom.choice(title_adj)[adj_gender]
        if adj_number:
            if not adj.endswith("s") and not adj.endswith("al") and not adj.endswith("x"):
                adj += "s"
            elif adj.endswith("al"):
                adj = adj[:-1] + "ux"

    return get_article(noun + adj, adj_gender, plural=adj_number)


def get_accessories(*_):
    return urandom.choice(accessories)


def get_f_weapons():
    return urandom.choice(fantasy_weapons)


def get_fo_weapons():
    return urandom.choice(fallout_weapons)


def get_sw_weapons():
    return urandom.choice(star_wars_weapons)


def get_weapons():
    return urandom.choice(fantasy_weapons + fallout_weapons + star_wars_weapons)
