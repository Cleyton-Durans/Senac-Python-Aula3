""" 
13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.

"""

num_base = float(input("Digite a base: "))
num_expoente = int(input("Digite o expoente: "))

resultado = 1.0
for i in range(num_expoente):
    resultado *= num_base
    print(f"{num_base} elevado a {i + 1} é {resultado}")