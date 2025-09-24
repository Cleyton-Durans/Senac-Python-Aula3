""" 

class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca
        self.ano = 2019

p1 = Carro("HB20")
print("Nome: ",HB20)

"""

class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def acelerar(self):
        print(f"{self.nome} está acelelrando")
        
fusca = Carro("Fusca")
mar = Carro('chevrolet')
print("Nome: ",fusca.nome, mar.marca)
fusca.acelerar()

