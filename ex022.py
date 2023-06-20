from time import sleep
x = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
sleep(1)
print('Seu nome em maiúsculas é: {}. \nSeu nome em minúsculas é: {}.'.format(x.upper(), x.lower()))
print('Seu nome tem {} letras.'.format(len(x.replace(' ', ''))))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(x.split()[0], len(x.split()[0])))
