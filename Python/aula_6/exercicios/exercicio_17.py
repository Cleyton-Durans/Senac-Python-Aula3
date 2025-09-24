""" 
17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

"""

fatorial = 1
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

for i in range (numero, 0, -1):
    fatorial *= i
print(f"Fatorial de {numero} é: {fatorial}")

    