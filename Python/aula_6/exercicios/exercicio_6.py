"""
6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

"""
# Utilizand estrutura de repetoção While
numero = 1
while numero <= 20:
    if numero < 20:
        print(numero, end=" * ")
    else:
        print(numero)
    numero += 1

# Estrutura utilizando o for "range()"
for numero in range(1,21):
    print(numero, end=" - ")