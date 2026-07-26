'''

Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

Formúla: C = 5 * ((F-32) / 9).

'''

f = float(input('Informe o grau em Fahrenheit: '))

c = 5 * ((f - 32) / 9)

print(f' O grau em {f}f°, tranformado em {c:.1f}c°')