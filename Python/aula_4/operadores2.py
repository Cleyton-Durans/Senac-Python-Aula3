dinheiro = True
senha_correta = 12345
senha = int(input("Digite a senha crreta: "))
#senha_correta = int(input("Digita a senha correta: "))

if dinheiro == True and senha == senha_correta:
    print("Saque efetuado! ")
#elif dinheiro == True and senha == False:
#   print("Senha invalida! ")
#elif dinheiro == False and senha == True:
#    print("Senha invalida! ")
#elif dinheiro == False and senha == False:
 #   print("Senha invalida! ")
else:
    print("Senha incorreta")