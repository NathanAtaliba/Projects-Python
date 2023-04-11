import threading
import time
import random
from pymongo import MongoClient

#Configurações do MongoDB
client = MongoClient('localhost', 27017) #Configura a porta do servidor
db = client.bancoiot #inicializa db como cliente.bancoiot
sensores = db.sensores #sensores sera a colections sensores do bancoiot

# definição das classes de sensores
class Sensor(threading.Thread): # Criando a classe sensor
    def __init__(self, nome):  # construtor para nome do sensor
        threading.Thread.__init__(self)
        self.nome = nome
        self.valor = 0
        self.alarmado = False
    def run(self):  # rodando a thread e gerando um numero aleatorio
        while True:
            self.valor = round(random.uniform(30, 40), 2) #gerando valor de 30 a 40 para temperatura
            print(f"{self.nome}: {self.valor} C°")
            self.atualizar_db()
            if self.valor > 38 and not self.alarmado:
                self.alarmado = True
                print(f"Atenção! Temperatura muito alta! Verificar {self.nome}!")
            time.sleep(8) #Tempo que usuario deseja pare leitura dos sensores

    def atualizar_db(self):  # atualizando no documento o valor do sensor e se esta alarmado
        query = {"nomeSensor": self.nome}
        update = {"$set": {"valorSensor": self.valor}}
        sensores.update_one(query, update, upsert=True)
        if self.alarmado:
            update = {"$set": {"sensorAlarmado": True}}
            sensores.update_one(query, update)

# criação dos objetos de sensores e documentos no banco de dados
temp1 = Sensor("Temp1")
temp2 = Sensor("Temp2")
temp3 = Sensor("Temp3")

#Documento para manipulação
documento = [
    {"nomeSensor": "Temp1",
     "valorSensor": 0,
     "unidadeMedida": "C°",
     "sensorAlarmado": False},

    {"nomeSensor": "Temp2",
     "valorSensor": 0,
     "unidadeMedida": "C°",
     "sensorAlarmado": False},

    {"nomeSensor": "Temp3",
     "valorSensor": 0,
     "unidadeMedida": "C°",
     "sensorAlarmado": False},
]

for doc in documento:
    sensores.update_one({"nomeSensor": doc["nomeSensor"]}, {"$setOnInsert": doc}, upsert=True)

# inicialização das threads
temp1.start()
temp2.start()
temp3.start()

