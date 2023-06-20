from time import sleep
x = str(input('Digite seu nome completo: ')).strip().upper()
print('Analisando...')
sleep(1)
print('Seu nome tem Silva? {}'.format('SILVA' in x))
