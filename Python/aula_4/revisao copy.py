#MODULO
#PRINT (12 % 4 == 0 )

n = int(input("Digite um valor numérico "))
if(n % 2 == 0):
    #print(f' O {n} digitad é par')
    print(f' O {n} digitado é par')
elif(n % 2 == 1 ) :
    print(f'O número =>', n,'digitado é impar')
else:
    print('Número digitado inválido, inicie novamente!')