"""

Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.

"""

valor_hora = float(input("Quanto você ganha por hora: R$"))

horas_mes = int(input("Quantas horas você trabalhou: "))

total = valor_hora * horas_mes

print(f"Você trabalhou {horas_mes}h a sua hora custa R${valor_hora} \nrecebendo o total de: R${total:.2f}")