a = 0
b = 0
d = ''
e = 0
for c in range(1, 5):
    print('----{}ª PESSOA----'.format(c))
    x = str(input('Nome : ')).strip()
    y = int(input('Idade: '))
    z = str(input('Sexo [M/F]: ')).strip()
    a += y / 4
    if z in 'Mm' and y > b:
        b = y
        d = x
    if z in 'Ff' and y < 20:
        e += 1
print('\n- A média de idade do grupo é de {} anos.'.format(a))
print('- O homem mais velho se chama {} e ele tem {} anos.'.format(d, b))
print('- Ao todo são {} mulheres com menos de 20 anos.'.format(e))
