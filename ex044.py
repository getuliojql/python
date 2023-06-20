print('{}     {}{}{}{}     {}'.format('\033[7;30m', '\033[1;4;7;30m',
                                      'LOJAS CURSO EM VÍDEO', '\033[m', '\033[7;30m', '\033[m'))
x = float(input('Digite o preço das compras: R$'))
y = int(input('Qual a forma de pagamento? \nDigite [1] para selecionar à vista no dinheiro/cheque.'
              '\nDigite [2] para selecionar à vista no cartão. \nDigite [3] para selecionar 2x no cartão.'
              '\nDigite [4] para selecionar 3x ou mais no cartão. \nSua opção: '))
if y == 1:
    print('\nPor pagar com dinheiro/cheque, você ganhou um {}desconto{}'
          ' de 10%! Seu novo total é de R${:.2f}.'.format('\033[32m', '\033[m', x - x / 10))
elif y == 2:
    print('\nPor pagar à vista no cartão, você ganhou um {}desconto{}'
          ' de 5%! Seu novo total é de R${:.2f}!'.format('\033[32m', '\033[m', x - x / 20))
elif y == 3:
    print('\nSua compra será parcelada em 2x de R${:.2f} {}sem juros{}.'.format(x / 2, '\033[32m', '\033[m', x))
elif y == 4:
    z = int(input('Em quantas parcelas você deseja dividir? '))
    print('\nSua compra será parcelada em {}x de R${:.2f} {}com juros{}. Seu novo total '
          'é de R${:.2f}.'.format(z, (x + x / 5) / z, '\033[31m', '\033[m', x + x / 5))
else:
    print('Você digitou uma opção inválida. Tente novamente')
