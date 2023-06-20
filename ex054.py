from datetime import date
y = 0
z = 0
for c in range(1, 8):
    x = int(input('Digite o ano no qual a {}ª pessoa nasceu: '.format(c)))
    if date.today().year - x < 18:
        y = y + 1
    elif date.today().year >= 18:
        z = z + 1
print('\n{}****LEVANDO EM CONSIDERÇÃO A MAIORIDADE BRASILEIRA****{}'.format('\033[31m', '\033[m'))
print('Das 7 pessoas, {} são menores de idade e {} são maiores.'.format(y, z))
