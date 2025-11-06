from fastapi import FastAPI
import random

app = FastAPI(title="Fantasy Place Generator")

prefixes = [
    "Elder", "Shadow", "Silver", "Iron", "Storm", "Moon", "Dragon",
    "Oak", "Crystal", "Raven", "Frost", "Blood", "Sun", "Mist", "Whisper"
]

middles = [
    "fall", "mire", "haven", "crest", "vale", "spire", "dusk",
    "wood", "ford", "grove", "keep", "peak", "marsh", "reach", "hollow"
]

suffixes = [
    "shire", "hold", "lands", "mere", "gate", "loch", "field",
    "watch", "hollow", "fall", "mount", "moor", "fort", "cliff"
]

def generate_fantasy_place():
    """Gen order"""
    return f"{random.choice(prefixes)} {random.choice(middles)}{random.choice(suffixes)}"

@app.get("/place")
def get_place():
    """Gen one name"""
    return {"place": generate_fantasy_place()}

@app.get("/places/{n}")
def get_places(n: int = 5):
    """Return list of places"""
    return {"places": [generate_fantasy_place() for _ in range(n)]}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Liste ordonnée des suffixes pour les pioches, du plus faible au plus fort
suffixes = [
    "en ruine", "très abîmée", "en mauvais état", "rafistolée", "tordue",  # 1-5
    "douteuse", "usée", "fissurée", "branlante", "fragile",
    "ridée", "délabrée", "bancale", "déséquilibrée", "instable",
    "terne", "éraflée", "défaillante", "démotivée", "peu fiable",
    # 21-40
    "abîmée", "fatiguée", "usée par le temps", "mal ajustée", "peu solide",
    "inconsistante", "sous-performante", "délaissée", "négligée", "déformée",
    "terne", "approximative", "intacte mais ordinaire", "fonctionnelle", "acceptable",
    "standard", "commune", "correcte", "simple", "utilitaire",
    # 41-60
    "ajustée", "robuste", "solide", "raffinée", "pratique",
    "efficace", "stable", "soignée", "bien faite", "fiable",
    "poli", "équilibrée", "de bonne facture", "convenable", "appréciée",
    "fonctionnelle et robuste", "confortable", "bien entretenue", "renforcée", "exemplaire",
    # 61-80
    "précise", "aiguisée", "revêtue de cuivre", "affûtée",
    "en acier poli", "soigneusement façonnée", "cohérente", "de bonne réputation", "presque parfaite", "sans défaut apparent",
    "bien équilibrée", "finement travaillée", "en acier de qualité", "aux reflets métalliques", "à poignée solide",
    "usinée à la perfection", "élégante", "en argent poli", "efficacement forgée", "respectée",
    # 81-100
    "magnifique", "d’atelier renommé", "hautement respectée", "fleurie de gravures simples", "ornée discrètement",
    "à finesse maîtrisée", "trempée avec soin", "au tranchant net", "à longue durée", "hautement appréciée",
    "en métal pur", "sobre mais efficace", "gravée de qualité", "à manche résistant", "racée",
    # 101-120
    "lustreuse", "soyeuse", "belle", "haute performance", "sans accrocs",
    "spécialement conçue", "artisanale", "ciselée avec soin", "prestigieuse", "réputée",
    "diamantée", "précieuse", "à pointe cristalline", "lumineuse", "à reflets multiples",
    "d’artisan expert", "noble", "augmentée de runes", "résonnante", "intrinsèquement magique",
    # 121-140
    "aux inscriptions sacrées", "en acier trempé", "de maître forgeron", "bénie par un prêtre", "délicate mais solide",
    "en or pur", "d’un savoir oublié", "trempée dans la lave", "à âme cristalline", "aux reflets bleutés",
    "runique", "fabriquée avec soin ancestral", "à pointe incassable", "issue du savoir nain", "irréprochable",
    # 141-160
    "remarquable", "noble et fière", "auréolée de lumière", "augmentée d’un sceau sacré", "en acier céleste",
    "enchantée", "aux gravures majestueuses", "d’esprit antique", "pure et noble", "digne d’un seigneur",
    "en pierre de lune", "baignée dans la magie", "liée aux étoiles", "de toute beauté", "parfaite",
    # 161-180
    "transcendante", "glorieuse", "lumineuse", "aux énergies élémentaires", "céleste",
    "baignée de lumière sacrée", "aux chants anciens", "sacralisée", "avec présence ancestrale", "révérée",
    "forgée par les nains légendaires", "destinée à un roi", "héroïque", "à éclat éternel", "mythique",
    # 181-200
    "enchâssée de cristaux sacrés", "portée par les héros", "issue d’une prophétie", "au pouvoir sacré",
    "de grande renommée", "aux échos mystiques", "inspirée par les dieux", "chérie par les anges",
    "au tranchant astral", "issue des étoiles", "pure et éternelle", "dominatrice", "salutaire",
    # 201-230
    "aux pouvoirs divins", "trempée dans la lumière d’un dragon", "parfaite en tous points", "emblématique",
    "ancêtre magique", "dotée d’un éclat sublime", "forgée par les mains divines", "trônant dans la gloire",
    "issue du cœur d’un volcan sacré", "parfaite incarnation du savoir-faire",
    "conçue pour les dieux", "d’une absolue clarté", "lumineuse et pure", "éternelle",
    # 231-250
    "sacrée", "emblème de puissance", "transcendante", "forgée par les dieux", "mythique",
    "surnaturelle", "épique", "d’or étincelant", "ultime", "légendaire"
]

@app.get("/pioche")
async def generate_pickaxe():
    quality_index = random.randint(1, len(suffixes))
    suffix = suffixes[quality_index - 1]  # -1 car les indices Python commencent à 0
    return {"pioche": f"Pioche {suffix}", "qualite": quality_index}
