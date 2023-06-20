x = float(input('Qual a velocidade do carro? '))
if x > 80:
    print('Você foi multado em R${:.2f}! \nO limite de velocidade da rodovia é ''de 80km/h.'.format((x-80)*7))
print('Dirija com segurança!')