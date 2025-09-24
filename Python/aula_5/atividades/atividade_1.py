try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    if n1 > n2:
        print(f" Número {n1} é maior que o segundo digito! ")
    elif n1 < n2:
        print(f"Número digitado {n2} é maior que o primeiro digito! ")
    else:
        print("Os Números são iguais! ")
except :
    print("Digito incorreto")