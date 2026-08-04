'''

Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome.

'''

nome = str(input('Informe seu nome completo: ')).strip()

nome_tratado = nome.split()

print(f'''

{nome}

Seu primeiro nome: {nome_tratado[0]}

seu último nome: {nome_tratado[-1]}

''')