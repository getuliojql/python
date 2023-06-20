from math import hypot
x = float(input('Quanto mede o cateto oposto: '))
y = float(input('Quanto mede o cateto adjacente: '))
print('A hipotenusa desse triângulo mede {:.2f}.'.format(hypot(x, y)))
