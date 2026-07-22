"""

Crie um programa que leia dois números e depois mostre a soma

"""

n1 = input("Escolha um número: ") # valor 1
n2 = input("Escolha mais um número: ") # valor 1
s = n1 + n2 # 1 + 1 = 2

print('A soma vale', s) # Ocorre um erros, pois ele não soma, mas sim concatena os valores ficando: 11

#Forma correta: 

n1 = int(input("Escolha um número: ")) # valor 1
n2 = int(input("Escolha mais um número: ")) # valor 1

print('A soma vale', s)