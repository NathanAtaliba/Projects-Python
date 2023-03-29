import threading
import time
import random
from pymongo import MongoClient

# configurações do MongoDB
client = MongoClient('localhost', 27017)
db = client.bancoiot
collection = db.sensores

# definição das classes de sensores
class Sensor(threading.Thread):
    def _init_(self, nome):
        threading.Thread._init_(self)
        self.nome = nome
        self.valor = 0
        self.alarmado = False

    def run(self):
        while True:
            self.valor = round(random.uniform(30, 40), 2)
            print(f"{self.nome}: {self.valor} C°")
            self.atualizar_db()
            if self.valor > 38 and not self.alarmado:
                self.alarmado = True
                print(f"Atenção! Temperatura muito alta! Verificar {self.nome}!")
            time.sleep(5)

    def atualizar_db(self):
        query = {"nomeSensor": self.nome}
        update = {"$set": {"valorSensor": self.valor}}
        collection.update_one(query, update, upsert=True)

        if self.alarmado:
            update = {"$set": {"sensorAlarmado": True}}
            collection.update_one(query, update)

# criação dos objetos de sensores e documentos no banco de dados
temp1 = Sensor("Temp1")
temp2 = Sensor("Temp2")
temp3 = Sensor("Temp3")

docs = [
    {"nomeSensor": "Temp1", "valorSensor": 0, "unidadeMedida": "C°", "sensorAlarmado": False},
    {"nomeSensor": "Temp2", "valorSensor": 0, "unidadeMedida": "C°", "sensorAlarmado": False},
    {"nomeSensor": "Temp3", "valorSensor": 0, "unidadeMedida": "C°", "sensorAlarmado": False},
]

for doc in docs:
    collection.update_one({"nomeSensor": doc["nomeSensor"]}, {"$setOnInsert": doc}, upsert=True)

# inicialização das threads
temp1.start()
temp2.start()
temp3.start()