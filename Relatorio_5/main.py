from database import Database
from Livro import livro
from crud import livroCLI

db = Database(database="Biblioteca", collection="livros")
livro = livro(database=db)

livroCLI = livroCLI(livro)
livroCLI.run()
