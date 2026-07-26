'''

Faça um programa que elai o valor do sálario de um fúncionario e mostre seu novo sálario, com 15% de aumento.

'''

salario = float(input('Informe o seu sálario: R$ '))

aumento = salario + (salario * 0.15)

print(f'O seu sálario é de: R${salario:.2f} \nCom 15% de aumento ficar: R${aumento:.2f}')