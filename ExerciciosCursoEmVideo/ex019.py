'''

Um professor deseja sortear de quatro alunos, um aluno para apagar o quadro.
Faça um programa que recebe os nomes do alunos e escreva o nome do aluno escolhido.

'''

import random

aluno1 = input('Informe o seu nome aluno(a): ')
aluno2 = input('Informe o seu nome aluno(a): ')
aluno3 = input('Informe o seu nome aluno(a): ')
aluno4 = input('Informe o seu nome aluno(a): ')

nomes = [aluno1, aluno2, aluno3, aluno4]

print(random.choice(nomes))

