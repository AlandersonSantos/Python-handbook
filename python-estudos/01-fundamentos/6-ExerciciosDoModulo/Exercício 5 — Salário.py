'''

Peça:

nome
horas trabalhadas
valor da hora

Valor de 1h =  R$ 7,37

'''

nome = input('Informe seu nome: ')
horas_trabalhadas = float(input('Informe quantas horas trabalhas: '))
valor_hora = 7.37

valor_receber = valor_hora * horas_trabalhadas

print(f'''

Funcionario(a): {nome}

Suas horas trabalhas foi de: {horas_trabalhadas}h

o seu total a receber é de: R$ {valor_receber:.2f}


''')