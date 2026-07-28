'''

Faça um programa que recebe o valor do cateto oposto e o cateto adjacente de um triângulo retangulo,
mostre o comprimento da hipotenusa.

'''

from math import hypot

cat_oposto = float(input('Informe o valor do cateto oposto: '))
cat_adjacente = float(input('Informe o valor do cateto adjacente: '))

hipo = hypot(cat_oposto, cat_adjacente)

print(f'O valor da hipotenusa é: {hipo:.2f}')