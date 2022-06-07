numeros = []

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso..')
    else:
        print('Valor duplicado, tente outro valor')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

numeros.sort()
print(f'A lista em ordem crescente é: {numeros}')

