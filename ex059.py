from time import sleep
x = int(input('Digite o 1° valor: '))
y = int(input('Digite o 2º valor: '))
z = 0
while z != 5:
    z = int(input('\nMENU:\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair\nSua opção: '))
    if z == 1:
        print('A soma entre {} e {} é igual a {}.'.format(x, y, x + y))
        z = 0
    if z == 2:
        print('O produto de {} e {} é igual a {}.'.format(x, y, x * y))
        z = 0
    if z == 3:
        if x > y:
            print('O maior dos dois números é o {}.'.format(x))
        elif x < y:
            print('O maior dos dois números é o {}.'.format(y))
        else:
            print('Os números são iguais.')
        z = 0
    if z == 4:
        x = int(input('\nDigite o 1° valor: '))
        y = int(input('Digite o 2° valor: '))
        z = 0
    sleep(1)
