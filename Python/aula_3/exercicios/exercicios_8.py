#   1. Faça um Programa que pergunta quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario = float(input("Quanto voce ganha por horas? "))
horas_trabalho = int(input("Quantas horas trabalhou nesse mês? "))
horas_dinheiro = horas_trabalho * salario
print(f" Voce ganhou {horas_trabalho:.2f} no mês referido.")

