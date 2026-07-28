'''

faça um programa que receba um valor real qualquer e transforme esse valor em inteiro.


'''




from math import trunc

num_float = float(input('Informe um número com casas decimais: '))


print(f'O seu número escolhido foi: {num_float} \nSeu número inteiro ficar: {trunc(num_float)}')