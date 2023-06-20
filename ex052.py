x = int(input('Digite um número: '))
y = 0
for c in range(2, x):
    if x % c == 0:
        y = 1
if x == 0 or x == 1:
    print('O número informado {}não é{} um número primo!'.format('\033[31m', '\033[m'))
elif y == 1:
    print('O número informado {}não é{} um número primo!'.format('\033[31m', '\033[m'))
elif y == 0:
    print('O número informado {}é{} um número primo!'.format('\033[32m', '\033[m'))
