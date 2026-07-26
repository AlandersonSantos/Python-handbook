'''

Leia a idade em anos.

Mostre aproximadamente:

meses
dias

Considere:

12 meses por ano
365 dias por ano

'''

nome = input('Qual seu nome: ')
idade = int(input('Qual a sua idade em anos: '))

meses = 12 * idade
dias = 365 * idade

print(f'''

Olá {nome}, irei calcular sua idade em meses e dias

Sua idade é de: {idade}
      
Sua idade em meses é de: {meses}
      
Sua idade em dias é de: {dias}

''')