from time import sleep
from random import randint
x = randint(0, 5)
print('-----------JOGO DA ADIVINHAÇÃO-----------')
y = int(input('Em qual número você acha que eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if x == y:
    print('Você acertou! Eu pensei no número {}!'.format(y))
else:
    print('Você errou! Eu pensei no número {}...'.format(x))
