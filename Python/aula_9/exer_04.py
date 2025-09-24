# 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
# Imprima as consoantes.

consoante = []
contador = 0
vogal = ['a', 'e', 'i', 'u', ]

for i in range (3):
    letra =  str(input(f" Digite a letra {i+1} Letra: ")).lower()
    consoante.append(letra)
    
    print("---------------")

    if letra.isalpha() and letra not in vogal:
        #print(consoante)
        contador += 1
print(f"foi informado o total de {contador} consoantes")

