'''

Faça um programa que leia uma frase uma frase pelo teclado e mostre:

- Quantas vezes aparece a letra 'A'.
- Em que posição aparece a primeira vez.
- Em que posição aparece a ultima vez.

'''

frase = str(input('Informe uma frase: ')).strip().upper()


print(f'''

Aparece o taltal de: {frase.count('A')} de letras 'A'

A primeira letra 'A' está no índice: {frase.find('A') + 1}

A ultima letra 'A' está no índice: {frase.rfind('A') + 1}

''')