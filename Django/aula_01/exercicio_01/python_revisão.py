print("################### REVISÃO DE STRINGER ########################")
nome = "Cleyton"
sobrenome = "Durans"

# Concatenação
print("CONCATENAÇÃO")
nome_completo = nome + " " + sobrenome
nome_completo2 = f"{nome} {sobrenome}"
print("Nome completo:", nome_completo)

# Fatiamento
print("FATIAMENTO")
print("Primeira letra:", nome[0])
print("Últimas 3 letras:", nome[-3:])
print("Letras da posição 1 a 3:", nome[1:4])

# Métodos principais
print("MÉTODOS PRINCIPAIS")
print("Maiúscula:", nome.upper())
print("Minúscula:", nome.lower())
print("Inicial Maiúscula:", nome_completo.title())
print("Substituindo sobrenome:", nome_completo.title().replace("Durans", "Nascimento"))
print("Split:", nome_completo.split("a"))

# Comentário:
# title() -> Deixa a primeira letra de cada palavra em maiúscula!

print("################### REVISÃO DE INTEIRO ########################")
idade = 25
print("Idade:", idade)
print("Idade X 2:", idade * 2)
print("Idade / 2:", idade / 2)
print("Idade Potência 2:", idade ** 2)
print("Resto da Divisão:", idade % 5)

# Função
print("Mínimo:", min(3,1,8,2,4,3,8))
print("Máximo:", max(3,1,8,2,4,3,8))
print("Absoluto:", abs(-10))
print("Arredondar:", round(20.5545612))

print("################### REVISÃO DE FLOAT ########################")
altura = 1.71

# Operação com Float
print("Altura", altura)
print("Altura X 2", altura*2)
print("Altura : 3", altura/3)

# Operações com Float
print("Arredondado", round(altura,1))

# Biblioteca Math
import math
print("Raiz quadrada:", math.sqrt(16))
print("PI:", math.pi)

print("math é um módulo da biblioteca padrão do Python que contém funções matemáticas, como:")
print("math.sqrt() → raiz quadrada")
print("math.pow(x, y) → potência")
print("math.pi → constante π")
print("math.ceil() / math.floor() → arredondamentos")

print("################### REVISÃO E BOOLEAN ########################")
instrutor = True
ativo = False

# Comparação Retornam Bool
print("10 > 5?", 10 > 5)
print("10 == 5?", 10 == 5)
print("10 < 5?", 10 < 5)

#Use em if
print("TESTE DE IF E ELSE, COM ATRIBUIÇÃO DE VALOR (TRUE E FALSE)")
if instrutor:
    print("É instrutor (IF)")
else:
    print("Não é o instrutor (ELSE)")

if ativo:
    print("Tem Valor Ativo")
else:
    print("Não Tem Valor Ativo")

print("################### REVISÃO DE LISTA ########################")
cores = ["vermelho" , "azul" , "amarelo" , "branco"]
print("Cores da lista: ",cores)

# Acesso e Fatiamento
print("Primeira cor: ",cores[1][1]) # Dessa maneira o programa retorna o "Letra 2" do "item 2" da lista.
print("Primeira cor: ",cores[1][1:])
print("Primeira cor: ",cores[3])

# Métodos principais
# Adiciona

cores.append("amarelo")
print("Após append", cores)

#Remove
cores.remove("vermelho")
print("Após remove: ", (cores))

# Cria uma cópia da lista
print("Quantidade: ", len(cores))
print("Existe 'azul'?", "azul" in cores)

# Aqui é feita uma cópia independente
cores2 = cores.copy() # Todo a referência da variavel cores ira estar em cores2
cores.append("laranja")

# Impressão das listas
print("cores1", cores)
print("cores2", cores2)

print("################### REVISÃO DE TUPLA ########################")
par = (1,2,3)
print("## IMPRIMIR A TUPLA ##",par)
print("A TUPLA É IMUTÁVEL ->")
print("Primeiro", par[0])
print("Último", par[-1])

# Tupla é imutável
# par[0] = 99 #ERRO
print("Comprimento:", len(par))
print("Existe '2' na tupla?", 2 in par)


print("################### REVISÃO DE DICIONÁRIO ########################")
#Criação de um dicionário
config = {"modo": "aula", "nivel": "inicial"}
print(config)

# Acesso
print("nivel", config["nivel"])
print("nivel", config.get("nivel"))

# Adição/Alteração
config["modo"] = "dev"
config["turma"] = "Python 1"
print("Print config com alteração ->",config)

# Método Principais
print("Chaves:", config.keys())
print("Valores:", config.values())
print("Itens:", config.items())

# Interação
for chave, valor in config.items():
    print(chave, ":", valor)
print("Itens Apos interação :", config.items())





























