'''

Faça um programa que leia três números e mostre
qual é o maior e qual é o menor.

'''

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))



maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print(f'O maior número foi: {maior}')
print(f'O menor número foi: {menor}')

#=======Segunda forma=======

a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))

#Verificação do maior número:

maior1 = a

if b > a and b > c:
    maior1 = b
if c > a and c > b:
    maior = c

print(f'O maior valor foi: {maior1}')

#Verificação do menor número:

menor1 = a

if b < a and b < c:
    menor1 = b
if c < a and c < b:
    menor1 = c

print(f'O menor número foi: {menor1}')