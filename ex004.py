x = input('Digite algo: ')
print('O tipo primitivo de "{}" é {} \n'.format(x, type(x)))
print('É composto apenas por espaços? {} \nÉ um número? {}'.format(x.isspace(), x.isnumeric()))
print('É alfabético? {} \nÉ alfanumérico? {}'.format(x.isalpha(), x.isalnum()))
print('Está apenas em maiúsculas? {} \nEstá apenas em minúsculas? {}'.format(x.isupper(), x.islower()))
print('Está capitalizada (primeira letra maiúscula)? {}'.format(x.istitle()))
