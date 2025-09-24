"""
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

"""
#   len(nome) É uma função que retorna o valor do campo.
#   Use try e except para tratar erros na conversão de tipos de dados.
#   .lower() Converte o valor para minúsculo.
#   .upper() Converte o valor para maiúsculo.
#   in Verifica se o valor está contido na lista.
#   not in Verifica se o valor não está contido na lista.
#   break Encerra o laço de repetição.
#   continue Retorna ao início do laço de repetição.
#   exit() Encerra o programa.

while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    print("Nome inválido! Deve ter mais de 3 caracteres")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        else:
            print("Idade inválida! Deve estar entre 0 e 150.")
    except ValueError:
        print("Idade inválida! Digite um número inteiro.")
        
while True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario > 100:
            break
        else:
            print("Salário inválido! Deve ser maior que 100.")
    except ValueError:
        print("Salário inválido! Digite um número válido.")

while True:
    sexo = input("Digite seu sexo (f/m): ").lower()
    if sexo in ['f', 'm']:
        break
    print("Sexo inválido! Digite 'f' para feminino ou 'm' para masculino.")

while True:
    estado_civil = str(input("Digite seu estado civil (s / c / v / d :")).lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil inválido! Digite 's', 'c', 'v' ou 'd'.")

print("_________________________________________")
print("DADOS VALIDADOS COM SUCESSO!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {'feminino' if sexo == 'f' else 'Masculino'}")
print(f"Estado civil: {estado_civil}")