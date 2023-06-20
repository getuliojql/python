x = int(input('Digite um número para ver sua tabuada: '))
print('\n{}TABUADA DO {}{}'.format('\033[31m', x, '\033[m'))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(x, c, x * c))
