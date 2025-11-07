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
# Générateur de lieux
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
# Générateur de pioches                                            
# -----------------------
suffixes_pioches = [
"cassée","tordue","fragile","usée","émoussée","abîmée","fendue","déformée","branlante","terne",
"lourde","instable","bancale","grossière","mal taillée","imparfaite","faible","fatiguée","ébréchée","endommagée",
"mal ajustée","décentrée","écaillée","dégradée","mal forgée","mal finie","inégale","désunie","primitive","douteuse",
"improvisée","mal entretenue","rudimentaire","mal proportionnée","usée par le temps","terne et usée","très usée","presque brisée","de fortune",
"faiblement forgée","déséquilibrée","mal trempée","de piètre qualité","instable","abîmée par l’usage","mal réparée","mauvaise","moche","trop lourde",
"ordinaire","simple","commune","basique","fonctionnelle","acceptable","standard","correcte","utilitaire","passable",
"modeste","adaptée","fiable","rustique","stabilisée","ajustée","pratique","robuste","fiable et stable","simple mais efficace",
"robuste mais lourde","correcte et durable","équilibrée et stable","solide et correcte","fiable et utile","ordinaire mais durable","stable et correcte","solide","robuste",
"stable","fiable","fonctionnelle","soignée","durable","équilibrée","raffinée","propre","bien faite","pratique",
"harmonieuse","agréable","soigneuse","ajustée et solide","simple et pratique","équilibrée et fiable","soignée et robuste","stable et durable","robuste et efficace","fiable et équilibrée",
"robuste et soignée","précise","fiable et robuste","solide et stable","équilibrée et solide","robuste et fiable","durable et stable","fiable et efficace","fonctionnelle et solide","soignée et équilibrée",
"ajustée et robuste","propre et stable","fiable et soignée","robuste et durable","fiable et stable","fonctionnelle et fiable","stable et équilibrée","robuste et précise","fiable et solide","robuste et pratique",
"solide et efficace","affûtée","bien polie","renforcée","de bonne qualité","brillante","en bon état","raffinée","bien équilibrée","soigneusement faite",
"bien forgée","fiable et polie","soignée et précise","raffinée et stable","bien entretenue","précise et stable","robuste et élégante","fiable et polie","équilibrée et polie","fiable et brillante",
"soignée et brillante","raffinée et durable","bien proportionnée","robuste et lisse","fiable et soignée","agréablement équilibrée","soigneusement forgée","propre et brillante","précise et efficace","robuste et harmonieuse",
"parfaite","lumineuse","aiguisée","finement polie","bien affûtée","aux reflets métalliques","aux bords nets","équilibrée à la perfection","soyeuse",
"d’apparence noble","d’une forge reconnue","d’alliage pur","éclatante","affûtée à la perfection","revêtue d’argent","brillante et solide","bien trempée","sans défaut",
"de belle facture","soigneusement polie","aux gravures fines","en métal pur","bien équilibrée et polie","raffinée et pure","élégante","magnifique",
"gracieuse","bien trempée","précise et élégante","aux reflets bleutés","d’une belle brillance","de qualité supérieure","équilibrée et noble","à luisance propre","finement équilibrée","de bonne réputation",
"aux détails précis","pure et nette","harmonieuse et brillante","travaillée avec soin","à manche poli","raffinée et claire","en métal noble","aux lignes parfaites","à finition propre","d’artisan experte",
"noble","runique","gravée","ornée","charmée","bénie des anciens","aux reflets magiques","sacralisée","enchantée","belle et brillante",
"de forge ancienne","augurée","dorée","lumineuse et pure","ornée de runes","gravée avec soin","aux motifs anciens","aux reflets d’or","runique et équilibrée","énergisée",
"d’esprit ancien","chargée d’énergie","vibrante","chantante","lumineuse et stable","pure et rare","aux gravures soignées","dorée et polie","resplendissante",
"magique","aux pouvoirs anciens","aux inscriptions fines","rare et équilibrée","raffinée et magique","bénie et brillante","aux lueurs argentées","d’une aura douce","lumineuse et noble","de prestige",
"d’acier céleste","pure et polie","en alliage sacré","liée à la magie","aux éclats mystiques","polie par un mage","forgée avec soin divin","chargée de lumière","subtilement enchantée","divine",
"mythique","céleste","transcendante","glorieuse","auréolée","héroïque","sacrée","ultime","éternelle","infinie",
"exaltée","révérée","vénérée","immortelle","légendaire","précieuse","splendide","radieuse","lumineuse","brillante",
"resplendissante","éblouissante","magnifique","éclatante","harmonieuse","raffinée","noble","parfaite","divine","mythique",
"céleste","héroïque","sacrée","ultime","transcendante","glorieuse","immortelle","légendaire","supérieure","exquise",
"prestigieuse","majesteuse","remarquable","élégante","fine","pure","précieuse","rare","unique","inestimable",
"d’acier trempé","d’acier poli","d’acier brillant","d’argent pur","d’argent poli","d’argent divin","d’or massif","d’or pur","d’or divin","de mithril clair",
"de mithril pur","de mithril divin","d’adamantium ancien","d’adamantium pur","d’adamantium divin","de diamant pur","de diamant parfait","de diamant légendaire","robuste et brillant","fiable et solide",
"de cristal légendaire"
]

@app.get("/pioche")
async def generate_pickaxe():
    qualite = random.randint(1, len(suffixes_pioches))
    suffix = suffixes_pioches[qualite - 1]
    return {"pioche": f"Pioche {suffix}", "qualite": qualite}
