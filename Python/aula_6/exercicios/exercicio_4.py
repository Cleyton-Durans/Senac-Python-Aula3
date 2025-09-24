"""
4. Faça um Programa que verifique se uma letra digitada é 
vogal ou consoante.
"""

while True:
    
    letra = input("Digite uma letra: ").lower()
    if len(letra) != 1 or not letra.isalpha():
        print(" Entrada Inválida! Digite apenas uma letra.")
    elif letra in ['a','e','i','o','u']:
        print(F"{letra} é uma vogal.")
        break
    else:
        print(f"{letra} é uma consoante.")

        break  


"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população 
de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários 
para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

"""
# VARIAVEIS 
populacao_a = 80000
populacao_b = 200000

# VALOR DA TAXA EM PORCENTUAL
taxa_a = 0.03
taxa_b = 0.015

# TAXA DE PORNCETUAL
pop = 0

# ESTRUTURAD DE CONDICAO
while 
