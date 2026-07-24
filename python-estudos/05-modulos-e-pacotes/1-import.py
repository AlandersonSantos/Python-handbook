"""
==========================
FROM IMPORT / IMPORT
==========================

O Python possui diversos módulos prontos, chamados de biblioteca padrão
(Standard Library), como:

- math
- random
- datetime
- os
- sys

Também é possível instalar bibliotecas criadas por outras pessoas utilizando
o gerenciador de pacotes pip.

----------------------------------

Conceitos

Biblioteca
É um conjunto de módulos e pacotes que possuem um objetivo específico.

Módulo
É um arquivo Python (.py) que contém funções, classes, variáveis e constantes.

----------------------------------

Como utilizar

Existem duas formas principais de importar um módulo.

1) Importar o módulo inteiro

import math

Nesse caso, todas as funções do módulo ficam disponíveis utilizando
o nome do módulo.

Exemplo:

math.sqrt(25)
math.factorial(5)

----------------------------------

2) Importar apenas o que será utilizado

from math import hypot

Nesse caso, apenas a função hypot é importada.

Exemplo:

hipotenusa = hypot(3, 4)

Assim não é necessário escrever:

math.hypot(3, 4)
"""

#PRÁTICA

# 1) Importar o módulo inteiro

import math # Nesse comando estou importando o módulo inteiro: Ceil, floor, trunc,pow, sqrt, factorial....


numero = int(input("Informe um número: "))

raiz = math.sqrt(numero) #Quando importamos o módulo inteiro, precisamos colocar: math.função que vamos usar.

print(f"A raíz quadrada de {numero} e igual a {math.ceil(raiz)} #Estamos arredondando para cima") 


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 2) Importar apenas o que será utilizado

from math import sqrt # Nesse comando, eu quero somente importar o sqrt (Usado para calcúlos de raíz quadrada).


from math import sqrt, ceil, floor # Nesse comando, eu quero somente importar o sqrt e ceil (usado para arredondar para cima).


numero2 = int(input("Informe um número: "))

numero2 = sqrt(numero) #Diferente do outro, não precisamos chamar o módulo "math.funçaõ", mas sim somente a função.

print(f"A raíz quadrada de {numero} e igual a {floor(raiz)} #Estamos arredondando para baixo") 