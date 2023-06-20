x = float(input('Digite seu peso: '))
y = float(input('Digite sua altura: '))
z = x / (y**2)
print('\nSeu IMC é de {:.1f}.'.format(z))
if z < 18.5:
    print('Você está {}abaixo do peso{}.'.format('\033[33m', '\033[m'))
elif z < 25:
    print('Você está com o {}peso ideal{}.'.format('\033[32m', '\033[m'))
elif z < 30:
    print('Você está em {}sobrepeso{}.'.format('\033[33m', '\033[m'))
elif z < 40:
    print('Você está {}obeso{}.'.format('\033[31m', '\033[m'))
else:
    print('Você tem {}obesidade mórbida{}.'.format('\033[1;31m', '\033[m'))
