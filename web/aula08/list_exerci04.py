notas = {
    "ana": 10,
    "bruno": 9,
    "carla": 8,
    "Aluan": 7
}

print(notas.items())# Mostra os itens do dicionário (chave,valor)
print(notas.keys())# Mostra as chaves do dicionário
print(notas.values())# Mostra os valores do dicionário
# buscando o registro que não existe*/
print("Notas do Aluan", notas["Aluan"])

if notas.get("Aluan") is None:
    print("Aluna não Cadastrado")
else:
    print('Aluno ja cadastrado!')