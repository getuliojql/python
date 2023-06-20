x = float(input('Digite o valor da casa: R$'))
y = float(input('Digite o salário do comprador: R$'))
z = int(input('Digite em quantos anos a casa vai ser paga: '))
if x / z / 12 > y / 10 * 3:
    print('O empréstimo foi {}NEGADO{}. A prestação mensal seria de R${:.2f}. \nA prestação mensal não pode exceder '
          '30% do salário do comprador.'.format('\033[1;31m', '\033[m', x / (z *12)))
else:
    print('O empréstimo foi {}APROVADO{}. \nA prestação mensal será '
          'de R${:.2f}.'.format('\033[1;32m', '\033[m', x / (z * 12)))
