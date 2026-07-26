'''

Leia:

peso
altura

Calcule o IMC.

Mostre apenas o valor (sem classificar).

'''

nome = input('Qual o seu nome: ')
altura = float(input('Qual sua altura: '))
peso = float(input('Qual o seu peso: '))

imc = peso / (altura ** 2)

print(f'O seu Índice de Massa Corporal (IMC) é de: {imc:.2f}')
