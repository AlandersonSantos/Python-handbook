'''

Peça:

nome do produto
preço
quantidade

Calcule:

subtotal

Depois aplique:

10% de desconto

Mostre:

Produto:
Quantidade:
Subtotal:
Desconto:
Total:

'''

produto = input('Qual o produto: ')
preco = float(input('Qual o preço do produto: '))
quantidade = int(input('Qual a quantidade de produtos: '))



subtotal = preco * quantidade
desconto = subtotal * (10/100)
total = subtotal - desconto


print(f'''
 =============================     

      Lista de compras:

      Produto: {produto}
      Quantidade: {quantidade}
      Subtotal: R$ {subtotal}
      Desconto: R$ {desconto}
      Total: R$ {total}


=============================    
''')