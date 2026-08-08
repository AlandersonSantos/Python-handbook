'''

Desenvolva um programa que elai o comprimento
de três retas e diga ao usuário se elas podem ou
não formar um triângulo.

'''

s1 = float(input('Informe o primeiro segmento: '))
s2 = float(input('Informe o segundo segmento: '))
s3 = float(input('Informe o terceito segmento: '))

triangulo = s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2

if triangulo == True:
    print('Os segmentos PODEM FAZER um triângulo')

else:
    print('Os segmentos NÂO PODEM FAZER um triângulo')
