objetos_precos = ('lapis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00, 'trasnferidor', 4.20,
                  'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.30, 'livro', 34.90)
print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
for objeto in objetos_precos:
    if int(objetos_precos.index(objeto)) % 2 == 0:
        print(f'{objeto.capitalize():.<30} R${objetos_precos[(objetos_precos.index(objeto)) + 1]:>7.2f}')
