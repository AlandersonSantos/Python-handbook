'''

Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.

'''

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe mais um número inteiro: '))
n3 = float(input('Informe um número real: '))

print(f' O produto do dobro do primeiro com metade do segundo: {(n1 * 2) * (n2 / 2)}')

print(f' A soma do triplo do primeiro com o terceiro: {(n1 * 3) + n3}')

print(f' O terceiro elevado ao cubo: {n3 ** 3}')
