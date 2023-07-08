palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'\nNa palavra {p.upper()} temos', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f' {letra}', end='')
