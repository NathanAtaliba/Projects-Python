from database import Database
db = Database(database="Biblioteca", collection="livros")
db.resetDatabase()

print("Oque voce deseja fazer?")
print("1 - Adicionar livro")
print("2 - Atualizar livro")
print("3 - Deletar livro")
print("4 - Procurar livro")
print("5 - Nada")
entrada = int(input("Entre com o valor: "))
def adicionarLivro():
    print("Qual livro voce deseja adicionar?")
    titulo = input("Entre com o titulo:")
    autor = input("Entre com o autor: ")
    ano = int(input("Entre com o ano: "))
    preco = int(input("Entre com o preco: "))

    return 0
def atualizarLivro():
    print("Qual livro voce deseja atualizar?")
    titulo = input("Entre com o titulo que deseja modificar:")
    tituloNovo = input("Entre com o titulo novo:")

    return 0
def deletarLivro():
    print("Qual livro voce deseja deletar?")
    titulo = input("Entre com o titulo:")

    return 0
def procurarLivro():
    print("Qual livro voce deseja procurar?")
    titulo = input("Entre com o titulo:")


    return 0
def nada():
    print("Obrigado, volte sempre!")

    return 0
def default():

    return 0
def switch (entrada):
    if(entrada == 1):
        return adicionarLivro()
    elif(entrada == 2):
        return adicionarLivro()
    elif(entrada == 3):
        return adicionarLivro()
    elif(entrada == 4):
        return adicionarLivro()
    elif (entrada == 5):
        return nada()
    else:
        return default

switch(entrada)
