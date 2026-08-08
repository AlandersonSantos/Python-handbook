'''

Faça um programa que receba a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por km, para viagens de até
200km e R$0,45 para viagens mais longas.

'''

km = float(input('Qual a sua distância da sua viagem: '))

if km >= 200:
    print('Uma viagem bem longa, ganhou um desconto!!')

    passagem_com_desconto = km * 0.45

    print(f'Você vai pagar: R${passagem_com_desconto:.2f} na passagem')

else:

    print('Sua viagem não chega a 200km, sem desconto')

    passagem_sem_desconto = km * 0.50

    print(f'Você vai pagar: R${passagem_sem_desconto:.2f}')

print('Tenha uma boa viagem!!')
