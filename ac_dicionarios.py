import ac01

agenda = {'Pedro': ['11-94444-8888', '11-98888-0000'],
          'Ana': ['11-99999-4567'],
          'José': ['11-95555-5555', '11-97777-0000', '11-95555-4444']}

nome = input('Nome: ')
telefone = input('Telefone: ')

agenda_add = ac01.incluir_pessoa(agenda, nome, telefone)
print(agenda_add)
agenda_excluir = ac01.excluir_pessoa(agenda, nome)
print(agenda)
agenda_pesquisa = ac01.pesquisar_pessoa(agenda, nome)
print(agenda_pesquisa)
agenda_incluir_tel = ac01.incluir_telefone(agenda, nome, telefone)
print(agenda)
agenda_excluir_tel = ac01.excluir_telefone(agenda, nome, telefone)
print(agenda)
