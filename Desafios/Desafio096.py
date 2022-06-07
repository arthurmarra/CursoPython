def área(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a:.1f}m²')


largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

área(largura, comprimento)


