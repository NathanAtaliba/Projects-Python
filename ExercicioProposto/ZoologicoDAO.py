import numpy as np
import Habitat
import Animal

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class ZoologicoCLI(SimpleCLI):
    def __init__(self, animal_model):
        super().__init__()
        self.animal_model = animal_model
        self.add_command("create", self.create_animal)
        self.add_command("read", self.read_animal)
        self.add_command("update", self.update_animal)
        self.add_command("delete", self.delete_animal)

    def create_animal(self):
        nomeanimal = input("Entre com o nome do animal: ")
        especie = input("Entre com a especie do animal: ")
        idade = int(input("Entre com a idade do animal: "))
        id = int(input('Entre com o id do Habitat: '))
        nome = input('Entre com o nome do Habitat: ')
        tipoAmbiente = input('Entre com o tipo de ambiente do habitat: ')
        idCuidador = int(input('Entre com o id do cuidador: '))
        nomeCuidador = input('Entre com o nome do cuidador: ')
        documento = input('Entre com o nome do documento: ')

        habitat = [
            {
            "id" : id,
            "nome": nome,
            "tipoAmbiente": tipoAmbiente,

            "cuidador": [{
                "id": idCuidador,
                "nome": nomeCuidador,
                "documento": documento
            }]
            }
        ]

        self.animal_model.create_animal(nomeanimal, especie, idade, habitat)

    def read_animal(self):
        id = input("Enter the id: ")
        animal = self.animal_model.read_animal_by_id(id)
        if animal:
            print(f"Nome: {animal['nome']}")
            print(f"especie: {animal['especie']}")
            print(f"idade: {animal['idade']}")
            print(f"habitat: {animal['habitat']}")

    def update_animal(self):
        id = input("Entre com o id : ")
        nome = input("Entre com o novo nome: ")
        especie = input("Enter com a nova especie: ")
        idade = int(input("Entre com a idade nova: "))
        habitat = input("Entre com o novo habitat: ")
        self.animal_model.update_animal(id, nome, especie, idade, habitat)

    def delete_animal(self):
        id = input("Enter the id: ")
        self.animal_model.delete_animal(id)

    def run(self):
        print("Bem vindo ao Zoologico")
        print("Entre com os comandos: create, read, update, delete, quit")
        super().run()
