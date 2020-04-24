class Livro:
    def __init__(self):
        self.titulo = None
        self.autor = None
        self.preco = None

    def exibir_dados(self):
        print('Título: ', self.titulo)
        print('Autor: ', self.autor)
        print('Preço: ', self.preco)


meu_livro = Livro()
meu_livro.titulo = 'Harry Potter'
meu_livro.autor = 'J. K. Rowling'
meu_livro.preco = 20.0

meu_livro.exibir_dados()

meu_livro.preco = 19.0

meu_livro.exibir_dados()

print('O autor do livro é: ', meu_livro.autor)

outro_livro = Livro()
outro_livro.titulo = 'Senhor dos Anéis'
outro_livro.preco = 30.0

outro_livro.exibir_dados()
