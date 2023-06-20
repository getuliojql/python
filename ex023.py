x = int(input('Digite um número: '))
print('Milhares: {} \nCentenas: {} \nDezenas : {} \nUnidades: {}'.format(x//1000%10, x//100%10, x//10%10, x//1%10))
