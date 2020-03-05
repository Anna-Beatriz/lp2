'''
Crie um dicionário (inicialmente vazio) para armazenar uma listagem de alunos. 
Nesse dicionário, a chave é o RA do aluno e o valor é o nome do aluno.
Considere que o RA de cada aluno deve ser composto por um número inteiro de 7 dígitos.
Crie uma função que recebe como parâmetros o dicionário, o RA e o nome de um aluno e insere esse aluno no dicionário.
Caso o RA não esteja no formato correto, deve ser gerada uma exceção do tipo ValueError
Caso o RA já exista no dicionário, deve ser gerada uma exceção do tipo TypeError
Crie uma função que recebe como parâmetro o dicionário e o RA de um aluno e retorna o nome desse aluno.
Caso o RA não exista no dicionário, a função deve gerar uma exceção do tipo KeyError
'''

alunos = {}




try:
    def aluno(alunos, nome, ra):
    if not nome in alunos:
        alunos[nome] = ra
    return alunos  

    nome = input('Nome:')
    ra = int(input('RA:'))

    if nome in alunos:
        raise TypeError
    if ra < 1000000 or ra > 10000000:
        raise ValueError
except ValueError:
        print('O RA não está correto!')
except TypeError:
        print('O RA já existe!')
else:
    alunos[ra] = nome

def busca_aluno():
    try:
        if ra not in alunos:
            raise KeyError
        except KeyError:
            print('RA inexistente!')
        else:
            alunos[ra]

aluno(alunos, nome, ra)
print(alunos)

'''
Solução do professor:
def adicionar_aluno(alunos, ra, nome):
    try:
        if ra in alunos:
            raise TypeError
        if ra < 1000000 or ra > 10000000:
            raise ValueError
    except TypeError:
        print('RA já existente')
    except ValueError:
        print('RA inválido')
    else:
        alunos[ra] = nome


def busca_aluno(alunos, ra):
    try:
        if ra not in alunos:
            raise KeyError
    except KeyError:
        print('RA Inexistente')
    else:
        return alunos[ra]


alunos = {}
adicionar_aluno(alunos, 1912541, 'Paulo')
adicionar_aluno(alunos, 1821125, 'João')
adicionar_aluno(alunos, 1912548, 'Ana')
print(busca_aluno(alunos, 1912541))
print(busca_aluno(alunos, 9999999))
'''