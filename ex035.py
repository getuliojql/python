x = float(input('Digite o comprimento da primeira reta: '))
y = float(input('Digite o comprimento da segunda reta : '))
z = float(input('Digite o comprimento da terceira reta: '))
if x < y + z and y < x + z and z < x + y:
        print('\nAs retas acima PODEM formar um triângulo!')
else:
    print('\nAs retas acima NÃO PODEM formar um triângulo!')
