"""

crie um programa que leia a quantia de dinheiro que uma pessoa tem na carteira e mostre quantos dólares
ela pode comprar.

Considere: U$ 1.00 = R$ 3.27

"""

reais = float(input("Informe quanto reais você tem: "))

con_dolares = reais // 3.27

print(f"Você tem: R${reais} \nEm dólares você tem: U${con_dolares:.2f}")