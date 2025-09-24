class Carro:
    # Atributo de classe
    # Acesso Não precisa de craição de uma instância

    rodas = 4 

    # Contrutor
    def __init__(self, marca, ano):
        # Atributo de instância
        # Acesso - Precisa de criação de instância
        self.marca = marca
        self.ano = ano
    
    # Método de classe (usa self)
    # Acesso - Precisa de criação de uma primeira instância
    def ligar(self):
        print(f"O carro {self.marca} está ligado.")
    
    # Método de classe (usa cls)
    # Acesso - Não precisa de criação de uma primeira instância
    @classmethod
    def mudar_numero_rodas(cls, novas_rodas):
        cls.rodas = novas_rodas
        print("Agora todos os carros têm {cls.rodas} rodas.")

# Método estático (não usa self nem cls)
# Acesso - Não precisa da criação de uma instância
# Escopo - Não recebe o self e nem cls então não tem cesso
# Caso queria acessar os da Classe poderá, porém que passar explicitamente

@staticmethod
def calcular_idade(ano_fabricacao, ano_atual):
    return ano_atual - ano_fabricacao


# ======= Testando a classe ========= #

carro1 = Carro("Toyota", 2020)
carro2 = Carro("Fiat", 2018)