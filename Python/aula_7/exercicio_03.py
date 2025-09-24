fruta = ['maça', 'banana', 'laranja', 'melão','morango']

print(F"IMPRIMA TODAS AS FRUTAS ==> {fruta[4]}")
tamanho = len(fruta)
print(f" Tamanho da lista é {tamanho}")

# IMRPIMA APENAS O INDICE 02
print(f"___________________________")
print(f"Imprima em número decrescente a fruta '-2': {fruta[-2]}")

# ADICIONA UM INDICE NO VETOR EM UMA FILA ESPECÍFICA
fruta[2] = 'mamao'
print(f"___________________________")
print(f"Imprima apenas o índice número 02: {fruta[2]}")

# ADICIONAR ÍNDICE COM COMANDO 'INSERT'
fruta.insert(3, 'abacaxi')
print(f"___________________________")
print(f"Imprima o Índice Número 3 do vetor: {fruta[3]}")





