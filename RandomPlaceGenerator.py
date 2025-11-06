from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Fantasy Place and Pickaxe Generator")

# CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------
# GENERATEUR DE LIEUX
# ---------------------

prefixes = [
    "Elder", "Shadow", "Silver", "Iron", "Storm", "Moon", "Dragon",
    "Oak", "Crystal", "Raven", "Frost", "Blood", "Sun", "Mist", "Whisper"
]

middles = [
    "fall", "mire", "haven", "crest", "vale", "spire", "dusk",
    "wood", "ford", "grove", "keep", "peak", "marsh", "reach", "hollow"
]

suffixes_places = [
    "shire", "hold", "lands", "mere", "gate", "loch", "field",
    "watch", "hollow", "fall", "mount", "moor", "fort", "cliff",
    # Doublons pour augmenter le nombre de lieux
    "vale", "spire", "grove", "peak", "ford", "mire", "keep",
    "hollow", "loch", "mount", "moor", "cliff", "gate", "field"
]

def generate_fantasy_place():
    return f"{random.choice(prefixes)} {random.choice(middles)}{random.choice(suffixes_places)}"

@app.get("/place")
def get_place():
    return {"place": generate_fantasy_place()}

@app.get("/places/{n}")
def get_places(n: int = 5):
    return {"places": [generate_fantasy_place() for _ in range(n)]}

# ----------------------
# GENERATEUR DE PIOCHES
# ----------------------

