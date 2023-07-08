numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                   'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
controle = 0
while controle == 0:
    numero_novo = int(input('Digite um número entre 0 e 20: '))
    for chave, numero in enumerate(numeros_extenso):
        if numero_novo < 0 or numero_novo > 20:
            print('Tente novamente. ', end='')
            numero_novo = int(input('Digite um número entre 0 e 20: '))
        else:
            if chave == numero_novo:
                print(f'Você digitou o número {numero}')
    continuar = str(input('Você quer continuar [S/N]? '))
    if continuar == 'N':
        controle = 1


#SOLUÇÃO DO GUANABARA
'''controle = 0
while controle == 0:
    numero_novo = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero_novo <= 20:
        controle = 1
    else:
        print('Tente novamente. ', end='')
print(f'Você digitou o número {numeros_extenso[numero_novo]}')'''
