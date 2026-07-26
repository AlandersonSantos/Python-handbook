'''

Leia uma quantidade de segundos.

Converta para:

horas
minutos
segundos

Exemplo

7325

2 horas
2 minutos
5 segundos

'''

inforSegundo = int(input('Informe a quantidade de segundos: '))

horas = inforSegundo // 3600
minutos = (inforSegundo % 3600) // 60 
segundos = (inforSegundo % 3600) % 60


print(f'Em horas: {horas}')
print(f'Em minutos: {minutos}')
print(f'Em segundos: {segundos}')