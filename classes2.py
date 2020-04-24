class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def exibir_dados(self):
        print('Título: ', self.titulo)
        print('Autor: ', self.autor)
        print('Preço: ', self.preco)


meu_livro = Livro('Harry Potter', 'J. K. Rowling', 20)
meu_livro.exibir_dados()

meu_livro.preco = 19.0
meu_livro.exibir_dados()

print('O autor do livro é: ', meu_livro.autor)

outro_livro = Livro('Senhor dos Anéis', '', 30)
outro_livro.exibir_dados()
