from funcao_05 import converter_metros_para_centimetro
from funcao_06 import calcular_area_circulo
from funcao_07 import calcular_area_do_quadrado

def menu():
    while True:
        print("\n -- Menu de Opções ")
        print("1 - Converter metros para centímetros ")
        print("2 - Calcular área do círculo ")
        print("3 - Calcular área do quadrado ")
        print("0 - Sair ")

        opcao = input("Escolha uma oção: ")

        if opcao == '1':
            converter_metros_para_centimetro()
        elif opcao == '2':
            calcular_area_circulo()
        elif opcao == '3':
            calcular_area_do_quadrado()
        elif opcao == '0':
            print("Saindo do programa. Até amanhã")
            break
        else:
            print("Opção Inválida! - Tente novamente")
           
#   Iniciar o menu
if __name__ == "__main__":
    menu()

        
# OBERVAÇÃO IMPORTANTE