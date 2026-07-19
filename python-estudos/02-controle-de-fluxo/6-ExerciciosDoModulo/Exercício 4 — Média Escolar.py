"""

Leia três notas.

Calcule a média.

Mostre:

Aprovado (média ≥ 7)
Recuperação (média entre 5 e 6.9)
Reprovado (média < 5)

"""

nota1 = float(input("Informe a sua primeira nota: "))
nota2 = float(input("Informe a sua segunda nota: "))
nota3 = float(input("Informe a sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Meus parabéns, você passou!!")

elif media >= 5 :
    print("Você está de recuperação, estude mais!!")

else:
    print("Você foi reprovado, tente novamente!!")