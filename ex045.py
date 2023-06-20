from time import sleep
from random import randint

print('-----PEDRA, PAPEL E TESOURA-----')
x = int(input('Suas opções: \n[0] - Pedra \n[1] - Papel \n[2] - Tesoura \nSua jogada: '))
y = randint(0, 2)
if x > 2:
    print('Opção inválida. Tente novamente.')
else:
    print('{}JO{}'.format('\033[34m', '\033[m'))
    sleep(1)
    print('{}KEN{}'.format('\033[34m', '\033[m'))
    sleep(1)
    print('{}PÔ!{}'.format('\033[34m', '\033[m'))
    print('')
    if x == 0:
        if y == 0:
            print('{}EMPATOU!{} Nós dois escolhemos pedra.'.format('\033[33m', '\033[m'))
        elif y == 1:
            print('{}EU GANHEI!{} Você escolheu pedra e eu escolhi papel.'.format('\033[31m', '\033[m'))
        else:
            print('{}VOCÊ GANHOU!{} Você escolheu pedra e eu escolhi tesoura.'.format('\033[32m', '\033[m'))
    elif x == 1:
        if y == 0:
            print('{}VOCÊ GANHOU!{} Você escolheu papel e eu escolhi pedra.'.format('\033[32m', '\033[m'))
        elif y == 1:
            print('{}EMPATOU!{} Nós dois escolhemos papel.'.format('\033[33m', '\033[m'))
        else:
            print('{}EU GANHEI!{} Você escolheu papel e eu escolhi tesoura.'.format('\033[31m', '\033[m'))
    elif x == 2:
        if y == 0:
            print('{}EU GANHEI!{} Você tesoura e eu escolhi pedra.'.format('\033[31m', '\033[m'))
        elif y == 1:
            print('{}VOCÊ GANHOU!{} Você escolheu tesoura e eu escolhi papel.'.format('\033[32m', '\033[m'))
        else:
            print('{}EMPATOU!{} Nós dois escolhemos tesoura.'.format('\033[33m', '\033[m'))
