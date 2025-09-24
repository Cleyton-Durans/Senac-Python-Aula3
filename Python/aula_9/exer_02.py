# 2.	Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

for i in range (10):
    l = float(input(f"Digite o {i+1}º Número da lsita: "))
    lista.append(l)

for i in range (10):
    lista.reverse()
    print(f"Coluna {i+1} possui número dessa é ---> {lista[i]:.0f}")