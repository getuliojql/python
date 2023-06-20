from datetime import date
x = int(input('Que ano quer saber se é bissexto? Digite 0 para analisar o ano atual: '))
if x == 0:
    x = date.today().year
if x % 4 > 0 and x % 100 != 0 or x % 400 == 0:
    print('{} não é um ano bissexto!'.format(x))
else:
    print('{} é um ano bissexto!'.format(x))
