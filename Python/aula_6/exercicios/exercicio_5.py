"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população 
de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários 
para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.


# VARIAVEIS 
populacao_a = 80000
populacao_b = 200000

# VALOR DA TAXA EM PORCENTUAL
taxa_a = 0.03
taxa_b = 0.015

# TAXA DE PORNCETUAL
Taxa_anual = 0

# ESTRUTURAD DE CONDICAO
while populacao_a <= populacao_b:
    populacao_a += populacao_b * taxa_a
    populacao_b += populacao_a * taxa_b
    Taxa_anual =+ 1
    print(f"ano {Taxa_anual} : população A = {populacao_a} População B = {populacao_b}")
print(f"Serão necessários {Taxa_anual} anos para a população do país A ultrapassar ou igualar a população do país B.")
print(f"População A: {int(populacao_a)} Habitantes)")
print(f"População n: {int(populacao_b)} Habitantes)")


---------------------------------------------------------------------------

5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

"""

# VARIAVEIS 
populacao_a = float(input("Digite a popilação A: "))
populacao_b = float(input("Digite a população B: "))


# VALOR DA TAXA EM PORCENTUAL
taxa_a = float(input("Digite a taxa de população A: "))
taxa_b = float(input("Digite a taxa de população B: "))


# TAXA DE PORNCETUAL
Taxa_anual = 0

taxa_a = taxa_a / 100
taxa_b = taxa_b / 100

# ESTRUTURAD DE CONDICAO
while populacao_a <= populacao_b:
    populacao_a += populacao_b * taxa_a
    populacao_b += populacao_a * taxa_b
    Taxa_anual += 1
    print(f"ano {Taxa_anual} : população A = {populacao_a} População B = {populacao_b}")
print(f"Serão necessários {Taxa_anual} anos para a população do país A ultrapassar ou igualar a população do país B.")
print(f"População A: {int(populacao_a)} Habitantes)")
print(f"População n: {int(populacao_b)} Habitantes)")
