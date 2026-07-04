"""

Faça um programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.

"""

lado = float(input("Informe o valor do lado do quadrado: "))

area = lado ** 2

dobro = area * 2

print(f"""

Área do quadrado é de: {area}

O valor em dobro é de: {dobro}


""")