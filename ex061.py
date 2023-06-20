x = int(input('Informe o primeiro termo: '))
y = int(input('Informe a razão: '))
z = x
print('\n{}Os 10 primeiros termos da P.A. formada são:{} '.format('\033[32m', '\033[m'), end='')
while z < x + y * 10:
    print(z, end='➡')
    z += y
print('...')
