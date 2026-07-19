"""

Peça a idade do usuário.

Mostre:

"Maior de idade"
ou
"Menor de idade"

"""

MAIOR_IDADE = 18

idade = int(input("Informe a sua idade:"))

print("Maior de idade" if idade >= MAIOR_IDADE else "Menor de idade")