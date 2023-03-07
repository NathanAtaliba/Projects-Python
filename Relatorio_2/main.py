from database import Database

db = Database(database="dex", collection="pokemons")
db.resetDatabase()

pokemons = db.collection.find()
for pokemon in pokemons: #printando ela
    print(pokemon)
