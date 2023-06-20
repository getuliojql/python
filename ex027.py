x = str(input('Digite seu nome completo: ')).strip()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}. \nSeu último nome é {}.'.format(x.split()[0], x[x.rfind(' ')+1:len(x)+1]))
