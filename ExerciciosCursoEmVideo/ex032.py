'''

Faça um programa que leia um ano qualquer
e mostre se ele é bissexto.

'''

import calendar
from datetime import date

print('Escolha um ano, para ver se ele é BISSEXTO.')
print('Coloque 0 para saber o ano atual.')

ano = int(input('Informe o ano que deseja ser analisado: '))

if ano == 0:
    ano = date.today().year

if calendar.isleap(ano) == True:
    print(f'Sim, esse ano de {ano} é bissexto')

else:
    print(f'Não, esse ano de {ano} não é bissexto')

