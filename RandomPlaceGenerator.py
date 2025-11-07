from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Fantasy Place & Pickaxe Generator")

# Autoriser toutes les origines (pour usage web)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# 🚩 GÉNÉRATEUR DE LIEUX
# ==============================

prefixes = [
    "Elder", "Shadow", "Silver", "Iron", "Storm", "Moon", "Dragon", "Oak",
    "Crystal", "Raven", "Frost", "Blood", "Sun", "Mist", "Whisper",
    "Twilight", "Ember", "Golden", "Dark", "Ash", "Wind", "Wolf", "Fire",
    "Stone", "Cloud", "Night", "Ice", "Bright", "Star", "Thorn"
]

middles = [
    "fall", "mire", "haven", "crest", "vale", "spire", "dusk", "wood",
    "ford", "grove", "keep", "peak", "marsh", "reach", "hollow",
    "watch", "brook", "meadow", "ridge", "moor", "cairn", "run", "field",
    "gate", "fort", "bay", "shore", "rift", "den", "rock"
]

suffixes_places = [
    "shire", "hold", "lands", "mere", "gate", "loch", "field",
    "watch", "hollow", "fall", "mount", "moor", "fort", "cliff",
    "vale", "pass", "rest", "stone", "keep", "crown", "reach", "thorn",
    "grove", "point", "bluff", "ridge", "cross", "hall", "rock", "bastion"
]

def generate_fantasy_place():
    return f"{random.choice(prefixes)} {random.choice(middles)}{random.choice(suffixes_places)}"

@app.get("/place")
def get_place():
    return {"place": generate_fantasy_place()}

@app.get("/places/{n}")
def get_places(n: int = 5):
    return {"places": [generate_fantasy_place() for _ in range(n)]}

# ==============================
# ⚒️ GÉNÉRATEUR DE PIOCHES
# ==============================

suffixes_pioches = [
    # 1–100 : très mauvaise qualité
    "cassée", "en ruine", "abîmée", "tordue", "fragile", "fissurée", "usée",
    "branlante", "mal forgée", "émoussée", "déformée", "instable", "lente",
    "peu fiable", "grossière", "ternie", "imparfaite", "endommagée", "faible",
    "douteuse", "instable", "défaillante", "primitive", "rudimentaire",
    "mal équilibrée", "incomplète", "abîmée par le temps", "mal taillée",
    "brûlée", "pliée", "inégale", "éraflée", "rafistolée", "bancale",
    "négligée", "mal entretenue", "improvisée", "ordinaire", "lourde",
    "en mauvais état", "terne", "fatiguée", "usée par l’usage", "mal polie",
    "ancienne", "de fortune", "mal conçue", "décalée", "déséquilibrée",
    "faiblement forgée", "grossièrement taillée",
    # 101–200 : qualité moyenne
    "acceptable", "fonctionnelle", "commune", "solide", "de base", "correcte",
    "standard", "classique", "poli", "fiable", "simple", "ajustée",
    "stabilisée", "ordinaire mais utile", "utile", "équilibrée", "renforcée",
    "raffinée", "bien taillée", "robuste", "soignée", "usuelle", "propre",
    "de bonne facture", "opérationnelle", "régulière", "affûtée", "stable",
    "bien conçue", "correctement forgée", "fonctionnelle et solide",
    "bien entretenue", "durable", "équilibrée", "ferme", "digne", "soigneuse",
    "en bon état", "poli à la main", "standard renforcée",
    # 201–300 : bonne qualité
    "en acier poli", "affûtée", "renforcée", "équilibrée", "précise",
    "efficace", "de qualité", "bien travaillée", "affinée", "agréable",
    "soigneusement polie", "finement taillée", "à poignée solide",
    "au tranchant net", "en acier trempé", "en fer pur", "de bonne réputation",
    "bien équilibrée", "stable et fiable", "respectée", "revêtue d’argent",
    "raffinée à la main", "artisanale", "noble", "robuste et élégante",
    "lumineuse", "agréablement équilibrée", "sûre", "fiable et solide",
    "au poli éclatant", "brillante", "à manche renforcé",
    "taillée avec précision", "agréablement forgée",
    # 301–400 : rare et magique
    "ornée", "gravée", "en argent poli", "runique", "enchantée",
    "bénie", "rare", "d’atelier renommé", "aux reflets bleus", "gravée d’or",
    "aux runes anciennes", "aux motifs nains", "aux symboles anciens",
    "en acier mystique", "forgée dans la lave", "aux éclats d’argent",
    "aux reflets mystiques", "chargée d’énergie", "aux gravures fines",
    "pure", "aux gemmes incrustées", "aux reflets argentés",
    "magique", "mystique", "d’énergie stable", "sacrée", "aux éclats runiques",
    "aux gravures elfiques", "en métal béni", "aux marques anciennes",
    "aux reflets célestes", "bénie par la lumière", "aux ornements sacrés",
    "énergisée", "aux pierres précieuses", "aux symboles magiques",
    "aux chants anciens", "aux vibrations étranges", "aux reflets lunaires",
    "aux reflets d’or", "aux symboles bénis", "magiquement pure",
    "transcendée", "aux éclats bleus", "aux reflets divins",
    # 401–500 : épique → légendaire
    "divine", "sacrée", "céleste", "mythique", "légendaire", "draconique",
    "angélique", "du crépuscule", "de l’aube", "ancestrale", "glorieuse",
    "des anciens", "de la lumière", "du néant", "du firmament", "du phénix",
    "du destin", "éternelle", "du dragon", "ultime", "suprême", "des dieux",
    "célestiale", "primordiale", "du monde ancien", "d’or pur", "lumineuse",
    "brillante", "parfaite", "sublime", "noble", "royale", "transcendante",
    "enchanteresse", "unique", "prophétique", "immortelle", "de la création",
    "infinie", "cosmique", "spectrale", "divinisée", "sainte", "fantastique",
    "miraculeuse", "du firmament", "des cieux", "ultime", "légendaire absolue"
]

@app.get("/pioche")
async def generate_pickaxe():
    quality_index = random.randint(1, len(suffixes_pioches))
    suffix = suffixes_pioches[quality_index - 1]
    return {"pioche": f"Pioche {suffix}", "qualite": quality_index}
