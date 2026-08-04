'''

Crie um programa que leia o nome completo de uma pessoa
e diga se ela tem ou não o "Silva" no nome.

'''

nome = str(input('informe o seu nome completo: ')).strip()


print(f'Seu nome tem Silva: {'SILVA' in nome.upper()}')