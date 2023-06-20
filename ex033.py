x = int(input('Digite um número     : '))
y = int(input('Digite outro número  : '))
z = int(input('Digite mais um número: '))
print('--------------------------')
a = x
if y < x and y < z:
    a = y
if z < x and z < y:
    a = z
print('{} é o menor dos três números.'.format(a))
b = x
if y > x and y > z:
     b = y
if z > x and z > y:
    b = z
print('{} é o maior dos três números.'.format(b))
