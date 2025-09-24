#   EXCEPT 

try:
    numero = int(input("Digite um número "))
    if numero % 2 == 0:
        print("Número digitado é par")
    else:
        print("Número é impar")
except ValueError:
    print("Caracter digitado invalido")

