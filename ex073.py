times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasgo da Gama', 'Chapecoense',
         'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport', 'EC Vitória', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Lista de times do Brasileirão: {times}\n')
print(f'Os 5 primeiros são {times[:5]}\n')
print(f'Os 4 últimos são {times[-4:]}\n')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
