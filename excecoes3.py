'''
Crie uma lista, inicialmente vazia, para armazenar uma listagem de nomes.
Criar uma função para inserir um nome na lista
Criar uma função que recebe como parâmetro a lista e uma posição (índice) dessa lista e retornar o nome que está nessa posição. 
Essa função deve gerar e tratar uma exceção do tipo IndexError caso o índice não exista na lista.
'''

def inserir_nome(nome):
    nomes.append(nome)
    return nomes

def posicao_lista(nomes, posicao):
    try:
        return nomes[posicao]
    except IndexError:
        print('Índice inexistente')
       
nomes = []

nome = input('Nome: ')
posicao = int(input('Posição: '))

inserir_nome(nome)
print(nomes)
posicao_lista(nomes, posicao)

'''
#Solução do professor:
inserir_nome(nomes, 'João')
inserir_nome(nomes, 'Maria')
print(posicao_lista(nomes, 0))
print(posicao_lista(nomes, 5))
'''