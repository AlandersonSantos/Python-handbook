'''
==================
VARIÁVEIS
==================

São valores que podem ser alterado ao decorrer do código, conhecidas como valores MUTÁVEL, ou seja, podem ser modificadas.

'''

#Criando uma variável

nome = 'Jesus Cristo' #Nossa variável 'nome' , recebe um valor 'Jesus cristo'
print(nome)

idade = 33 #Nossa variável 'idade' recebe um valor inteiro '33'
print(idade)

#Tambbém podemos criar duas variaveis na mesma linha de código, basta separar por virgula:

cidade, estado = 'Marechal Deodoro', 'Alagoas' #Criamos duas variáveis.
print(cidade, estado)

'''
==================
CONSTANTES
==================

São valores que não são alterados ao decorrer do código, conhecidas como valores IMUTÁVEL, ou seja, não podem ser alteradas.

No python não existe uma forma de criar uma CONSTANTE, para identificar isso, escrevemos ela com letra MAIÚSCULA.

'''

ESTADO_SIGLA = ['AL','BH','SP'] #Essa variavel nunca sera alterada, pois uma lista de siglas de estado, sendo uma constante, ou seja, um valor imutável.
print(ESTADO_SIGLA)