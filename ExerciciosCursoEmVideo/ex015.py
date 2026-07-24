"""

Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado.

Calcule o preço a pagar. Sabendo que o carro custa R$60 por dia e R$0.15 por KM rodados.

"""

dias = int(input("Informe quantos dias você ficou com o carro: "))
km = int(input("Quantos KM rodados: "))

dias_calculo = 60 * dias
km_calculo = 0.15 * km

print(f"O preço a pagar é de: R${dias_calculo + km_calculo:.2f}")