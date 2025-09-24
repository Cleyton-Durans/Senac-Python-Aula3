# 6. Faça um Programa que peça as quatro notas de 10 alunos, calcule 
# e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

nmaior7 = soma = 0
vetormedia = []

for i in range (2): # Total de 3 alunos
    
    for j in range (4): # Total de quatro notas
        nota = float(input(f"Digite a {j+1} nota do {i+1} aluno: "))
        soma = soma + nota
    
    media = soma/4
    print(f"Média do {i+1}º aluno é:  {media}" )
    soma = 0
    vetormedia.append(media)
            
for i in range (2): 
    if vetormedia[i] >= 7 :
        nmaior7 = nmaior7 +1

print(f"Número de alunos que obteve nota maior que 7 é: {nmaior7}" )
