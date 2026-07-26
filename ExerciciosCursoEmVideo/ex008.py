'''

Escreva um programa que leia um valor em metros e o converta para centímetros e milímetros, exibindo os resultados na tela.

'''

metros = float(input('Informe o valor em metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print(f'Seus {metros}m \nEm centímetros {centimetros}cm \nEm milímetros {milimetros}mm')