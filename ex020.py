from random import shuffle
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
e = [a, b, c, d]
shuffle(e)
print('A ordem de apresentação será: {}.'.format(e))
