class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self, canal):
        self.canal = canal


tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
for i in range(8):
    tv.aumentar_volume()
print('A tv está no canal:', tv.canal)  # imprime 5
print('A tv está no volume:', tv.volume)  # imprime 10
