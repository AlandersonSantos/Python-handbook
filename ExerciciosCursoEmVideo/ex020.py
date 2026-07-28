'''

Um professor deseja fazer uma apresentação de projeto, ele solicitou um programa que sortear a ordem de apresentação.


'''

import random

aluno1 = input('Informe o seu nome aluno(a): ')
aluno2 = input('Informe o seu nome aluno(a): ')
aluno3 = input('Informe o seu nome aluno(a): ')
aluno4 = input('Informe o seu nome aluno(a): ')

nomes = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(nomes)

print(f'A ordem da apresentação: {nomes}')