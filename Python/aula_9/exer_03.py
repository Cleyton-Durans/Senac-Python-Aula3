# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

nota = []
media = " "

 
for i in range(4):
    while True:
        try:
            n = float(input(f"Digite sua {i+1}º nota: "))
        except ValueError:
            print(f" Digito inválido! digite novamente")
        break
    nota.append(n)

for i in range(4):
    print(f" {i+1}º Bimestre Notas {nota[i]}")

# Média do aluno!
media = sum(nota) / len(nota)
print(f"Média do aluno é {media}")
    

