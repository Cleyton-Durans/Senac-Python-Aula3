#   Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#   mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input("Digite um usuário: ")
    senha = input("Digite uma senha: ")

    if senha == usuario:
        print("Erro: A senha não pode ser igual ao nome de usuário.")
    else:
        print("Senha aceita!")
        break
