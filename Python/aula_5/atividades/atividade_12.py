#   12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
#   e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
#   O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.  

#   - Desconto do IR:
#   - Salário Bruto até 900 (inclusive) - isento
#   - Salário Bruto até 1500 (inclusive) - desconto de 5%
#   - Salário Bruto até 2500 (inclusive) - desconto de 10%
#   - Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 
# e a quantidade de hora é 220.

#   Salário Bruto: (5 * 220)        : R$ 1100,00
#   (-) IR (5%)                     : R$   55,00  
#   (-) INSS ( 10%)                 : R$  110,00
#   FGTS (11%)                      : R$  121,00
#   Total de descontos              : R$  165,00
#   Salário Liquido                 : R$  935,00



valor_hora = float(input('Digite o valor da hora trabalhada'))
qt_hora = float(input('Digite a quantidade de hora trabalhada'))
salario_bruto = valor_hora * qt_hora

#print(f'Salário Bruto: {valor_hora} * {qt_hora}        : R$ {salario_bruto}')
print('Salário Bruto:',valor_hora * qt_hora,': R$ ',salario_bruto)

if salario_bruto <= 900:
    irtexto = 'isento'
    ir = 0  
elif salario_bruto >900 and salario_bruto <= 1500:
    #ir = salario_bruto * 0.05
    irtexto = '5%'
    ir = salario_bruto * 5 / 100
elif salario_bruto >1500 and salario_bruto <= 2500:
    #ir = salario_bruto * 0.1
    irtexto = '10%'
    ir = salario_bruto * 10 / 100
else:
      irtexto = '20%'
      ir = salario_bruto * 20 / 100

print(f'(-) IR ({irtexto})                     : R$   {ir}')

inss = 