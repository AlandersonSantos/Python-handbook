'''

Leia:

largura
comprimento

Calcule:

área

Depois mostre:

Área: XX m²

'''

print('Área de um Terreno')


largura = float(input('Informe a largura do seu terreno: '))
comprimento = float(input('Informe o comprimento do seu terreno: '))

area = largura * comprimento

print(f'''

Área: {area:.2f} m²

''')