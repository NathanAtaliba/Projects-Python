from database import Database
from Carta import carta
from cli import CartaCLI

db = Database(database= "Deck", collection= "Cartas")
cartaModel = carta(database=db)

cartaCLI = CartaCLI(cartaModel)
cartaCLI.run()
