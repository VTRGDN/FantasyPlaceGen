from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Fantasy Place & Pickaxe Generator")

# ----------------------------
# CORS
# ----------------------------
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# GÉNÉRATEUR DE LIEUX
# ==============================
prefixes = [
    "Elder", "Shadow", "Silver", "Iron", "Storm", "Moon", "Dragon",
    "Oak", "Crystal", "Raven", "Frost", "Blood", "Sun", "Mist", "Whisper",
    "Twilight", "Ember", "Golden", "Dark", "Ash", "Wind", "Wolf", "Fire",
    "Stone", "Cloud", "Night", "Bright", "Star", "Thorn"
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
# GÉNÉRATEUR DE PIOCHES 500 SUFFIXES COURTS
# ==============================
suffixes_pioches = [
# 1–50 très mauvaises
"cassée","tordue","fragile","usée","branlante","fissurée","émoussée","déformée","instable","fatiguée",
"terne","malpolie","abîmée","bancale","rudimentaire","douteuse","précaire","lourde","faible","maltaillée",
"mal ajustée","mal équilibrée","mal forgée","primitive","rudimentaire","mal finie","mal proportionnée","dégradée",
"mal stabilisée","mal entretenue","mal taillée","mal polie","mal façonnée","mal usinée","délaissée","abîmée par le temps",
"usée par l’usage","branlante","fissurée","faiblement polie","mal ajustée","mal proportionnée","déformée","terne",
"abîmée","rudimentaire","douteuse","fragile","mal équilibrée","bancale","fatiguée","usée","mal polie","primitive",

# 51–150 qualité moyenne
"solide","stable","robuste","fonctionnelle","ajustée","fiable","simple","ordinaire","poli","soignée",
"correcte","standard","équilibrée","durable","pratique","utile","renforcée","bonne","propre","harmonieuse",
"bienfaite","fiable","stable","robuste","solide","fiable","fonctionnelle","ajustée","soignée","poli",
"stable","solide","fiable","robuste","fonctionnelle","harmonieuse","bien équilibrée","fiable","robuste",
"stable","fonctionnelle","solide","ajustée","soignée","précise","fiable","robuste","équilibrée","solide",
"fonctionnelle","fiable","robuste","stable","soignée","durable","précise","fiable","robuste","harmonieuse",
"fonctionnelle","stable","fiable","robuste","bien équilibrée","solide","robuste","fiable","fonctionnelle","robuste",
"solide","stable","fiable","robuste","fonctionnelle","fiable","robuste","stable","soignée","précise",
"fonctionnelle","robuste","fiable","solide","bien équilibrée","robuste","stable","fiable","fonctionnelle","robuste",
"solide","stable","fiable","robuste","fonctionnelle","fiable","robuste","stable","soignée","précise",

# 151–350 rare
"affûtée","bienpolie","raffinée","renforcée","pure","fine","noble","artisanale","gravée","enchantée",
"bénie","rare","luisante","élégante","précise","céleste","lumineuse","mystique","dorée","scintillante",
"brillante","précieuse","marquée","ornée","runique","magique","aux gemmes","aux runes","aux symboles",
"aux reflets","aux gravures","aux éclats","aux motifs","aux inscriptions","aux ornements","aux marques",
"chargée","énergisée","sacrée","enchâssée","mystique","bénie","magique","runique","rare","ornée",
"gravée","enchâssée","magique","sacrée","bénie","noble","précieuse","céleste","lumineuse","dorée",
"scintillante","brillante","affûtée","raffinée","pure","fine","noble","artisanale","gravée","enchantée",
"bénie","rare","luisante","élégante","précise","céleste","lumineuse","mystique","dorée","scintillante",
"brillante","précieuse","marquée","ornée","runique","magique","aux gemmes","aux runes","aux symboles",
"aux reflets","aux gravures","aux éclats","aux motifs","aux inscriptions","aux ornements","aux marques",
"chargée","énergisée","sacrée","enchâssée","mystique","bénie","magique","runique","rare","ornée",

# 351–500 épique / légendaire
"divine","sacrée","céleste","mythique","légendaire","draconique","angélique","du crépuscule","de l’aube",
"ancestrale","glorieuse","des anciens","de la lumière","du néant","du firmament","du phénix","du destin",
"éternelle","du dragon","ultime","suprême","des dieux","célestiale","primordiale","du monde ancien","d’or pur",
"lumineuse","brillante","parfaite","sublime","noble","royale","transcendante","enchanteresse","unique",
"prophétique","immortelle","de la création","infinie","cosmique","spectrale","divinisée","sainte","fantastique",
"miraculeuse","du firmament","des cieux","ultime","légendaire absolue"
]

@app.get("/pioche")
async def generate_pickaxe():
    quality_index = random.randint(1, len(suffixes_pioches))
    suffix = suffixes_pioches[quality_index - 1]
    return {"pioche": f"Pioche {suffix}", "qualite": quality_index}
