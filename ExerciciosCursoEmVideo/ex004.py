'''

Faça um programa que receba um valor do teclado, mostre o seu tipo primitivo e todas as informações sobre ele.

'''

n = input('Digite algo: ')

print(f'Ele é uma letra: {n.isalpha}' )
print(f'Ele é um número: {n.isnumeric}')
print(f'Ele é um número e letra: {n.isalnum}')
print(f'São letras maiúsculas: {n.isupper}')
print(f'São letras minúsculas: {n.islower}')
print(f'É número decimal: {n.isdecimal}')
print(f':Tem somente espaço: {n.isspace}')
print(f'É um título: {n.istitle}')
