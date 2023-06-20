x = str(input('Digite uma frase: ')).strip().upper()
y = x.split()
z = ''.join(y)
i = ''
for c in range(len(z) -1, -1, -1):
    i += z[c]
if i == z:
    print('A frase digita {}é{} um palíndromo!'.format('\033[32m', '\033[m'))
else:
    print('A frase digitada {}não é{} um palíndromo!'.format('\033[31m', '\033[m'))
