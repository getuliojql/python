x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
if x > y:
    print('O {}primeiro número{} é maior.'.format('\033[1;34m', '\033[m'))
elif x < y:
    print('O {}segundo número{} é maior.'.format('\033[1;34m', '\033[m'))
else:
    print('Os dois número são {}iguais{}.'.format('\033[1;35m', '\033[m'))
