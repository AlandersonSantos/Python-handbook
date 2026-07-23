"""

Faça um programa que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

"""

produto = float(input("Informe o valor do produto: "))

desconto = produto - ( produto * 0.05)

print(f"O valor do produto é de: R$ {produto} \nCom desconto de 5%, ficar por: R$ {desconto}")