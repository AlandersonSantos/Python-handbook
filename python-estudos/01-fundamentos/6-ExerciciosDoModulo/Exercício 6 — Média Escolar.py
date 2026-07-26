'''

Leia três notas.

Calcule a média.

Mostre com duas casas decimais.

'''

nome = str(input('Informe o seu nome: '))

nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))
nota3 = float(input('Informe sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3


print(f'''

Olá aluno(a): {nome}

Sua média foi de: {media:.2f}

''')