# Liste de 500 suffixes, du plus mauvais au légendaire
suffixes_pickaxes = [
    # 1-50 très mauvais
    "en ruine", "bancale", "usée", "fragile", "délabrée", "tordue", "mal équilibrée",
    "très abîmée", "rafistolée", "ébréchée", "abîmée", "fatiguée", "peu fiable",
    "défaillante", "mal ajustée", "branlante", "terne", "éraflée", "déséquilibrée",
    "déformée", "instable", "douteuse", "malchanceuse", "négligée", "cassée",
    "sous-performante", "mal ficelée", "mal forgée", "fragilisée", "usée par le temps",
    "bancale et usée", "faiblement forgée", "inconsistante", "mal entretenue", "délaissée",
    "déglinguée", "défectueuse", "peu solide", "grumeleuse", "terne et usée",
    "mal proportionnée", "mal finie", "légèrement tordue", "dégradée", "éclatée",
    "terne et fragile", "mal façonnée", "d'une qualité douteuse", "prête à casser", "minable",
    # 51-150 médiocre / ordinaire
    "correcte", "standard", "commune", "simple", "fonctionnelle", "acceptable",
    "robuste", "équilibrée", "stable", "pratique", "solide", "fiable",
    "poli", "bien faite", "ajustée", "décent", "fonctionnelle et robuste", "confortable",
    "bien entretenue", "renforcée", "exemplaire", "adéquate", "modeste", "utilitaire",
    "basique", "courante", "ordinaire", "moyenne", "standardisée", "routine",
    "banale", "satisfaisante", "raisonnable", "conventionnelle", "prête à l'usage",
    "normale", "appréciable", "solide mais simple", "bonne facture", "fiabilité moyenne",
    "acceptable mais ordinaire", "équilibrée et pratique", "raisonnablement solide", "stable et correcte",
    "robuste mais simple", "en acier ordinaire", "polie mais simple", "fonctionnelle sans plus",
    "sans éclat", "utile mais commune", "courante et robuste", "moyennement efficace", "stable et fiable",
    "fiable mais banale", "bonne mais sans charme", "correcte et solide", "acceptable et pratique",
    "digne d'un mineur", "standard mais fiable", "moyenne mais fonctionnelle", "commune mais solide",
    "solide et moyenne", "prête pour le travail", "fonctionnelle mais ordinaire", "robuste mais banale",
    "modeste mais fiable", "bonne mais simple", "solide mais peu impressionnante", "moyenne et équilibrée",
    "pratique et commune", "utilitaire mais robuste", "banale mais fonctionnelle", "corrigée", "réparée",
    "refaite à neuf", "fonctionnelle mais médiocre", "fiable mais ordinaire", "moyennement robuste",
    "stable et pratique", "correcte pour le quotidien", "bonne mais sans éclat", "digne mais ordinaire",
    "acceptable pour un mineur", "fonctionnelle mais sans magie", "robuste mais ordinaire", "fiable mais basique",
    "standardisée et robuste", "utilitaire et efficace", "robuste mais sans charme", "fonctionnelle et moyenne",
    "corrigée mais ordinaire", "prête à l'emploi", "fiable mais basique", "solide mais simple", "banale mais correcte",
    "moyenne et utile", "commune mais robuste", "robuste et standard", "acceptable et stable", "correcte et pratique",
    "solide mais ordinaire", "moyennement utile", "fonctionnelle mais banale", "fiable et moyenne", "prête pour le travail quotidien",
    "stable mais ordinaire", "bonne mais modeste", "corrigée et fonctionnelle", "robuste mais basique", "standard et solide",
    "modeste mais pratique", "fiable mais ordinaire", "acceptable et correcte", "banale mais stable", "moyennement robuste",
    "solide mais ordinaire", "fonctionnelle et moyenne", "robuste mais commune", "fiable mais simple", "prête à l'usage",
    # 151-300 bonne / rare
    "raffinée", "efficace", "élégante", "fine", "soignée", "ajustée avec soin", "bien proportionnée",
    "très robuste", "affûtée", "en acier poli", "bien équilibrée", "en métal de qualité", "respectée",
    "ornée discrètement", "hautement appréciée", "poli et fonctionnel", "précise", "solide et fiable",
    "hautement fonctionnelle", "robuste et fine", "élégante et pratique", "bien conçue", "finement travaillée",
    "artisanale", "de bonne facture", "renforcée et stable", "bien forgée", "efficace et fiable",
    "fiable et durable", "robuste et raffinée", "fonctionnelle et élégante", "hautement stable", "bien proportionnée",
    "équilibrée et solide", "soignée et fine", "robuste et pratique", "efficacement forgée", "bien entretenue",
    "stable et précise", "fiable et fonctionnelle", "élégante et solide", "soignée et robuste", "raffinée et fiable",
    "robuste et efficace", "bien équilibrée et fiable", "précise et durable", "bien finie", "ajustée et solide",
    "robuste et harmonieuse", "fonctionnelle et raffinée", "fiable et bien forgée", "élégante et stable",
    "solide et bien proportionnée", "hautement fonctionnelle et fiable", "robuste et précise", "efficace et robuste",
    "bien équilibrée et stable", "fiable et bien entretenue", "fonctionnelle et harmonieuse", "soignée et efficace",
    "raffinée et durable", "robuste et bien finie", "élégante et fonctionnelle", "précise et stable", "solide et raffinée",
    "hautement robuste", "fiable et bien proportionnée", "robuste et fonctionnelle", "précise et fiable", "bien équilibrée et durable",
    "robuste et bien entretenue", "élégante et efficace", "solide et fonctionnelle", "raffinée et stable", "fiable et durable",
    "bien forgée et équilibrée", "robuste et harmonieuse", "fonctionnelle et fiable", "soignée et stable", "précise et durable",
    "élégante et robuste", "robuste et raffinée", "fiable et efficace", "bien proportionnée et solide", "fonctionnelle et harmonieuse",
    "hautement robuste et fiable", "robuste et précise et fiable", "élégante et durable", "solide et raffinée", "fiable et bien équilibrée",
    "robuste et stable et fonctionnelle", "bien finie et fiable", "précise et efficace", "robuste et fiable et solide", "hautement fonctionnelle et robuste",
    # 301-400 très haute / épique
    "enchâssée de gemmes", "runique", "enchanted", "forgée par les nains", "en acier trempé",
    "baignée de magie", "aux gravures anciennes", "à pointe incassable", "mythique", "héroïque",
    "destinée aux rois", "transcendante", "glorieuse", "lumineuse", "sacralisée",
    "baignée de lumière", "aux chants anciens", "révérée", "forgée par des maîtres légendaires",
    "digne d'un héros", "puissante", "ultime", "surnaturelle", "épique",
    "de grande renommée", "majestueuse", "portée par les champions", "issue d'une prophétie", "emblématique",
    "dominatrice", "pure et éternelle", "au tranchant astral", "dotée d'un éclat sublime", "forgée par les mains divines",
    "trônant dans la gloire", "issue des étoiles", "parfaite en tous points", "aux pouvoirs divins", "trempée dans la lumière d'un dragon",
    "inspirée par les dieux", "magnifique", "sacrée", "mythique et légendaire", "ultime et parfaite",
    # 401-500 légendaire / divin
    "légendaire", "ultime", "divine", "surnaturelle", "épique", "transcendante",
    "forgée par les dieux", "mythique", "sacrée", "emblème de puissance", "ultime chef-d'œuvre",
    "lumière éternelle", "d'or étincelant", "pour les rois", "destinée aux héros", "divinement forgée",
    "à la gloire des ancêtres", "extraordinaire", "invincible", "suprême", "inégalée",
    "légendaire et immortelle", "ultime puissance", "divine perfection", "mythique et sacrée", "épique et légendaire",
    "transcendante et lumineuse", "forgée par la lumière des étoiles", "immortelle", "d’une rareté absolue",
    "ultime création", "chef-d'œuvre des dieux", "invincible et sacrée", "légendaire et divine", "mythique et suprême",
    "éternelle", "surnaturelle et immortelle", "ultime et parfaite", "divinement puissante", "légendaire et épique",
    "mythique et transcendante", "ultime et lumineuse", "sacrée et immortelle", "divine et parfaite", "légendaire et mythique",
    "chef-d'œuvre éternel", "forgée par les dieux suprêmes", "ultime et surnaturelle", "mythique et invincible", "légendaire absolue"
]

@app.get("/pioche")
async def generate_pickaxe():
    quality_index = random.randint(1, len(suffixes_pickaxes))
    suffix = suffixes_pickaxes[quality_index - 1]
    return {"pioche": f"Pioche {suffix}", "qualite": quality_index}
