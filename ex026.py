x = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" aparece {} vezes nessa frase.'.format(x.count('a')))
print('A primeira letra "A" aparece na {}ª posição.'.format(x.find('a')+1))
print('A última letra "A" aparece na {}ª posição.'.format(x.rfind('a')+1))
