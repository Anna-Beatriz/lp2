class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_tiulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero


filmes = []
for filme in range(3):
    titulo = input('Título: ')
    genero = input('Gênero: ')
    filme = Filme(titulo, genero)
    filmes.append(filme)

for filme in filmes:
    print('Título: ', filme.get_titulo()
          + ', ' + 'gênero: ', filme.get_genero())
