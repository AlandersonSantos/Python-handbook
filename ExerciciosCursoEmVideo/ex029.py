'''

Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar de 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada km acima do limite.

'''

km = float(input('Informe a velocidade do carro: '))

if km <= 80:

    print('Está conduzindo na velocidade permitida, pode passar.')

else:

    print('Está conduzindo na velocidade não permitida.')

    multa = (km - 80) * 7
    print(f'Seu carro foi multado em: R${multa:.2f}')