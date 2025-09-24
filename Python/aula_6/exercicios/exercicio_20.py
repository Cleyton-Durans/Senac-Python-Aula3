""" 
20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

"""

fatorial = 1
while True:
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))

    for i in range (numero, 0, -1):
        fatorial *= i
    print(f"Fatorial de {numero} é: {fatorial}")
    if numero < 0 or numero >= 16:
        print("Número fora do intervalo permitido (0 a 15). Tente novamente.")
        fatorial = 1  
    else:
        continua = input("Desejo calcular o fatorial de outro número? (s/n): ")
        if continua.lower() != 's' :
            print("Programa encerrado.")
            break       
