s = 0
y = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        s += c
        y += 1
print('A soma dos {} números ímpares múltiplos de 3 entre 1 e 500 é igual a {}{}{}.'.format(y, '\033[32m', s, '\033[m'))
