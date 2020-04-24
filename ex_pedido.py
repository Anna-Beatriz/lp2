class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, prod):
        self.produtos.append(prod)

    def calcular_valor(self):
        soma = 0
        for prod in self.produtos:
            prod.preco *= prod.quantidade
            soma += prod.preco
        return soma


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é:', meu_pedido.calcular_valor())  # imprime 20.90
