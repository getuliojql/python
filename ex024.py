from time import sleep
x = str(input('Digite o nome de uma cidade: ')).strip().upper()
print('Analisando se essa cidade começa com a palavra "Santo"...')
sleep(1)
if x[:5] == 'SANTO':
    print('Sua cidade começa com a palavra "Santo"!')
else:
    print('Sua cidade não começa com a palavra "Santo"!')
'''x = str(input('Digite o nome de uma cidade: ')).strip().upper()
if x[:5] == 'SANTO':
    print('Sim, essa cidade começa com a palavra Santo.')
else:
    print('Não, essa cidade não começa com a palavra santo')'''