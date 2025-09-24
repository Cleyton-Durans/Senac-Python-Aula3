# 5.	Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor =         []
vetorpar =      []
vetorimpar =    []

for i in range (5):
    n = int(input(f"Digite o {i+1}º número: "))
    vetor.append(n)
        
    if n % 2 == 0:
        vetorpar.append(n)
    else:
        vetorimpar.append(n)

# Imprimir os dados do vetores.

print(f"Os vetores par: {vetorpar}")
print(f"Os Vetores imparpar: {vetorimpar}")
print("!!----------------------!!")
print(f"Os Vetores par e imparpar: {vetor}") 