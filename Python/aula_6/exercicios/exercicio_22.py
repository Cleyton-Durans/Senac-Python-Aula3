""" 
22. Altere o programa de cálculo dos números primos, informando, 
caso o número não seja primo, por quais número ele é divisível.

"""

numero = int(input("Digite um número inteiro: "))
if numero < 2:
    print(f"{numero} não é primo. ")
else:
    primo = True
    divisores = []
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            divisores.append(i)
                    
    if len(divisores) == 0:
        print(f"{numero} é primo. ")
    else:
        print(f"{numero} não é primo.  ")
        print(f"{numero} é divisível por: {divisores}")
        