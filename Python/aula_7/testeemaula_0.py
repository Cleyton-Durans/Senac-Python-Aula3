# CRIANDO VETOR COM ÍNDICES INCLUSOS
fruta = ['maca', 'banana', 'laranja', 'melao','morango']
print ("\n".join(fruta))
print("______________________")

# ESTRUTURA DE CONDIÇÃO!
# EMTRADA E PROCESSAMENTO DE DADOS
while True:
    try:
        f_selecionada = input("Digite uma fruta que deseja excluir? ").lower()

        if f_selecionada == 'maça' or f_selecionada == 'maca':
            print('Estamos excluindo a fruta escolhida! ')
            fruta.remove('maca')
            

        elif f_selecionada == 'banana':
            print('Estamos excluindo a fruta escolhida! ')
            fruta.remove('banana')
            
        
        elif f_selecionada == 'laranja':
            print('Estamos excluindo a fruta escolhida! ')
            fruta.remove('laranja')
            

        elif f_selecionada == 'melao' or f_selecionada == 'melão':
            print('Estamos excluindo a fruta escolhida! ')
            fruta.remove('melao')
            

        elif f_selecionada == 'morango':
            print('Estamos excluindo a fruta escolhida! ')
            fruta.remove('morango')
            

        else:
            print("digito inválido, digite uma fruta válida")
            break
    except ValueError:
        print("Valor inválido, digite um valor válido")
# IMPRESSÃO DA LISTA ATUALIZADA
print(f" Lista de frutas atualizada! {fruta}")
    








