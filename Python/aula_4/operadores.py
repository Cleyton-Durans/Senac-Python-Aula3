dinheiro = True
senha = True
#senha_correta = int(input("Digita a senha correta: "))

if dinheiro == True and senha == True:
    print("Saque efetuado! ")
elif dinheiro == True and senha == False:
    print("Senha invalida! ")
elif dinheiro == False and senha == True:
    print("Senha invalida! ")
elif dinheiro == False and senha == False:
    print("Senha invalida! ")
#else:
#    print("Saldo insuficinete")


"""
dinheiro = True
senha = 1234
senha_correta = int(input("Digita a senha correta: "))

if dinheiro == True and senha_correta == senha:
    print("Saque efetuado! ")
elif dinheiro == True and senha == False:
    print("Senha invalida! ")
#else:
#    print("Saldo insuficinete")

"""