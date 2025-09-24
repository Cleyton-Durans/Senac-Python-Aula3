#   7.	Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = []
soma = 0
multiplicacao = 1

for i in range(5):
    n = int(input(f" Digite {i+1}º número:  "))
    vetor.append(n)
    soma += n
    multiplicacao *= n 

print("Os número são...: ")

for i in range(5):
    print(f" {i+1}º número do {vetor[i]}  ")
print(f"A multiplicação dos número é: {multiplicacao}")
print(f"A soma dos número: {soma}")
