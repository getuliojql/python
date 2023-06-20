x = float(input('Digite a distância em metros: '))
print('Uma distância de {} metros corresponde a: \n->{}mm \n->{}cm \n->{}dm'.format(x, x*1000, x*100, x*10))
print('->{}dam \n->{}hm \n->{}km'.format(x/10, x/100, x/1000))
