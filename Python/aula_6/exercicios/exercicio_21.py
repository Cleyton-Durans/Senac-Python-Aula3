""" 
21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.

"""

numero = int(input("Digite um número inteiro: "))
if numero < 2:
    print(f"{numero} não é primo. ")
else:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f"{numero} é primo. ")
    else:
        print(f"{numero} não é primo.  ")
        