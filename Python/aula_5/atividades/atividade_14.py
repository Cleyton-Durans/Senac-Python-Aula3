"""14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento
- Entre 9.0 e 10.0 : A
- Entre 7.5 e 9.0 : B
- Entre 6.0 e 7.5 : C
- Entre 4.0 e 6.0 : D
- Entre 4.0 e zero : E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” 
se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    print("_______________________________________")
        
    media = (nota1 + nota2) /2
    
    if media >= 9.0 and media <= 10.0:
        conceito = "A (APROVADO)"
    elif media >=7.5 and media < 9.0:
        conceito = "B (APROVADO)"
    elif media >=6.0 and media <7.5:
        conceito = "C (APROVADO)"
    elif media >=4.0 and media <6.0:
        conceito = "D (REPROVADO)"
    elif media >=0 and media <4.0:
        conceito = "E (REPROVADO)"
    else:
        conceito = "Nota inválida" 
 
    print(f"Notas: {nota1}, {nota2}")
    print(f"Média: {media:.2f}")    
    
    print(f"Conceito: {conceito}")
except ValueError:
    print("Erro: Digite valores numéricos válidos para as notas.")



