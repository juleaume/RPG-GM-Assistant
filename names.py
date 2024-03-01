import urandom

from descriptions import physical, mental, get_title, get_article

elfique_pref = [
    "Aen",
    "Ala",
    "And",
    "Ar",
    "Cas",
    "Cel",
    "Cyl",
    "El",
    "Eln",
    "Fir",
    "Gael",
    "Hu",
    "Koeh",
    "Laer",
    "Lue",
    "Nail",
    "Rhy",
    "Sere",
    "Tia",
    "Tele",
    "Zau",
]
elfique_suf = [
    "ael",
    "ari",
    "bor",
    "dil",
    "ebrim",
    "eth",
    "eil",
    "evar",
    "ir",
    "mac",
    "mus",
    "oth",
    "rad",
    "re",
    "riel",
    "rond",
    "sar",
    "sil",
    "tahl",
    "thus",
    "uil",
    "vain",
    "wen",
    "wyn",
]
nain_pref = [
    "Bal",
    "Bi",
    "Bjo",
    "Bo",
    "Bom",
    "Dal",
    "Do",
    "Dwa",
    "Dwal",
    "Ein",
    "Fi",
    "Ful",
    "Gar",
    "Gal",
    "Gei",
    "Glo",
    "Hak",
    "Ham",
    "Hroth",
    "Iv",
    "Ke",
    "Ki",
    "Mag",
    "No",
    "O",
    "Odd",
    "Rag",
    "Ran",
    "Sig",
    "Sno",
    "Tar",
    "Thor",
    "Wul",
]
nain_suf = [
    "",
    "ar",
    "bur",
    "dil",
    "f",
    "fur",
    "gar",
    "inn",
    "li",
    "lin",
    "ll",
    "mar",
    "nar",
    "ne",
    "nir",
    "on",
    "os",
    "r",
    "rin",
    "rn",
    "rri",
    "ta",
    "th",
    "ulf",
    "urd",
    "var",
]
humain_m = [
    "Aiden",
    "Bruce",
    "Dirk",
    "Gareth",
    "Gregor",
    "Gustave",
    "Haslten",
    "Harold",
    "Jacques",
    "Jean",
    "Kirk",
    "Lief",
    "Liam",
    "Patrick",
    "Robert",
    "Ronan",
    "Seth",
    "Steven",
    "Tom",
    "William",
]
humain_f = [
    "Abby",
    "Bridget",
    "Cate",
    "Marguerite",
    "Hélène",
    "Hilda",
    "Ingrid",
    "Jessica",
    "Linnea",
    "Maggie",
    "Natalia",
    "Olga",
    "Rebecca",
    "Raelia",
    "Rose",
    "Sarah",
    "Scarlett",
    "Sophia",
    "Tamara",
    "Violette",
]
orque_pref = [
    "Blud",
    "Bruh",
    "Dirg",
    "Dur",
    "Gaz",
    "Gor",
    "Goth",
    "Gut",
    "Lor",
    "Luth",
    "Mag",
    "Nar",
    "Nug",
    "Od",
    "Og",
    "Skum",
    "Teg",
    "Was",
    "Wort",
    "Yag",
]
orque_suf = [
    "bag",
    "brak",
    "dar",
    "dreg",
    "gar",
    "gog",
    "ghul",
    "git",
    "grub",
    "ok",
    "rak",
    "rot",
    "ruk",
    "sarg",
    "shak",
    "sot",
    "tek",
    "thag",
    "tor",
    "zod",
]
reptilien_pre = [
    "Geth",
    "Grath",
    "Gyss",
    "Hyss",
    "Kla",
    "Lath",
    "Lex",
    "Lyth",
    "Mor",
    "Nar",
    "Nyl",
    "Pesh",
    "Ssath",
    "Sser",
    "Ssla",
    "Tla",
    "Xer",
    "Xyl",
    "Xyss",
]
reptilien_suf = [
    "chal",
    "chyss",
    "geth",
    "hesh",
    "hyll",
    "kesh",
    "klatch",
    "lyss",
    "mash",
    "moth",
    "myss",
    "resh",
    "ron",
    "ryn",
    "tetch",
    "tek",
    "thyss",
    "toss",
    "xec",
    "yss",
]


def get_human(gender):
    if gender:
        name = urandom.choice(humain_f)
    else:
        name = urandom.choice(humain_m)
    if urandom.random() > 0.7:
        name += get_title(gender)
    return name


def get_goblin(gender):
    rand = urandom.random()
    if rand > 0.7:
        desc = get_article(urandom.choice(mental + physical)[gender], gender)
    elif rand > 0.2:
        desc = ""
    else:
        desc = get_title(gender)
    return urandom.choice(orque_pref + reptilien_pre) + urandom.choice(orque_suf + reptilien_suf) + desc


def get_elfe(_):
    return (
        urandom.choice(elfique_pref)
        + urandom.choice(elfique_suf)
        + urandom.choice(elfique_suf + [""] * len(elfique_suf) * 2)
        + " "
        + urandom.choice(elfique_pref)
        + urandom.choice(elfique_suf)
    )


def get_dwarf(gender):
    suffix = urandom.choice(nain_suf)
    if urandom.random() > 0.3:
        title = ", fille de " if gender else ", fils de "
        title += urandom.choice(nain_pref) + suffix
    else:
        title = get_title(gender)
    return urandom.choice(nain_pref) + suffix + title


def get_orc(gender):
    if urandom.random() > 0.3:
        desc = get_article(urandom.choice(physical)[gender], gender)
    else:
        desc = get_title(gender)
    return urandom.choice(orque_pref) + urandom.choice(orque_suf) + desc


def get_saurien(gender):
    return (
        urandom.choice(reptilien_pre)
        + urandom.choice(reptilien_suf)
        + get_article(urandom.choice(mental)[gender], gender)
    )
