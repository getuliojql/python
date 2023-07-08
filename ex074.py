#SOLUÇÃO DO GUANABARA
from random import randint

valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for v in valores:
    print(v, end=' ')
print(f'\nO menor valor sorteado foi {min(valores)}')
print(f'O maior valor sorteado foi {max(valores)}')

#ESQUECI DE USAR TUPLAS
'''from random import randint
valores = ()
menor = maior = 0
print('Os valores sorteados foram: ', end='')
for i in range(0, 5):
    novo_valor = randint(0, 10)
    print(novo_valor, end=' ')
    if i == 0:
        menor = novo_valor
        maior = novo_valor
    else:
        if novo_valor < menor:
            menor = novo_valor
        elif novo_valor > maior:
            maior = novo_valor
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')'''
