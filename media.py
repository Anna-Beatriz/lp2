def calcular_media(notas, nome):
    if nome in notas:
        lista = notas[nome]
        media = sum(lista)/len(lista)
        return media
    else:
        return 0


notas = {}
for i in range(3):
    nome = input('Nome:')
    nota1 = float(input('Primeira Nota:'))
    nota2 = float(input('Segunda Nota:'))
    notas[nome] = [nota1, nota2]
print(notas)

nome = input('Digite o nome de um aluno: ')
media = calcular_media(notas, nome)
print('Média do aluno:', media)
