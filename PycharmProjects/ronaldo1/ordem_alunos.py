from random import shuffle
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1,aluno2,aluno3,aluno4]
ordem = shuffle(lista)#shuffle significa embaralhar
print('A ordem de apresentação será: {}'.format(lista))
