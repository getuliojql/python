x = int(input('Digite um número: '))
y = x - 1
z = x
while y > 0:
    if y + 1 == x:
        print('{}! = {}'.format(x, x,),end='')
    print(' x', y, end='')
    z = z * y
    y -= 1
print(' = {}{}{}'.format('\033[32m', z, '\033[m'))
