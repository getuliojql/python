y = 0
z = 0
for c in range(1, 6):
    x = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        y = x
        z = x
    else:
        if x < y:
            y = x
        if x > z:
            z = x
print('\nO menor peso registrado foi {}kg e o maior foi {}kg.'.format(y, z))
