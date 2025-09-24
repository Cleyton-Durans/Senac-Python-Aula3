"""Atividade 15 - Triângulos
15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;
"""

#ENTRADA DE DADOS
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
print("_______________________________________")
    
#VERIFICANDO SE OS LADOS FORMA UM TRIÂNGULO
if (lado1 + lado2  > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os lados informados formam um triângulo.")
    #VERIFICANDO O TIPO DE TRIÂNGULO
    if lado1 == lado2 == lado3:
        tipo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print(f"Os lados formam um triângulo do tipo: {tipo}")
else:
    print("Valores informados não formam um triângulo.")       

    