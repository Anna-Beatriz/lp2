# Andrea Santos
# Anna Beatriz Moraes Santos
# Everton de Souza Siqueira


def salario(dic, nome):
    cargo = dic[nome][2]
    salario = dic[nome][1]

    if cargo == 'DESENVOLVEDOR':
        if salario >= 2000:
            desconto = (salario * 20) / 100
        else:
            desconto = (salario * 10) / 100
        salario -= desconto
        return salario

    elif cargo == 'ANALISTA':
        if salario >= 3000:
            desconto = (salario * 25) / 100
        else:
            desconto = (salario * 15) / 100
        salario -= desconto
        return salario

    elif cargo == 'GERENTE':
        if salario >= 5000:
            desconto = (salario * 30) / 100
        else:
            desconto = (salario * 20) / 100
        salario -= desconto
        return salario

    else:
        raise TypeError
