from time import sleep
print('{}CONTAGEM PARA O ANO NOVO!{}'.format('\033[32m', '\033[m'))
sleep(1)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\n{}FELIZ ANO NOVO!{}'.format('\033[31m', '\033[m'))
