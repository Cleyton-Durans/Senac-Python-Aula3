entrada = input(" Voce quer [entrar ou sair]")
entrada = entrada.lower()

"""
= ATRIBUIÇÃO
== COMPARAÇÃO
"""

# .LOWER() SERVE PARA DEIXAR TODAS INFORMAÇÃO DA VARIAVEL EM MINÚSCULA E ENVIA OARA O PROCESSAMENTO

if entrada == "entrar":
    print("Seja bem vindo, voce entrou no Sistema")
elif entrada == "sair":
    print("Voce saiu do Sistema")
else:
    print(" Voce não digitou a opção crreta!")

    