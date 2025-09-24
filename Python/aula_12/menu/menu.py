
"""
def menu():
    while True:
        print("\n -- Menu de Opções ")
        print("1 - Converter metros para centímetros ")
        print("2 - Calcular área do círculo ")
        print("3 - Calcular área do quadrado ")
        print("0 - Sair ")

        opcao = input("Escolha uma oção: ")

        if opcao == '1':
            runpy.run_path("exer_5.py")
        elif opcao == '2':
            runpy.run_path("exer_6.py")
        elif opcao == '3':
            runpy.run_path("exer_7.py")
        elif opcao == '0':
            print("Saindo do programa. Até amanhã")
            break
        else:
            print("Opção Inválida! - Tente novamente")
           
#   Iniciar o menu
if __name__ == "__main__":
    menu()

# OBERVAÇÃO IMPORTANTE

"""

import runpy


def menu():
    while True:
        print('\n -- Menu de opções')
        print('1 - converter metros para centimetros')
        print('2 - Calcular área do Círculo')
        print('3 - calcular a área de um quadrado')
        print('0 - Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            runpy.run_path('exer_5.py')
        elif opcao == "2":
            runpy.run_path('exer_6.py')
        elif opcao == "3":
            runpy.run_path('exer_7.py')
        elif opcao == '0' :
            print('Saindo do programa')
            break    
        else:
            print('Opção invalida')

#iniciar menu
if __name__=="__main__" : #importante para garantir que o menu só execute se for o arquivo principal
    menu()