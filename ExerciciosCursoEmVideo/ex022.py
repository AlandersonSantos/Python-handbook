'''

Faça um programa que laia o nome completo de uma pessoa e mostre:

1 - O nome com todas as letras maiúsculas.
2 - O nome com todas as letras minúsculas.
3 - Quantas letras tem ao todo (Sem os espaços).
4 - Quantas letras tem o primeiro nome.

'''

nome = str(input('Escreva seu nome completo: ')).strip()

nomeseparado = nome.split()

print(f'''

Seu nome em letras maiúsculas: {nome.upper()}.

Seu nome em letras minúsculas: {nome.lower()}.

Seu nome tem: {len(''.join(nomeseparado))} letras no seu nome.

O seu primeiro nome tem: {len(nomeseparado[0])} letras.
 
''')
