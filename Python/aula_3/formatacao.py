# IMC = ÍNDICE DE MASSA CORPOREA
# IMC = PESO / ALTURA ** 2
# IMC = PESO / (ALTURA * ALTURA)

nome = 'Durans'
altura = 1.65
peso = 60

print("Nome :", nome, end="\n")
print("Altura :", altura, end="\n")
# PROCESSAMENTO
imc = peso / altura * altura
print("IMC É :", imc)

# OUTRA FORMA
imc = peso / altura * altura
print(nome, "tem ", altura, "e seu IMC é", imc )

# F - STRINGS "UTILIZANDO COM O RÓTULO"
print(F" O {nome} tem {altura} de altura e pesa {peso}. Seu IMC é = {imc:.2F}")


