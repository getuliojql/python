from random import randint
x = randint(0, 10)
print(x)
y = x + 1
z = 0
print('{}--JOGO DA ADIVINHAÇÃO--{}'.format('\033[33m', '\033[m'))
while y != x:
    y = int(input('Digite seu palpite: '))
    z += 1
    if y != x:
        print('{}ERRADO{}'.format('\033[31m', '\033[m'))
print('{}ACERTOU{} na {}ª tentativa!'.format('\033[32m', '\033[m', z))
