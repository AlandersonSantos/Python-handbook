'''
Crie um programa que:

peça o nome;
peça a idade;
peça a cidade.

Depois mostre uma mensagem semelhante a:

Olá João, você tem 22 anos e mora em Recife.

'''
nome = input('Informe o seu nome: ')
idade = int(input('Informe sua idade: '))
cidade = input('Informe sua cidade: ')

print(f'Olá {nome}, você tem {idade} idade, e mora em {cidade}')