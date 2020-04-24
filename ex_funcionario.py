class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        self.salario = self.salario + (self.salario * percentual / 100)
        return self.salario


nome = input('Nome do funcionário: ')
salario = float(input('Salário: '))
funcionario1 = Funcionario(nome, salario)

percentual = float(input('Percentual de aumento: '))
funcionario1.aumentar_salario(percentual)
print('Funcionário: ', funcionario1.nome)
print('Salário atualizado: ', funcionario1.salario)
