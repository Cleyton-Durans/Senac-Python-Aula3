class Pessoa: 
    def __init__(self, nome, sobrenome):
        self.nome = nome 
        self.sobrenome = sobrenome

p1 = Pessoa ('Andre','Marques')
p2 = Pessoa ('Julmar','Santos')
print(p1.nome)
print(p2.nome)
print("=====")
print(p2.nome,p2.sobrenome)
