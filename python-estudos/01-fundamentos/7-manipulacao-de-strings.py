'''
======================
MANIPULAÇÃO DE STRINGS
======================

Manipulação de strings, também conhecida como manipulação de cadeias de caracteres,
é o conjunto de técnicas utilizadas para trabalhar com textos em um programa.

'''

# ====================
# TEORIA
# ====================

# Criamos uma variável que recebe uma frase.

frase = 'Linux o sistema operacional'

# Na memória, o Python armazena a string da seguinte maneira:
# Cada caractere ocupa uma posição chamada de índice.
# Os índices sempre começam em zero.

# [L] [i] [n] [u] [x] [ ] [o] [ ] [s] [i] [s] [t] [e] [m] [a] [ ] [o] [p] [e] [r] [a] [c] [i] [o] [n] [a] [l]
#  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26

# Com isso, podemos realizar algumas operações.

# ====================
# OPERAÇÕES
# ====================


# ====================
# 1 - FATIAMENTO
# ====================


# É a forma de acessar um caractere específico ou uma parte da string.

# Mostra a frase inteira.
print(frase)

# Estamos solicitando apenas o caractere do índice 9.
# Lembre-se de que os índices começam em zero.
# Resultado: i
print(frase[9])

# Também podemos pegar um intervalo de caracteres.
# A sintaxe é:
#
# string[início:fim]
#
# O índice inicial é incluído, mas o índice final NÃO.
# Ou seja, o Python sempre para uma posição antes do índice informado.

# Exemplo:
# Queremos pegar a palavra "Linux".

print(frase[0:4])  # Resultado: Linu

# Podemos informar um índice maior que o tamanho da string.
# O Python simplesmente irá até o último caractere disponível.

print(frase[8:27])  # Resultado: sistema operacional

# Também podemos informar um índice inicial, um índice final
# e pular de caractere em caractere.
# Sintaxe é:
#
# string[início:fim:puleDe]
#
# O índice inicial é incluído, mas o índice final NÃO.
# O terceiro valor indica de quantos em quantos caracteres o Python irá percorrer a string.

# Exemplo:
# Queremos pegar a frase "sistema operacional",
# pulando de dois em dois caracteres.

print(frase[8:27:2])  # Resultado: sseaoeainl

# Também podemos omitir o índice inicial.
# Se omitirmos esse valor, o Python começará do índice 0.
# Sintaxe é:
#
# string[:fim]
#
# Estamos dizendo: pegue do índice 0 até o índice informado.

# Exemplo:

print(frase[:5])  # Resultado: Linux

# Também podemos omitir o índice final.
# Se omitirmos esse valor, o Python irá até o último caractere da string.
# Sintaxe é:
#
# string[início:]
#
# Estamos dizendo: pegue do índice informado até o final da string.

# Exemplo:

print(frase[0:])  # Resultado: Linux o sistema operacional

# Também podemos omitir o índice final e informar um passo.
# Sintaxe é:
#
# string[início::puleDe]
#
# Estamos dizendo: comece no índice informado,
# vá até o final da string e percorra os caracteres
# pulando conforme o valor informado.

# Exemplo:

print(frase[0::2])  # Resultado: Lnxosseaoeainl

# ====================
# 2 - ANÁLISE
# ====================

# Operações de análise servem para obter informações sobre uma string.

# Método: len()
# Usado para mostrar o comprimento (quantidade de caracteres) da string.
#
# Sintaxe:
#
# len(string)

# Exemplo:

print(len(frase))  # Resultado: 27, pois a string possui 27 caracteres.

# Método: .count()
# Usado para contar quantas vezes um valor aparece na string.
# Para o Python, letras maiúsculas e minúsculas são diferentes.
#
# Sintaxe:
#
# string.count("valor")

# Vamos contar quantas letras 'o' minúsculas existem.

# Exemplo:

print(frase.count('o'))  # Resultado: 3, existem três letras 'o' minúsculas.

# Também podemos fazer a contagem apenas em uma parte da string.
#
# Sintaxe:
#
# string.count('valor', início, fim)
#
# Vamos contar quantos 'o' existem do índice 0 até o índice 14.

# Exemplo:

print(frase.count('o', 0, 15))  # Resultado: 1

# Método: .find()
# Usado para encontrar uma palavra ou trecho dentro da string.
#
# Sintaxe:
#
# string.find('valor')
#
# Vamos procurar o trecho "tem".

# Exemplo:

print(frase.find('tem'))  # Resultado: 11, pois "tem" começa no índice 11.

# Caso o valor informado não exista na string,
# o método retornará -1.

# Exemplo:

print(frase.find('Mundo'))  # Resultado: -1, pois essa palavra não existe.

# Também podemos utilizar o operador "in".
# Ele serve para verificar se um valor existe dentro da string.
#
# Sintaxe:
#
# 'valor' in variável

# Exemplo:

print('Linux' in frase)  # Resultado: True, pois a palavra "Linux" existe na variável frase.

# ====================
# TRANSFORMAÇÃO
# ====================

