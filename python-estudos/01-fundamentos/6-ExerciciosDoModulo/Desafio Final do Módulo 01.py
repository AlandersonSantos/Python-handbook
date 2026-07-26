'''

Sistema de Cadastro

Crie um pequeno sistema que solicite:

nome
idade
altura
peso
profissão
cidade

Depois calcule:

IMC
idade em meses
idade em dias

Ao final exiba um relatório organizado, por exemplo:

==========================
        CADASTRO
==========================

Nome:
Profissão:
Cidade:

Idade:
Meses:
Dias:

Peso:
Altura:
IMC:

==========================

'''

nome = input('Informe o seu nome: ')

sobrenome = input('Informe seu primeiro sobrenome: ')

idade = int(input('Qual a sua idade: '))

altura = float(input('Qual sua altura atual: '))

peso = float(input('Qual o seu peso atual: '))

email = input('Informe seu E-mail: ')

profissao = input('Qual a sua profissão: ')

cidade = input('Qual a sua cidade: ')


imc = peso / (altura ** 2) 

idade_meses = 12 * idade
idade_dias = 365 * idade


print(f'''


==========================
    CADASTRO REALIZADO
==========================

      
Seja bem-vindo {nome} {sobrenome}!!

e-mail cadastrado: {email}

Sua profissão {profissao}, deve ser cansativa

Você mora em {cidade}, é uma cidade linda!!

Sua idade: {idade}
Sua idade em meses: {idade_meses}
Sua idade em dias: {idade_dias}

Você tem {altura:.2f} de altura
Você tem atualmente{peso:.2f} kilos
O seu Índice de Massa Corporal (IMC) é de: {imc:.2f}

''')



