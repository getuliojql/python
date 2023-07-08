#SOLUÇÃO DO GUANABARA
numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {(numeros.index(3)) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')

#É POSSÍVEL LER VALORES DENTRO DE UMA TUPLA!
"""primeiro = int(input('Digite um número: '))
segundo = int(input('Digite outro número: '))
terceiro = int(input('Digite mais um número: '))
quarto = int(input('Digite o último número: '))

noves = 0
controle_tres = 0
pares = ()

numeros = (primeiro, segundo, terceiro, quarto)
print(f'Você digitou os valores {numeros}')

for e, n in enumerate(numeros):
    if n == 9:
        noves += 1
    elif n == 3 and controle_tres == 0:
        tres = e
        controle_tres = 1
print(f'O valor 9 apareceu {noves} vezes.')
print(f'O valor 3 apareceu na {(tres) + 1}ª posição.')
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')"""
