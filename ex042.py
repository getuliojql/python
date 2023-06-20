x = float(input('Digite o comprimento da primeira reta: '))
y = float(input('Digite o comprimento da segunda reta : '))
z = float(input('Digite o comprimento da terceira reta: '))
if x < y + z and y < x + z and z < x + y:
    print('\nAs retas acima {}PODEM{} formar um triângulo!'.format('\033[1;32m', '\033[m'))
    if x == y == z:
        print('O triângulo formado seria EQUILÁTERO.')
    elif x == y != z or x == z != y or y == z != x:
        print('O triângulo formado seria ISÓSCELES.')
    else:
        print('O triângulo formado seria ESCALENO.')
else:
    print('\nAs retas acima {}NÃO PODEM{} formar um triângulo!'.format('\033[1;31m', '\033[m'))
