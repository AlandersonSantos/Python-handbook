'''

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do: Cosseno, seno e tangente desse ângulo.

'''

from math import sin, cos, tan, radians


angulo = float(input('Informe o ângulo: '))

seno = sin(radians(angulo))
cons = cos(radians(angulo))
tan = tan(radians(angulo))

print(f'''

ângulo informado foi: {angulo}

Seno desse ângulo é: {seno:.2f}

Tangente desse ângulo é: {tan:.2f}

Cosseno desse ângulo é: {cons:.2f}


''')
