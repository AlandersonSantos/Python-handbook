'''

Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

Formula: F = (C * 9/5) + 32

'''

c = float(input('Informe a temperatura em celsius: '))

f = (c * 1.8) + 32

print(f' o grau em {c}c° para {f:.1f}f°')
