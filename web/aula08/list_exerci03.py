loginSenha = {
   'joao' : '12345',
   'Maria' : '5648',
   'ana' : '6235'
}

usuario =  input('Digite o nome do usuário')
senha = input('Digite a senha')
if usuario in loginSenha and loginSenha[usuario] == senha:
   print('login realizado com sucesso!')
else:
   print('Usuário ou Senha incorretas')
