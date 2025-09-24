# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))

for i in range(numero_1, numero_2 + 1):
    print(f"Número gerado no intervalo delas é {i}")