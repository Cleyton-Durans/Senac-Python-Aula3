# 7. Faça um programa que leia 5 números e informe o maior número.


#   Usei input() em vez de print() para capturar o valor digitado.
#   Utilize None como valor inicial para maior e menor, evitando que zeros ou outros valores interfiram.
#   As condições if maior is None or n > maior: e if menor is None or n < menor: atualizam corretamente os valores conforme as entradas.
#   No fim, exibo os resultados usando as variáveis corretas.

maior = None
menor = None

for i in range(5):
    n = int(input(f"Digite o {i+1}° número: "))
    if maior is None or n > maior:
        maior = n
    if menor is None or n < menor:
        menor = n 

print(f"O maior número digitado foi {maior}")
print(f"O menor número digitado foi {menor}")