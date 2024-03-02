from descriptions import (
    trophies,
    clothes,
    jewellery,
    equipment,
    food,
    consommable,
    merchandise,
    loot,
)

try:
    import urandom
except ImportError:
    import random as urandom


def d(side: int) -> int:
    return urandom.randint(1, side)


def get_transform() -> str:
    return urandom.choice(trophies + clothes + jewellery + equipment + food + consommable + merchandise + loot)


def get_direction() -> str:
    return urandom.choice(["le nord", "l'est", "le sud", "l'ouest", "le haut", "le bas"])


def get_temporel() -> str:
    return urandom.choice(["secondes", "minutes", "heures", "jours", "mois", "annees"])


def get_chaos() -> str:
    effects = [
        f"soigne {d(4)*25}% de ses blessures max",
        f"transforme en {get_transform()} pendant {d(4)} tours",
        f"implose en {d(4)} tours.",
        "explose, infligeant des degats aux cibles au contact",
        f"se retourne selon l'axe {get_direction()}/{get_direction()}",
        f"voit sa gravité changer vers {get_direction()}",
        f"change de {d(4) - 2:+} gabarits",
        f"se liquiefie en {d(3)} tours",
        "subit les effets d'un sort au hasard",
        "est teleportee vers une autre dimension",
        f"est teleportee {d(20)} m vers {get_direction()}",
        f"va {d(20)} {get_temporel()} dans le futur",
        "trouve le sens de la vie",
        f"se dedouble {d(20)} fois",
        f"devient intangible pendant {d(4)} tours",
        f"est figee pendant {d(4)} tours",
        f"change de type, de matiere, de consistence ou de couleur pendant {d(4)} tours",
        f"subit {d(4)*25}% de ses blessures max",
    ]
    return f"La cible {urandom.choice(effects)}"
