palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar','trabalhar')

for c in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[c]} temos', end = ' ')
    for letras in palavras[c]:
        if letras in 'aeiou':
            print(letras, end = ' ')