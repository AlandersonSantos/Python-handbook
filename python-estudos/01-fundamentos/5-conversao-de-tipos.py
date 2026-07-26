'''
==================
CONVESÃO DE TIPOS
==================

A convesão de tipos é usado, para deferenciar o valor de tipo para outro ou seja
se recebemos um valor em STRING e queremos passar para INT.

'''

#INTEIRO PARA FLOAT:

preco = 10; #Temos uma variavel do tipo inteiro
print(preco)

#Imagine numa que situação que deseja colocar esse PRECO com casas decimais:

preco = float(preco) #Convertendo o valor inteiro para float, ou seja, com casas decimais.
print(preco) #Ele vai adicionar as casas decimais.

#FLOAT PARA INTEIRO:

altura = 1.75 #Temos uma variavel com casas decimais.
print(altura)

#Mas queremos esse valor em inteiro:

altura = int(altura) #Nessa linha de código, estamos convertendo o valor do tipo float para inteiro.
print(altura) #Ele vai tirar as casas decimais.

#VALORES FLOAT DE DIVISÃO PARA INTEIRO:

maca = 10/3 #O resultado vai gerar casas decimais.
print(maca) #Ele vai escrever com casas decimais.

#Com a mesma situação, queremos o resultado inteiro, podemos usar duas barras:

maca = 10//3 #O resultado vai gerar um valor inteiro, ou seja, sem casas decimais.
print(maca) #Ele vai tirar as casas decimais.

#NÚMEROS PARA STRING:

idade = 22 #Temos um valor do tipo inteiro
print(idade)

#Podemos pegar esse valor e passar para string:

idade = str(idade) #Ele vai alteração, mas não ficar tipo inteiro, e sim string, ou seja, texto.
print(idade)


#STRING PARA NÚMEROS:

preco = '10.50' #Temaos uma variavel do tipo string.
print(preco)

#E queremos usar esse valor em calculo, sendo assim precisando passar para um tipo númerico:

preco = float(preco) #Nessa linha, pegamos o valor string e passamos para um tipo float
print(preco)

preco = int(preco) #Nessa linha, pegamos o valor float e passamos para um tipo inteiro, ou seja, sem casas decimais.
print(preco)

#ERROS DE CONVERSÃO:

#não consiguimos converter um valor string que não seja um número para um tipo númerico, ou seja, float ou inteiro.

#preco = 'dez' #Temos um valor string, mas não é um número.
#preco = float(preco) #Nessa linha, estamos tentando converter um valor string, gerando um erro.