from database import Database
from Jogo import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.238.107.201:7687", "neo4j", "paw-crosses-blower")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
game_db = GameDatabase(db)

# Criando alguns players
game_db.create_player("João")
game_db.create_player("Maria")
game_db.create_player("José")
game_db.create_player("Nathan")

# Criando alguns match e suas relações com os alunos
game_db.create_match("Jogo1", "João")
game_db.create_match("Jogo2", "Maria")
game_db.create_match("Jogo3", "José")
game_db.create_match("Jogo1", "Nathan")

# Inserindo player no jogo
game_db.insert_player_match("Joao", "Jogo1")
game_db.insert_player_match("Maria", "Jogo2")
game_db.insert_player_match("Jose", "Jogo3")
game_db.insert_player_match("Nathan", "Jogo1")
# Print de todas as informações do banco de dados
print("Players:")
print(game_db.get_players())
print("Matchs:")
print(game_db.get_matchs())
print()
# Fechando a conexão
db.close()
