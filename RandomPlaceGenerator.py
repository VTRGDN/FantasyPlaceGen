from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Fantasy Place Generator")

# -----------------------
# CORS
# -----------------------
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Générateur de lieux (inchangé)
# -----------------------
prefixes = [
    "Elder", "Shadow", "Silver", "Iron", "Storm", "Moon", "Dragon",
    "Oak", "Crystal", "Raven", "Frost", "Blood", "Sun", "Mist", "Whisper"
]

middles = [
    "fall", "mire", "haven", "crest", "vale", "spire", "dusk",
    "wood", "ford", "grove", "keep", "peak", "marsh", "reach", "hollow"
]

suffixes_lieux = [
    "shire", "hold", "lands", "mere", "gate", "loch", "field",
    "watch", "hollow", "fall", "mount", "moor", "fort", "cliff"
]

def generate_fantasy_place():
    return f"{random.choice(prefixes)} {random.choice(middles)}{random.choice(suffixes_lieux)}"

@app.get("/place")
def get_place():
    return {"place": generate_fantasy_place()}

@app.get("/places/{n}")
def get_places(n: int = 5):
    return {"places": [generate_fantasy_place() for _ in range(n)]}

# -----------------------
# Générateur de pioches avec 500 suffixes hiérarchisés
# -----------------------
suffixes_pioches = [
"cassée","tordue","fragile","usée","émoussée","abîmée","fendue","déformée","branlante","terne",
"lourde","instable","bancale","grossière","mal taillée","imparfaite","faible","fatiguée","ébréchée","endommagée",
"mal ajustée","décentrée","écaillée","dégradée","mal forgée","mal finie","inégale","désunie","primitive","douteuse",
"improvisée","mal entretenue","rudimentaire","mal proportionnée","usée par le temps","terne et usée","très usée","presque brisée","de fortune",
"faiblement forgée","déséquilibrée","mal trempée","de piètre qualité","instable","abîmée par l’usage","mal réparée","mauvaise","moche","trop lourde",
"ordinaire","simple","commune","basique","fonctionnelle","acceptable","standard","correcte","utilitaire","passable",
"modeste","adaptée","fiable","rustique","stabilisée","ajustée","pratique","robuste","fiable et stable","simple mais efficace",
"robuste mais lourde","correcte et durable","équilibrée et stable","solide et correcte","fiable et utile","ordinaire mais durable","stable et correcte","solide","robuste","stable",
"fiable","fonctionnelle","soignée","durable","équilibrée","raffinée","propre","bien faite","pratique","harmonieuse",
"agréable","soigneuse","ajustée et solide","simple et pratique","équilibrée et fiable","soignée et robuste","stable et durable","robuste et efficace","fiable et équilibrée","robuste et soignée",
"précise","fiable et robuste","solide et stable","équilibrée et solide","robuste et fiable","durable et stable","fiable et efficace","fonctionnelle et solide","soignée et équilibrée","ajustée et robuste",
"propre et stable","fiable et soignée","robuste et durable","fiable et stable","fonctionnelle et fiable","stable et équilibrée","robuste et précise","fiable et solide","robuste et pratique","solide et efficace",
"affûtée","bien polie","renforcée","de bonne qualité","brillante","en bon état","raffinée","bien équilibrée","soigneusement faite","bien forgée",
"fiable et polie","soignée et précise","raffinée et stable","bien entretenue","précise et stable","robuste et élégante","fiable et polie","équilibrée et polie","fiable et brillante","soignée et brillante",
"raffinée et durable","bien proportionnée","robuste et lisse","fiable et soignée","agréablement équilibrée","soigneusement forgée","propre et brillante","précise et efficace","robuste et harmonieuse","parfaite","lumineuse","aiguisée","finement polie","bien affûtée","aux reflets métalliques","aux bords nets",
"équilibrée à la perfection","soyeuse","d’apparence noble","d’une forge reconnue","d’alliage pur","éclatante","affûtée à la perfection","revêtue d’argent","brillante et solide","bien trempée","sans défaut","de belle facture","soigneusement polie","aux gravures fines","en métal pur","bien équilibrée et polie",
"raffinée et pure","élégante","magnifique","gracieuse","bien trempée","précise et élégante","aux reflets bleutés","d’une belle brillance","de qualité supérieure","équilibrée et noble","à luisance propre","finement équilibrée","de bonne réputation","aux détails précis","pure et nette","harmonieuse et brillante","travaillée avec soin","à manche poli","raffinée et claire","en métal noble","aux lignes parfaites","à finition propre","d’artisan experte","noble","runique","gravée","ornée","charmée","bénie des anciens","aux reflets magiques","sacralisée","enchantée","belle et brillante","de forge ancienne","augurée","dorée","lumineuse et pure","ornée de runes","gravée avec soin","aux motifs anciens","aux reflets d’or","runique et équilibrée","énergisée","d’esprit ancien","chargée d’énergie","vibrante","chantante","lumineuse et stable","pure et rare",
"aux gravures soignées","dorée et polie","resplendissante","magique","aux pouvoirs anciens","aux inscriptions fines","rare et équilibrée","raffinée et magique","bénie et brillante","aux lueurs argentées","d’une aura douce","lumineuse et noble","de prestige","mythique","divine","légendaire","d’obsidienne","de mithril","d’adamantium","d’argent pur","d’or pur","de platine","d’onyx","de topaze","d’émeraude","de rubis","de saphir","de diamant","de cristal","de cristal pur","raffinée de cristal","polie de diamant","affûtée de rubis","soignée de saphir","équilibrée d’émeraude","robuste de topaze","fiable d’onyx","brillante de platine","légendaire de mithril","ultime d’adamantium","sacrée d’or","divine d’argent","pure d’obsidienne","énergisée de cristal","resplendissante de diamant","enchâssée de rubis","ornée de saphir","magnifique d’émeraude","précieuse de topaze","inestimable d’onyx","prestigieuse de platine","noble de mithril","rare d’adamantium","féerique d’or","mythique d’argent","légendaire de cristal","ultime de diamant","sacrée de rubis","divine de saphir","pure d’émeraude","énergisée de topaze","resplendissante d’onyx","enchâssée de platine","ornée de mithril","magnifique d’adamantium","précieuse d’or","inestimable d’argent","prestigieuse de cristal","noble de diamant","rare de rubis","féerique de saphir","mythique d’émeraude","légendaire de topaze","ultime d’onyx","sacrée de platine","divine de mithril","pure d’adamantium","énergisée d’or","resplendissante d’argent","enchâssée de cristal","ornée de diamant","magnifique de rubis","précieuse de saphir","inestimable d’émeraude","prestigieuse de topaze","noble d’onyx","rare de platine","féerique de mithril","mythique d’adamantium","légendaire d’or","ultime d’argent","sacrée de cristal","divine de diamant","pure de rubis","énergisée de saphir","resplendissante d’émeraude","enchâssée de topaze","ornée d’onyx","magnifique de platine","précieuse de mithril","inestimable d’adamantium","prestigieuse d’or","noble d’argent","rare de cristal","féerique de diamant","mythique de rubis","légendaire de saphir","ultime d’émeraude","sacrée de topaze","divine d’onyx","pure de platine","énergisée de mithril","resplendissante d’adamantium","enchâssée d’or","ornée d’argent","magnifique de cristal","précieuse de diamant","inestimable de rubis","prestigieuse de saphir","noble d’émeraude","rare de topaze","féerique d’onyx","mythique de platine","légendaire de mithril","ultime d’adamantium","sacrée d’or","divine d’argent","pure de cristal","énergisée de diamant","resplendissante de rubis","enchâssée de saphir","ornée d’émeraude","magnifique de topaze","précieuse d’onyx","inestimable de platine","prestigieuse de mithril","noble d’adamantium","rare d’or","féerique d’argent","mythique de cristal","légendaire de diamant","ultime de rubis","sacrée de saphir","divine d’émeraude","pure de topaze","énergisée d’onyx","resplendissante de platine","enchâssée de mithril","ornée d’adamantium","magnifique d’or","précieuse d’argent","inestimable de cristal","prestigieuse de diamant","noble de rubis","rare de saphir","féerique d’émeraude","mythique de topaze","légendaire d’onyx","ultime de platine","sacrée de mithril","divine d’adamantium","pure d’or","énergisée d’argent","resplendissante de cristal","enchâssée de diamant","ornée de rubis","magnifique de saphir","précieuse d’émeraude","inestimable de topaze","prestigieuse d’onyx","noble de platine","rare de mithril","féerique d’adamantium","mythique d’or","légendaire d’argent","ultime de cristal","sacrée de diamant","divine de rubis","pure de saphir","énergisée d’émeraude","resplendissante de topaze","enchâssée d’onyx","ornée de platine","magnifique de mithril","précieuse d’adamantium","inestimable d’or","prestigieuse d’argent","noble de cristal","rare de diamant","féerique de rubis","mythique de saphir","légendaire d’émeraude","ultime de topaze","sacrée d’onyx","divine de platine","pure de mithril","énergisée d’adamantium","resplendissante d’or","enchâssée d’argent","ornée de cristal","magnifique de diamant","précieuse de rubis","inestimable de saphir","prestigieuse d’émeraude","noble de topaze","rare d’onyx","féerique de platine","mythique de mithril","légendaire d’adamantium","ultime d’or","sacrée d’argent","divine de cristal","pure de diamant","énergisée de rubis","resplendissante de saphir","enchâssée d’émeraude","ornée de topaze","magnifique d’onyx","précieuse de platine","inestimable de mithril","prestigieuse d’adamantium","noble d’or","rare d’argent","féerique de cristal","mythique de diamant","légendaire de rubis","ultime de saphir","sacrée d’émeraude","divine de topaze","pure d’onyx","énergisée de platine","resplendissante de mithril","enchâssée d’adamantium","ornée d’or","magnifique d’argent","précieuse de cristal","inestimable de diamant","prestigieuse de rubis","noble de saphir","rare d’émeraude","féerique de topaze","mythique d’onyx","légendaire de platine","ultime de mithril","sacrée d’adamantium","divine d’or","pure d’argent","énergisée de cristal","resplendissante de diamant","enchâssée de rubis","ornée de saphir","magnifique d’émeraude","précieuse de topaze","inestimable d’onyx","prestigieuse de platine","noble de mithril","rare d’adamantium","féerique d’or","mythique d’argent","légendaire de cristal","ultime de diamant","sacrée de rubis","divine de saphir","pure d’émeraude","énergisée de topaze","resplendissante d’onyx","enchâssée de platine","ornée de mithril","magnifique d’adamantium","précieuse d’or","inestimable d’argent","prestigieuse de cristal","noble de diamant","rare de rubis","féerique de saphir","mythique d’émeraude","légendaire de topaze","ultime d’onyx","sacrée de platine","divine de mithril","pure d’adamantium","énergisée d’or","resplendissante d’argent","enchâssée de cristal","ornée de diamant","magnifique de rubis","précieuse de saphir","inestimable d’émeraude","prestigieuse de topaze","noble d’onyx","rare de platine","féerique de mithril","mythique d’adamantium","légendaire d’or","ultime d’argent","sacrée de cristal","divine de diamant","pure de rubis","énergisée de saphir","resplendissante d’émeraude","enchâssée de topaze","ornée d’onyx","magnifique de platine","précieuse de mithril","inestimable d’adamantium","prestigieuse d’or","noble d’argent","rare de cristal","féerique de diamant","mythique de rubis","légendaire de saphir","ultime d’émeraude","sacrée de topaze","divine d’onyx","pure de platine","énergisée de mithril","resplendissante d’adamantium","enchâssée d’or","ornée d’argent","magnifique de cristal","précieuse de diamant","inestimable de rubis","prestigieuse de saphir","noble d’émeraude","rare de topaze","féerique d’onyx","mythique de platine","légendaire de mithril","ultime d’adamantium","de cristal légendaire"
]

@app.get("/pioche")
async def generate_pickaxe():
    suffix_index = random.randint(0, len(suffixes_pioches) - 1)
    suffix = suffixes_pioches[suffix_index]
    qualite = suffix_index + 1
    return {"pioche": f"Pioche {suffix}", "qualite": qualite}
