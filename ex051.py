x = int(input('Informe o primeiro termo: '))
y = int(input('Informe a razão: '))
print('\n{}Os 10 primeiros termos da P.A. formada são: {}'.format('\033[32m', '\033[m',), end='')
for c in range(x, x + 10 * y, y):
    print(c, end='➡')
print('...')
