x = int(input('Digite a distância da viagem: '))
if x <= 200:
    print('A passagem custará R${:.2f}.'.format(x*0.5))
else:
    print('A passagem custará R${:.2f}.'.format(x*0.45))

#if SIMPLIFICADO ou OPERADOR TERNÁRIO#
#y = x * 0.5 if x <= 200 else x *0.45
#print('A passagem custará R${:.2f}'.format(y))
