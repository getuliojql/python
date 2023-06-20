x = float(input('Digite a primeira nota: '))
y = float(input('Digite a segunda nota: '))
z = (x + y) / 2
if z < 5:
    print('Você foi {}REPROVADO{}.'.format('\033[1;31m', '\033[m'))
elif 5 <= z < 7:
    print('Você ficou de {}RECUPERAÇÃO{}.'.format('\033[1;33m', '\033[m'))
else:
    print('Você foi {}APROVADO{}.'.format('\033[1;32m', '\033[m'))
print('Sua média foi {:.1f}.'.format(z))
