'''
===========================
FOR 
============================

Uma estrutura de repetição é utilizada para executar um trecho de código várias vezes, 
podendo ter uma quantidade de repetições previamente definida ou indefinida.


FOR – Estrutura de repetição utilizada para percorrer um objeto iterável,
como listas, tuplas, strings, dicionários e outros. 
Geralmente é usada quando a quantidade de iterações é conhecida ou determinada pelo tamanho do objeto iterável.

'''

#FOR com IN (ESTÁ)

texto = input('Informe um texto: ')  # Criamos uma variável que recebe um texto informado pelo usuário.
VOGAIS = 'AEIOU'  # Criamos uma constante contendo todas as vogais em letras maiúsculas.

for letra in texto:  # Criamos uma estrutura de repetição que percorre cada caractere do texto informado.

    if letra.upper() in VOGAIS:  # Convertemos a letra para maiúscula e verificamos se ela está presente na constante VOGAIS.
        print(letra, end=' ')  # Se a letra for uma vogal, ela será exibida na tela, separada por um espaço.


#RANGE

'''
Uma funcção built-in, utilizado para fazer uma sequência de números inteiros,
usandndo um iniciou (inclusivo) e uma final(exclusivo) 

Recebe trêss argumentos:

1 - STOP (obrigatório)
2 - START (opcional)
3 - STEP (opcional)
'''

print(list(range(4))) #Ele vai mostrar o seguinte [0, 1, 2, 3]



#FOR com RANGE

