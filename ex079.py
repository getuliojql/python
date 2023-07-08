numeros = []
controle = 0

while controle == 0:
    novo_numero = (int(input('Digite um valor: ')))
    if novo_numero in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(novo_numero)
        print('Valor adicionado com sucesso...')

    sair = str(input('Quer continuar [S/N]? '))
    if sair.upper() == 'N':
        controle = 1

print(f'Você digitou os valores {sorted(numeros)}')