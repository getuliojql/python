x = float(input('Digite o salário do funcionário: R$'))
if x > 1250:
    print('Tal funcionário, que ganhava R${:.2f}, passaria a ganhar R${:.2f}.'.format(x, x+x/10))
else:
    print('Tal funcionário, que ganhava R${:.2f}, passaria a ganhar R${:.2f}.'.format(x, x+x/100*15))
