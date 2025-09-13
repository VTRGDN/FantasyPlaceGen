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
    """Toujours Préfixe + Middle+Suffix avec espace"""
    return f"{random.choice(prefixes)} {random.choice(middles)}{random.choice(suffixes)}"

@app.get("/place")
def get_place():
    """Retourne un seul lieu"""
    return {"place": generate_fantasy_place()}

@app.get("/places/{n}")
def get_places(n: int = 5):
    """Retourne une liste de n lieux"""
    return {"places": [generate_fantasy_place() for _ in range(n)]}
