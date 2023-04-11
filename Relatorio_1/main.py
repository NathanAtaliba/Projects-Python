class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.idade = idade
        self.nome = nome
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print('Som: ' + self.som)

    def mudar_cor(self, nova_cor):
        self.cor = nova_cor

class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome,idade,especie,cor,som)
        self.tamanho = tamanho

    def trombar(self):
        print(self.som)
    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

nome = input('Entre com o nome: ')
idade = int(input('Entre com a idade: '))
especie = input('Entre com a especie: ')
cor = input('Entre com a cor: ')
tamanho = input('Entre com o tamanho : ')
som = input('Entre com o som: ')

elefante1 = Elefante(nome,idade,especie,cor,som,tamanho)

if(especie == 'Africano' and idade < 10):
    elefante1.tamanho = 'pequeno'
    elefante1.som = "Paaah"
if(especie == 'Africano' and idade >= 10):
    elefante1.tamanho = 'grande'
    elefante1.som = 'PAHHHHHH'

elefante1.emitir_som()
print("Tamanho: " + elefante1.tamanho)













