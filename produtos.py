produtos = {}

for i in range(5):
    nome = input('Produto:')
    preco = float(input('Preço:'))
    produtos[nome] = preco

'''
produtos['camiseta'] = 45.0
produtos['calça'] = 99.00
produtos['meia'] = 20.00
produtos['tênis'] = 190.00
produtos['camisa polo'] = 45.0
'''
print(produtos)

for k in produtos:
    if produtos[k] > 50.00:
        print(k, produtos[k])
