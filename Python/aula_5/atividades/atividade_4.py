#   Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
try:

    letra = str(input("Digite uma letra: "))
    letra = letra.upper() #  '.UPPER()" MÉTODO PARA PASSAPARA MAIÚSCULA.

    #print(letra)
    vogal = ['A', 'E', 'I', 'O', 'U']
    consoante = ['B',"C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","X","W","Y","Z"]
    if letra in vogal:  
            print("Caracter é vogal!")
    elif letra in consoante:
        print("Caracter é consoante")
    else:
         print("Caracter não é uma letra")
except :
    print("Digite não é um cacacter válido! ")