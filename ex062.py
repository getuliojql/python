x = int(input('Informe o primeiro termo: '))
y = int(input('Informe a razão: '))
z = x
print('\n{}Os 10 primeiros termos da P.A. formada são:{} '.format('\033[32m', '\033[m'), end='')
while z < x + y * 10:
    print(z, end='➡')
    z += y
print('...')
a = 0
b = 0
c = 0
while c == 0:
    b = int(input('Informe quantos termos quer mostrar a mais: '))
    while b != 0:
        while a < b:
            print(z, end='➡')
            z += y
            a += 1
