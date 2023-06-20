s = 0
y = 0
for c in range(0, 6):
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        s += x
        y += 1
print('\nA soma dos {} números pares digitados é {}{}{}.'.format(y, '\033[32m', s, '\033[m'))
