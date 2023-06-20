from datetime import date
x = int(input('Digite seu ano de nascimento: '))
y = date.today().year - x
if y <= 9:
    z = 'MIRIM'
elif y <= 14:
    z = 'INFANTIL'
elif y <= 19:
    z = 'JUNIOR'
elif y <= 25:
    z = 'SÊNIOR'
else:
    z = 'MASTER'
print('Atletas de {} anos encontram-se na categoria {}{}{}.'.format(y, '\033[1;34m', z, '\033[m'))