# Os métodos de transformação são utilizados para modificar a forma como uma string é apresentada,
# como converter letras para maiúsculas ou minúsculas,
# substituir palavras ou remover espaços.
#
# Entretanto, em Python, strings são imutáveis,
# ou seja, seu conteúdo não pode ser alterado diretamente.
# Sempre que fazemos uma transformação, o Python cria uma nova string,
# enquanto a original permanece a mesma.

# Método: .replace()
# Usado para substituir um valor por outro.
#
# Sintaxe:
#
# string.replace('ValorOriginal', 'ValorNovo')
#
# Podemos usar para trocar "Linux" por "MacOS".

# Exemplo:

print(frase.replace('Linux', 'MacOS'))  # Resultado: MacOS o sistema operacional

# Método: .upper()
# Usado para transformar todos os caracteres em maiúsculas.
#
# Sintaxe:
#
# string.upper()

# Exemplo:

print(frase.upper())  # Resultado: LINUX O SISTEMA OPERACIONAL

# Método: .lower()
# Usado para transformar todos os caracteres em minúsculas.
#
# Sintaxe:
#
# string.lower()

# Exemplo:

print(frase.lower())  # Resultado: linux o sistema operacional

# Método: .capitalize()
# Usado para transformar todos os caracteres em minúsculas,
# deixando apenas o primeiro caractere da string em maiúsculo.
#
# Sintaxe:
#
# string.capitalize()

# Exemplo:

print(frase.capitalize())  # Resultado: Linux o sistema operacional

# Método: .title()
# Usado para transformar a primeira letra de cada palavra em maiúscula.
# A separação das palavras é feita pelos espaços.
#
# Sintaxe:
#
# string.title()

# Exemplo:

print(frase.title())  # Resultado: Linux O Sistema Operacional


# ====================
# NOVA STRING
# ====================

# Para os próximos métodos vamos utilizar uma nova string.

fraseNova = '   Aprenda sistema   '  # Com três espaços no início e no final.

# Em algumas situações, usuários podem inserir espaços extras
# apenas para testar ou por engano.
# Isso pode causar problemas durante a validação dos dados.
# Os métodos abaixo ajudam a remover esses espaços.

# Método: .strip()
# Remove os espaços do início e do final da string.
#
# OBS: Os espaços também são considerados caracteres.
#
# Sintaxe:
#
# string.strip()

# Exemplo:

print(fraseNova)          # Resultado:    Aprenda sistema
print(fraseNova.strip())  # Resultado: Aprenda sistema


# Método: .rstrip()
# Possui a mesma função do .strip(),
# porém remove apenas os espaços da direita (Right).
#
# Sintaxe:
#
# string.rstrip()

# Exemplo:

print(fraseNova)           # Resultado:    Aprenda sistema
print(fraseNova.rstrip())  # Resultado:    Aprenda sistema


# Método: .lstrip()
# Possui a mesma função do .strip(),
# porém remove apenas os espaços da esquerda (Left).
#
# Sintaxe:
#
# string.lstrip()

# Exemplo:

print(fraseNova)           # Resultado:    Aprenda sistema
print(fraseNova.lstrip())  # Resultado: Aprenda sistema   


# ====================
# DIVISÃO
# ====================

# Podemos dividir e juntar strings.

fraseDivisao = 'Linux o sistema operacional'

# Método: .split()
# Usado para dividir a string em partes.
# Por padrão, ele utiliza os espaços como separador,
# criando uma lista onde cada palavra se torna um elemento.
#
# Sintaxe:
#
# string.split()

# Exemplo:

NovaDivisao = fraseDivisao.split()

print(NovaDivisao)

# Resultado:
# ['Linux', 'o', 'sistema', 'operacional']

# ANTES:
#
# [L] [i] [n] [u] [x] [ ] [o] [ ] [s] [i] [s] [t] [e] [m] [a] [ ] [o] [p] [e] [r] [a] [c] [i] [o] [n] [a] [l]
#  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26

# DEPOIS:
#
# Lista
#
# Índice da lista:
#
#      0          1          2              3
# ['Linux',     'o',     'sistema',   'operacional']
#
# Cada elemento continua sendo uma string,
# portanto cada um possui seus próprios índices.
#
# "Linux"
#  0 1 2 3 4
#
# "sistema"
#  0 1 2 3 4 5 6


# ====================
# JUNÇÃO
# ====================

# Podemos juntar novamente a lista criada pelo .split().
# Primeiro armazenamos o resultado em uma variável
# para depois realizar a junção.

# Método: .join()
# Usado para unir os elementos de uma lista.
# O valor antes do .join() define qual separador será utilizado.
#
# Sintaxe:
#
# 'Separador'.join(lista)

# Exemplo:

print('-'.join(NovaDivisao))

# Resultado:
# Linux-o-sistema-operacional

# Também podemos utilizar um espaço como separador,
# retornando a frase ao formato original.

print(' '.join(NovaDivisao))

# Resultado:
# Linux o sistema operacional


