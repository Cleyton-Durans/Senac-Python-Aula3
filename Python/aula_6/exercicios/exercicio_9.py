# 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
# "if i % 2 !=0"  verific se o numero em i dividido por 2 tenha um valor diferente de 0.

for i in range(1,51):
    if i % 2 != 0:
        print(i,end=" - ")