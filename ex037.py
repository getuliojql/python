x = int(input('Digite um número inteiro: '))
y = int(input('Escolha uma das bases para conversão: \n[1] Binário \n[2] Octal \n[3] Hexadecimal \nSua opção: '))
if y == 1:
    print('{} em {}BINÁRIO{} é igual a {}.'.format(x, '\033[1;34m', '\033[m', bin(x).replace('0b', '')))
elif y == 2:
    print('{} em {}OCTAL{} é igual a {}.'.format(x, '\033[1;34m', '\033[m', oct(x).replace('0o', '')))
elif y == 3:
    print('{} em {}HEXADECIMAL{} é igual a {}.'.format(x, '\033[1;34m', '\033[m', hex(x).replace('0x', '')))
else:
    print('Você digitou uma opção inválida. Tente novamente.')
