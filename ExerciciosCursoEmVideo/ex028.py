'''

Escreva um programa que faça o computador 'pensar' em um número
inteiro entre 0 e 5 e peça para que o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá
escreve na tela se ganhou ou perdeu.

'''

from random import randint
from time import sleep

print('-+-' * 15)
print('Irei escolher um número entre 0 e 5. Tente acerta')
print('-+-' * 15)

usuario = int(input('Qual número você acha que pensei: '))

computador = randint(0,5)

print('PROCESSANDO...')
sleep(3)

if computador == usuario:
    print('Você acertou!!')
    print(f'Meu número {computador} o seu número {usuario}')

else:
    print('Você perdeu!!')
    print(f'Meu número {computador} o seu número {usuario}')

print('Obrigado por jogar!! ')