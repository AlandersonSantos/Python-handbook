'''
==================
OPERADORES ARITMÉTICOS
==================

Os operadores aritméticos são usados para realizar operações matemáticas entre valores numéricos.

'''

#ADIÇÃO:
print(1+1) #Ele vai mostrar o resultado: 2

#SUBTRAÇÃO:
print(10-2) #Ele vai mostrar o resultado: 8

#MULTIPLICAÇÃO:
print(10*2) #Ele vai mostrar o resultado: 20

#DIVISÃO:
print(12/3) #Ele vai mostrar o resultado: 4.0

#DIVISÃO INTEIRA:
print(12//3) #Ele vai mostrar o resultado: 4

#EXPONENCIAÇÃO:
print(2**3) #Ele vai mostrar o resultado: 8, ou seja, 2*2*2

#MODULO:
print(10%3) #Ele vai mostrar o resultado: 1, ou seja, o resto da divisão.


'''
==================
PRECEDÊNCIA DOS OPERADORES
==================

Regra que indicar qual equeação será feita primeiro, ou seja quem tem prioridade.

Ordem correta de precedência:
1º : () - Paraneteses
2º : ** - Exponenciação
3º : * / // % - Multiplicação, Divisão, Divisão Inteira e Módulo
4º : + - Adição e Subtração

'''
#EXEMPLO 1:

print(10-5*2) #Ele vai primeiro multiplicar 5*2 = 10, e depois subtrair 10-10 = 0.

#EXEMPLO 2:
print((10-5)*2) #Ele vai primeiro subtrair 10-5 = 5, e depois multiplicar 5*2 = 10.

#EXEMPLO 3:
print(10**2*2) #Ele vai primeiro fazer a exponenciação 10**2 = 100, e depois multiplicar 100*2 = 200.

#EXEMPLO 4:
print(10**(2*2)) #Ele vai primeiro fazer a multiplicação 2*2 = 4, e depois fazer a exponenciação 10**4 = 10000.

#EXEMPLO 5:
print(10/2*4) #Ele vai primeiro fazer a divisão 10/2 = 5, e depois multiplicar 5*4 = 20.



'''
==================
OPERADORES COMPARAÇÃO
==================

    Os operadores de comparação são usados para comparar valores e retornar um valor booleano (True ou False).

'''
#VARIÁVEIS USADAS PARA COMPARAR:
saldo = 450
saque = 200


#IGUALDADE:
print(saldo == saque) #Ele vai retornar um false, pois são valores diferentes.

#DIFERENÇA:
print(saldo!= saque) #Ele vai retornar um true, pois são valores diferentes.

#MAIOR que / MAIOR OU IGUAL:
print(saldo > saque) # Ele vai retornar um true, pois 450 é maior que 200.
print(saldo >= saque) # Ele vai retornar um true, pois 450 é maior ou igual a 200.

#MENOR que / MENOR OU IGUAL:
print(saldo < saque) # Ele vai retornar um false, pois 450 não é menor que 200.
print(saldo <= saque) # Ele vai retornar um false, pois 450 não é menor

'''
==================
OPERADORES DE ATRIBUIÇÃO
==================

    São usados para definir um valor inicial ou sobrepor esse valor a uma variável.

    isso: 'saldo += 100' é o mesmo que isso: 'saldo = saldo + 100' , mas resumido

'''

#ATRIBUIÇÃO SIMPLES:
saldo = 600 #A variável saldo recebe o valor 600.


#ATRIBUIÇÃO COM ADIÇÃO:
saldo += 100 #A variável saldo recebe o valor 600 + 100 = 700.
print(saldo)


#ATRIBUIÇÃO COM SUBTRAÇÃO:
saldo -= 200 #A variável saldo recebe o valor 700 - 200 = 500.
print(saldo)


#ATRIBUIÇÃO COM MULTIPLICAÇÃO:
saldo *= 2 #A variável saldo recebe o valor 500 * 2 = 1000.
print(saldo)


#ATRIBUIÇÃO COM DIVISÃO:
saldo /= 4 #A variável saldo recebe o valor 1000 / 4 = 250.
print(saldo)


#ATRIBUIÇÃO COM DIVISÃO INTEIRA:
saldo //= 2 #A variável saldo recebe o valor 250 // 2 = 125.
print(saldo)


'''
==================
OPERADORES LÓGICOS
==================

    São usados para combinar expressões booleanas (True ou False) e retornar um valor booleano. 

    OS TIPOS DE OPERADORES LÓGICOS SÃO:

    - AND (E): só retorna True se todas as variáves forem verdadeiras.
    - OR (OU): retorna True se pelo menos uma das variáveis for verdadeira.
    - NOT (NÃO): inverte o valor da variável, ou seja, se for True ele retorna False, e se for False ele retorna True.


'''

saldo = 1000
saque = 200
limite = 100

#OPERADOR AND (E):
print(saldo >= saque and saque <= limite)  # Ele ira retorna false, pois a segunda expressão é falsa.


#OPERADOR OR (OU):
print(saldo >= saque or saque <= limite) # Ele ira retorna true, pois a primeira expressão é verdadeira.


#OPERADOR NOT (NÃO):
print(not(saldo >= saque and saque <= limite)) # Ele ira retorna true, pois a segunda expressão é falsa, e o operador NOT inverte o valor para true.


saldo = 1000
saque = 200
limite = 100
conta_especial = True

#PARENTESES:

# 1 - PRIMEIRA FORMA:
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque) 
# Ele ira retorna true, pois a primeira expressão é falsa, mas a segunda é verdadeira, e o operador OR retorna true se pelo menos uma das expressões for verdadeira.

# 2 - PRIMEIRA FORMA:
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)) 
# Ele ira retorna true, pois a primeira expressão é falsa, mas a segunda é verdadeira, e o operador OR retorna true se pelo menos uma das expressões for verdadeira.


''''
==================
OPERADORES DE IDENTIDADE
==================

    São usados para comparar a identidade de dois objetos testando se ocupa o mesmo espaço na memoria.

    OS OPERADORES DE IDENTIDADE SÃO:
    - IS (É): retorna True se os dois objetos forem o mesmo objeto.
    - IS NOT (NÃO É): retorna True se os dois objetos não forem o mesmo objeto.

'''

curso = 'python'
nome_curso = curso
saldo,limite = 200, 200

print(curso is nome_curso)  # Ele ira retorna true, pois os dois objetos são o mesmo.

print(curso is  not nome_curso)  # Ele ira retorna false, pois os dois objetos são o mesmo.

print(saldo is limite)  # Ele ira retorna true, pois os dois objetos são o mesmo.

''''
==================
OPERADORES DE ASSOCIAÇÃO
==================

    São usados para verificar se um valor está presente em uma sequência (lista, tupla, string, etc).

    OS OPERADORES DE ASSOCIAÇÃO SÃO:
    - IN (ESTÁ): retorna True se o valor estiver presente na sequência.
    - NOT IN (NÃO ESTÁ): retorna True se o valor não estiver presente na sequência.

'''

curso = 'Curso de Python'
frutas = ['banana', 'maçã', 'laranja']
saque = [200, 300, 400]

print('Python' in curso)  # Ele ira retorna true, pois o valor 'Python' está presente na sequência.

print('maçã' in frutas)  # Ele ira retorna true, pois o valor 'maçã' está presente na sequência.

print('uva' not in frutas)  # Ele ira retorna true, pois o valor 'uva' não está presente na sequência.

print(500 in saque)  # Ele ira retorna false, pois o valor 500 não está presente na sequência.