from database import Database
from Consulta import BancoDeDados

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.210.126.150:7687","neo4j", "oil-wires-passages")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
try:
    banco = BancoDeDados(db)
    print('Conectado!')
except:
    print('Não conectado!')

# Criando algumas pessoas
banco.criar_pessoa("Engenheiro", "Nathan", 22, "M")
banco.criar_pessoa("Reporter", "Renan", 17, "M")
banco.criar_pessoa("Pedreiro", "Ian", 18, "M")
banco.criar_pessoa("Comerciante", "Joao", 59, "M")
banco.criar_pessoa("Contadora", "Fernanda", 55, "F")
banco.criar_pessoa("Medica", "Eloiza", 32, "F")
banco.criar_pessoa("Contadora", "Luzia", 70, "F")

# Criando alguns match e suas relações com os alunos
banco.criar_pet("Toddy", 7, "Marron", "Dog")
banco.criar_pet("Billy", 8, "Amarelo", "Cat")
banco.criar_pet("Talis", 3, "Verde", "Bird")

#Criando relacionamento pessoa com pet e pessoa com pessoa
banco.criar_pessoa_pet("Nathan", "Toddy")
banco.criar_pessoa_pet("Nathan", "Billy")
banco.criar_pessoa_pet("Nathan", "Talis")
banco.criar_pessoa_pessoa("Ian", "Nathan", "IRMAO_DE")
banco.criar_pessoa_pessoa("Fernanda", "Renan", "PAI_DE")
banco.criar_pessoa_pessoa("Fernanda", "Nathan", "PAI_DE")
banco.criar_pessoa_pessoa("Fernanda", "Ian", "PAI_DE")
banco.criar_pessoa_pessoa("Joao", "Fernanda", "ESPOSO_DE")
banco.criar_pessoa_pessoa("Luzia", "Fernanda", "PAI_DE")

while True:
    # Print de todas as informações do banco de dados
    print("Oque deseja fazer?")
    print("0-Mostrar pessoas")
    print("1-Mostrar pets")
    print("2-Procurar quem tem algum emprego especifico")
    print("3-Procurar se uma pessoa é filha de alguem")
    print("4-Procurar quem é casada com tal pessoa")
    print("5-Sair")
    escolha = int(input("Escolha: "))

    if escolha == 0:
        print("Pessoas: ", banco.get_pessoa())
    elif escolha == 1:
        print("Pets: ", banco.get_pet())
    elif escolha == 2:
        nome = input("Entre com o nome do emprego: ")
        print("Quem é " + nome + " :", banco.get_emprego(nome))
    elif escolha == 3:
        nome = input("Entre com o nome do pai ou da mae: ")
        print("Quem tem " + nome + "como pai ou mae: ", banco.get_Pai(nome))
    elif escolha == 4:
        nome = input("Entre com o nome da pessoa que voce quer saber do relacionamento: ")
        print("Essa pessoa tem relacionamento com: ", banco.get_Relacionamento(nome))
    elif escolha == 5:
        print("Até mais!")
        break
    else:
        print('Opção não existe!')

# Fechando a conexão
db.close()
