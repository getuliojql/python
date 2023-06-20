from time import sleep
from datetime import date
i = int(input('-----Qual seu sexo?----- \nDigite [1] para masculino. \nDigite [2] para feminino. '
              '\nSua opção: '))
if i == 1:
    x = int(input('Digite seu ano de nascimento: '))
    y = date.today().year - x
    print('PROCESSANDO...')
    sleep(2)
    if y < 18:
        print('{}Você ainda vai se alistar ao serviço militar em {} ano(s).{}'.format('\033[1;32m', 18 - y, '\033[m'))
    elif y == 18:
        print('{}VOCÊ DEVE SE ALISTAR AO SERVIÇO MILITAR ESSE ANO!{}'.format('\033[1;31m', '\033[m'))
    else:
        print('{}Você deve ter se alistado ao serviço militar há {} ano(s){}.'.format('\033[1;32m', y - 18, '\033[m'))
elif i == 2:
    print('Você é do sexo feminino. Mulheres não passam pelo alistamento militar obrigatório. Tenha um bom dia.')
else:
    print('Opção inválida. Tente novamente.')
