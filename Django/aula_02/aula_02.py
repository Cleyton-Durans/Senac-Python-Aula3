class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def ligar(self):
        print(f"O carro {self.marca} está ligado.")

    def acelerar(self):
        print(f"O carro {self.marca} está acelerando.")

# ======= Testando a classe ========= #

carro1 = Carro("Toyota", 2020)
carro2 = Carro("Fiat", 2018)

carro1.ligar()
carro1.acelerar()

carro2.ligar()
carro2.acelerar()

             
