# CRIE UMA CLASSE CHAMADA ANIMAL, ANIMAL TERÁ 3 ATRIBUTOS (NOME, PESO E IDADE)
# CRIE 3 OBJETS PARA A CLASSE ANIMAL (GIRAFA, GATO, LEÃO)
#CRIE MÉTODO COMER ONDE ESTE MÉTODO INFORMARÁ QUE O ANIMAL QUE CHAMOU O MÉTODO ESTÁ COMENTO

class Animal:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade

    def comer(self):
        print(f"{self.nome} está comendo!")

a1 = Animal('Girafa','244,55','15')
a2 = Animal('Gato','15,20','3')
a3 = Animal('Leão','184,10','8')

print(f"Nome 1º Animal: {a1.nome} | peso: {a1.peso} | idade: {a1.idade}")
a1.comer()
print(f"Nome 2º Animal: {a2.nome} | peso: {a2.peso} | idade: {a2.idade}")
a2.comer()
print(f"Nome: 1º Animal: {a3.nome} | peso: {a3.peso} | idade: {a3.idade}")
a3.comer()
        