'''

Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

'''

print('-+-' * 15)
print('calculadora para o aumento de salário!!')
print('-+-' * 15)

salario = float(input('Informe o valor do seu salário: R$'))

if salario <= 1250:

    novo_salario = salario + (salario * 0.15)
    print(f'Seu antigo R${salario:.2f} novo salário é: R${novo_salario:.2f}')

else:

    novo_salario = salario + (salario * 0.10)
    print(f'Seu antigo R${salario:.2f} novo salário é: R${novo_salario:.2f}')