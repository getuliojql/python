valores = []
maior = menor = 0

for chave in range(5):
    valores.append(input(f'Digite um valor para a posição {chave}: '))

    if chave == 0:
        maior = menor = valores[chave]
    else:
        if valores[chave] > maior:
            maior = valores[chave]
        elif valores[chave] < menor:
            menor = valores[chave]
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for idx, valor in enumerate(valores):
    if valor == maior:
        print(f'{idx}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')
for idx, valor in enumerate(valores):
    if valor == menor:
        print(f'{idx}... ', end='')
