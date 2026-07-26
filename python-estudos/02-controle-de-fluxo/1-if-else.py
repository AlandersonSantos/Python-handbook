'''
==================
ESTRUTURA CONDICIONAIS
==================

Estrutura cooncidcionais, são elementos usados para fazer mudanças de resultados de acordo,
com alguma condição lógica.

'''

# IF - Estrutura simples, podemos fazer até um desvio de fluxo. Exemplo:

saldo = 200
saque = float(input('Informe o valor do saque: '))

if saldo > saque: #Se o saldo e máior que o saque, se for verdadeiro ele vai executar o bloco.
    print('Saque Realizado com sucesso!')


# IF & ELSE - estrutura que nos permite dois desvios de fluxo.

idade = int(input('Informe a sua idade: '))

if idade >= 18: # Caso a idade seja maior ou igual a 18, ele vai executar o blovo do print positivo.
    print('Maior de idade!!')

else: #Caso a idade seja menor que 18, ele irá executar o bloco do print negativo.
    print('Menor de idade!!')

# IF, ELIF & ELSE - Uma estrutura que permite mais de dois desvios de fluxo, Podendo ter várias condições.

opcao = int(input('Informe uma opção: [1] Sacar, [2] Depositar, [3] Consultar saldo: '))

if opcao == 1: #Primeira condição, caso a opção seja igual a 1, ele vai executar o bloco 'Saque realizado'
    print('Saque realizado!!')

elif opcao == 2: #Segunda condição, caso a opção seja igual a 2, ele vai executar o bloco 'Deposito realizado'
    print('Deposito realizado!!')

elif opcao == 3: #Terceira condição, caso a opção seja igual a 3, ele vai executar o bloco 'Seu saldo é de' 
    print('Seu saldo é de: ')

else: #Caso nenhuma das condições seja atendida, ele vai executar o bloco 'Opção inválida'
    print('Opção inválida!!')

# IF ANINHADO - Estrutura que permite fazer uma condição dentro de outra condição.

idade = int(input('Informe a sua idade: '))
tem_representante = True #Se estive com representante, ele vai ter acessso, caso não tenha, não entrará.

if idade >= 18: # Caso seja maior de idade, ele vai executar o bloco do 'Maior de idade!!'.
    print('Maior de idade!!')

else: #Caso ele seja menor de idade, ele vai verificar outra condição, se tem ou não representante.

    if tem_representante: # Se o representante for verdadeiro, o bloco 'Menor de idade, mas com representante!!' será executado.
        print('Menor de idade, mas com representante!!')

    else: # Caso contrario, ele executará o bloco 'Menor de idade, sem representante!!'
        print('Menor de idade, sem representante!!')



# IF TERNÁRIO - Estrutura que permite fazer uma condição em uma linha só, sem precisar de blocos.

idade = int(input('Informe a sua idade: '))

print('Maior de idade!!' if idade >= 18 else 'Menor de idade!!')
# Se a idade for maior ou igual a 18, ele vai imprimir 'Maior de idade!!', caso contrario, ele vai imprimir 'Menor de idade!!'