# Andrea Santos
# Anna Beatriz Moraes Santos
# Everton de Souza Siqueira


import ac_salario

try:
    tst1 = ac_salario.salario(
        {'maria': ['maria@email.com', 5000.00, 'DESENVOLVEDOR']},
        'maria'
        )
    assert tst1 == 4000
    print('Teste 1 correto!')
except AssertionError:
    print('Teste 1 com ERRO!')
    print('Retorno: ', tst1)
    print('Esperado: ', 4000)


try:
    tst2 = ac_salario.salario(
        {'maria': ['maria@email.com', 1500.00, 'DESENVOLVEDOR']},
        'maria'
        )
    assert tst2 == 1350
    print('Teste 2 correto!')
except AssertionError:
    print('Teste 2 com ERRO!')
    print('Retorno: ', tst2)
    print('Esperado: ', 1350)


try:
    tst3 = ac_salario.salario(
        {'joana': ['joana@email.com', 7000.00, 'ANALISTA']},
        'joana'
        )
    assert tst3 == 5250
    print('Teste 3 correto!')
except AssertionError:
    print('Teste 3 com ERRO!')
    print('Retorno: ', tst3)
    print('Esperado: ', 5250)


try:
    tst4 = ac_salario.salario(
        {'joana': ['joana@email.com', 2500.00, 'ANALISTA']},
        'joana'
        )
    assert tst4 == 2125
    print('Teste 4 correto!')
except AssertionError:
    print('Teste 4 com ERRO!')
    print('Retorno: ', tst4)
    print('Esperado: ', 2125)


try:
    tst5 = ac_salario.salario(
        {'joao': ['joao@email.com', 10000.00, 'GERENTE']},
        'joao'
        )
    assert tst5 == 7000
    print('Teste 5 correto!')
except AssertionError:
    print('Teste 5 com ERRO!')
    print('Retorno: ', tst5)
    print('Esperado: ', 7000)


try:
    tst6 = ac_salario.salario(
        {'joao': ['joao@email.com', 4500.00, 'GERENTE']},
        'joao'
        )
    assert tst6 == 3600
    print('Teste 6 correto!')
except AssertionError:
    print('Teste 6 com ERRO!')
    print('Retorno: ', tst6)
    print('Esperado: ', 3600)
