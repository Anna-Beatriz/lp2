class Cliente:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.telefone = None

    def alterar_nome(self, nome):
        self.nome = nome

    def alterar_idade(self, idade):
        self.idade = idade

    def alterar_telefone(self, telefone):
        self.telefone = telefone

    def exibir(self):
        print(cliente1.nome)
        print(cliente1.idade)
        print(cliente1.telefone)


cliente1 = Cliente()
cliente1.alterar_nome('João')
cliente1.alterar_idade('25')
cliente1.alterar_telefone(912345678)
cliente1.exibir()
