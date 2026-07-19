"""

Leia um número.

Informe se ele é:

positivo
negativo
ou igual a zero.

"""

numero = int(input("Informe um número inteiro: "))

if numero > 0:
    print("Esse número é positivo!!")

elif numero < 0:
    print("Esse número é negativo!!")

else:
    print("O número informado é zero!!")