"""

Faça um programa que peça o raio de um círculo, calcule e mostre sua área:

"""

raio = float(input("Informe o valor do raio: "))
PI = 3.14

area = PI * (raio ** 2)

print(f"""

A área de um círculo com o raio de {raio} é igual a: {area:.2f}cm

""")