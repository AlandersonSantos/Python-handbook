'''

Crie um programa que leia o nome de uma cidade e diga
se ela começa ou não com o nome "Santo".

'''

cidade = str(input('Informe um nome de uma cidade: ')).strip()

cidadetratado = cidade.upper()

print(f'''

A cidade começa com Santa: {cidadetratado[:5] == 'SANTO'}

''')