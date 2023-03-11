from database import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})
bulbasaur = getPokemonByDex(1)
writeAJson(bulbasaur, "bulbasaur")

def get_4_letters_or_less(collection):
  names = collection.find({}, {"name": 1})
  four_letters_or_less = []
  for name in names:
    if len(name["name"].keys()) <= 4:
      if all(len(word) <= 4 for word in name["name"].values()):
        four_letters_or_less.append(name["name"].values())
  return four_letters_or_less
writeAJson(get_4_letters_or_less(db.collection), "pokemon_4_words_or_less")

def getNameById(number: int):
    return db.collection.find({"id": number},{"name"})
namePokemon = getNameById(1)
writeAJson(namePokemon, "namePokemon")

def getAttackById(number: int):
    return db.collection.find({"id": number},{"base.Attack"})
attackPokemon = getAttackById(1)
writeAJson(attackPokemon, "attackPokemon")

def getDefById(number: int):
    return db.collection.find({"id": number},{"base.Defense"})
defensePokemon = getDefById(1)
writeAJson(defensePokemon, "defensePokemon")

