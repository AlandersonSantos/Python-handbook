'''

crie um programa que leia a quantia de dinheiro que uma pessoa tem na carteira e mostre quantos dólares
ela pode comprar.

Considere: U$ 1.00 = R$ 3.27

'''

reais = float(input('Informe quantos reais você tem: R$'))

con_dolares = reais // 3.27

print(f'Você tem: R${reais:.2f} \nEm dólares você tem: U${con_dolares:.2f}')