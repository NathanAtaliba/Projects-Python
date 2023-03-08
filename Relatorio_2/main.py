from database import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})
pokemon = getPokemonByDex(1)
writeAJson(pokemon,"bulbasauro")

def get_4_letters_or_less(collection):
  names = collection.find({}, {"name": 1})
  four_letters_or_less = []
  for name in names:
    if len(name["name"].keys()) <= 4:
      if all(len(word) <= 4 for word in name["name"].values()):
        four_letters_or_less.append(name["name"].values())
  return four_letters_or_less

writeAJson(get_4_letters_or_less(db.collection), "pokemon_4_words_or_less")

pokemon1 = db.collection.find({"type": "Grass", "base.Attack": { "$lte": 50 }})
writeAJson(pokemon1, "pokemon_grass")
def buscaNomeEnglish():
    return
def buscaAttack():
    return
def buscaDef():
    return

