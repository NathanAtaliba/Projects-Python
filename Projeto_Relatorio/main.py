from database import Database
from TeacherCRUD import BancoDeDados

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://54.173.102.236:7687", "neo4j", "conjectures-taste-lumps")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
try:
    banco = BancoDeDados(db)
    print('Conectado!')
except:
    print('Não conectado!')

'''
#ENTRADA DE DADOS POR USUARIO
while True:
    print('Oque voce deseja fazer:')
    print('1- Criar Teacher')
    print('2- Atualizar Cpf do Teacher')
    print('3- Deletar Teacher')
    print('4- Procurar Teacher')
    print('5- Sair')
    escolha = int(input('Escolha:'))
    if escolha == 1:
        nome = input('Entre com o nome do teacher: ')
        ano = int(input('Entre com o ano de nascimento do teacher: '))
        cpf = input('Entre com o cpf do teacher: ')
        banco.criar_Teacher(nome, ano, cpf)
    elif escolha == 2:
        nome = input('Entre com o nome do teacher: ')
        cpfNovo = input('Entre com o cpf Novo: ')
        banco.update_Teacher(nome, cpfNovo)
    elif escolha == 3:
        nome = input('Entre com o nome do teacher: ')
        banco.delete_Teacher(nome)
    elif escolha == 4:
        nome = input('Entre com o nome do teacher: ')
        print(banco.read_Teacher(nome))
    elif escolha == 5:
        print('Até mais!')
        break
    else:
        print('Opção não existe! Tente novamente!')
'''

banco.criar_Teacher('Chris Lima',1956,'189.052.396-66')
print(banco.read_Teacher('Chris Lima'))
banco.update_Teacher('Chris Lima', "162.052.777-77")

# Fechando a conexão
db.close()
