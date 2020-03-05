# Atividade Contínua 01
# Aluno 01: Anna Beatriz Moraes Santos
# Aluno 02: Everton de Souza Siqueira


def incluir_pessoa(agenda, nome, telefone):
    if nome not in agenda:
        agenda[nome] = telefone
    return agenda


def excluir_pessoa(agenda, nome):
    if nome in agenda:
        agenda.pop(nome)
    return agenda


def pesquisar_pessoa(agenda, nome):
    if nome in agenda:
        return agenda[nome]


def incluir_telefone(agenda, nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    return agenda


def excluir_telefone(agenda, nome, telefone):
    if nome in agenda:
        agenda[nome].remove(telefone)
    return agenda
