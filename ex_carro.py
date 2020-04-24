class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.quantidade_combustivel = 0

    def adicionar_combustivel(self, combustivel):
        self.quantidade_combustivel += combustivel

    def obter_combustivel(self):
        return self.quantidade_combustivel

    def andar(self, km):
        self.consumo = km / self.consumo
        self.quantidade_combustivel -= self.consumo


fusca = Carro(15)  # 15 quilômetros por litro de combustível
fusca.adicionar_combustivel(20)  # abastece com 20 litros de combustível
fusca.andar(100)  # anda 100 quilômetros.
print('{:.2f}'.format(fusca.obter_combustivel()))  # imprime o combustível que resta no tanque
