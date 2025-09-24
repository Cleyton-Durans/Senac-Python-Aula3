# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

media = 0
soma = 0

for i in range(5):
    numero = int(input(f" Digite o {i+1} numero: "))
    soma = soma + numero
media = soma / 5

print(f"A média dos número digitados é : {media}")
print(f"A soma doas número digitaods é : {soma} ")