continua = True

while continua:
    try:
        x = int(input('Primeiro valor:'))
        y = int(input('Segundo valor:'))
        z = x / y
        print('O resultado da divisão é:', z)
    except ValueError:
        print('Tipo inválido!')
    except ZeroDivisionError:
        print('Zero não é divisível!')
    else:
        continua = False