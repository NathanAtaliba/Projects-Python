from database import Database
from Animal import animal
from ZoologicoDAO import ZoologicoCLI

db = Database(database="Zoologico", collection="zoologico")
animal = animal(database=db)

zoologicoCLI = ZoologicoCLI(animal)
zoologicoCLI.run()
