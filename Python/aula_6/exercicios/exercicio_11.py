# 11. Altere o programa anterior para mostrar no final a soma dos números.

soma = 0 
numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))

for i in range(numero_1 + 1 , numero_2):
    print(i, end=" _")
    soma = soma + i
print(f"a soma do número digitado é {soma}")