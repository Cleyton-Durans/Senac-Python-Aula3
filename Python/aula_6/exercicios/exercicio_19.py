"""
19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

# 18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

qt_numero = int(input("Digite a quantidade de números: "))
lista = []

for i in range(qt_numero):
    numero = int(input(f'Digite o {i+1}º número: '))
    lista.append(numero)
    # Verifica se o número está entre 0 e 1000
    if numero < 0 and numero > 1000:
        print("Número fora do intervalo permitido (0 a 1000). Tente novamente.")
        continue
    
print(lista)
# IMRPIMIR MÁXIMO
print(f'Máximo: {max(lista)}')
# IMRPIMIR MÍNIMO
print(f'Mínimo: {min(lista)}')
# IMRPIMIR SOMA
print(f'Soma: {sum(lista)}')
# IMRPIMIR REVERSO
lista.reverse()
print("Reverso", lista)
    