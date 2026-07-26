'''

Tendo como dados de entrada um arquivo em Gigabytes,
construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:

Gigabytes * 1024

'''

gigabytes = float(input('Informe a quantidade de gigabytes: '))

megabytes = gigabytes * 1024

print(f'A quantidade de {gigabytes}GB o arquivo tem {megabytes}MGs')