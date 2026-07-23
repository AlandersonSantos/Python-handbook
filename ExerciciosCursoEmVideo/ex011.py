"""

Faça um rpograma que receba o valor da largura e altura de uma parede em metros, calcule a área e a quantidade de tinta
necessaria para pintala.

Cada lata de tinta pinta uma área de 2m²

"""

altura = float(input("Informe a altura da parede em metros: "))
largura = float(input("Informr a largura da parede em metros: "))


area = altura * largura

tinta = area // 2

print(f"A área da sua parede é de: {area}m² \nVocê precisa de {tinta} latas de tintas.")