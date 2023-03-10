# Criando uma classe Animal com atributos com 2 metodos
class Animal:
    def _init_(self, nome, idade, especie, cor, som):
        self.nome = nome  # (string)
        self.idade = idade  # (inteiro)
        self.especie = especie  # (string)
        self.cor = cor  # (string)
        self.som = som  # (string)

    def emitir_som(self):
        print(self.som)

    def mudar_cor(self,nova_cor):
        self.cor = nova_cor
#Criando uma classe Elefante que herda de animal com atributos com 2 metodos
class Elefante(Animal):
    def _init_(self, nome, idade, especie, cor,som, tamanho):
        self.tamanho = tamanho
        super()._init_(nome, idade, especie, cor, som)
    def trombar(self):
        print(self.som)
    def mudar_tamanho(self,novo_tamanho):
        self.tamanho = novo_tamanho
# Instanciando classes e variaveis
nome = input("Escreva o nome do elefante: ")
idade = int(input("Escreva a idade do elefante: "))
especie = input("Escreva o especie do elefante: ")
cor = input("Escreva o cor do elefante: ")
tamanho = input("Escreva o tamanho do elefante: ")

elefante = Elefante(nome,idade,especie,cor,"",tamanho)
if elefante.especie == "Africano":
    if elefante.idade < 10:
        elefante.mudar_tamanho("Pequeno")
        elefante.som = "Paaah"
    else:
        elefante.mudar_tamanho("grande")
        elefante.som = "PAHHHHHH"
else:
    elefante.mudar_tamanho(elefante.tamanho)
    elefante.trombar()

print("Tamanho do elefante: " + elefante.tamanho)
print("Som: " + elefante.som)
