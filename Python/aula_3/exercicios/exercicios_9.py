#   Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
farenheit = float(input("Digite um n. de graus celsius para ser calculado: "))

celsius = (5 * (farenheit-32) / 9)
print(F'O Graus Celsius calculados é calculado é {celsius:.2f} °F.')


