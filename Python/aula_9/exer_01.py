#   1.	Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

# Criar uma lista
lista = []

# Entrando com os cincos número da lista
for i in range (5):
    #Pedindo o usuário oara digitar o valor da lista
    l = int(input(f"Digite o {i+1}º Número da lsita: "))
    # gravando o número na lista
    lista.append(l)

# Imrpimindo o conteúdo da lista
for i in range (5):
    print(f"Coluna {i+1} possui número dessa é ---> {lista[i]}")
    