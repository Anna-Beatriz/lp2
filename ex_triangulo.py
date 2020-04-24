class Triangulo:
    def __init__(self, a, b, c):
        self.lado_a = a
        self.lado_b = b
        self.lado_c = c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

    def maior_lado(self):
        if self.lado_a > self.lado_b and self.lado_a > self.lado_c:
            return self.lado_a
        elif self.lado_b > self.lado_a and self.lado_b > self.lado_c:
            return self.lado_b
        else:
            return self.lado_c


a = float(input('Digite o lado A do triângulo: '))
b = float(input('Digite o lado B do triângulo: '))
c = float(input('Digite o lado C do triângulo: '))

meu_objeto = Triangulo(a, b, c)
print('Perímetro: ', meu_objeto.calcular_perimetro())
print('Maior lado: ', meu_objeto.maior_lado())
