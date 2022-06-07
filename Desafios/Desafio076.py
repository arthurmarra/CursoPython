prod = ('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.90,
        'Estojo', 25,
        'Transferidor', 4.20,)


print('-'*40)
print(f'{"Lista de preços":^40}')
print('-'*40)
for pos in range(0, len(prod)):
    if pos % 2 == 0:
        print(f'{prod[pos]:.<30}', end= '')
    else:
        print(f'R${prod[pos]:>7.2f}')