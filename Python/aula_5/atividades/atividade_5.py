#       5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#       - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#       - A mensagem "Reprovado", se a média for menor do que sete;
#       - A mensagem "Aprovado com Distinção", se a média for igual a dez.

try:
    nota1 = int(input("Digite sua nota 1 para ser calculada: "))
    nota2 = int(input("Digite sua nota 2 para ser calculada: "))

    media = (nota1 + nota2) / 2

    if media == 10 : 
        print("Aprovado com distinção")
    elif media >= 7 :
        print("Aprovado")
    else:
        print("Reprovado")
except:
    print("Digito incorreto.") 