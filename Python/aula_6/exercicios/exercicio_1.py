# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
try:
    while True:
        nota = int(input("Digite uma nota ente [0 a 10]: ")) 
        if nota < 0 or nota > 10:
            print("Digite um valor válido")
        else:
            print("Voçê digitou um valor válido")
            break   #QUEBRA O CICLO DE REPETIÇÃO
except ValueError:
    print("Digite um númeor inteiro.")