lista = []

qtdnum = 0
while True:
    n = int(input('Digite um número: '))
    qtdnum+=1
    lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        print('Finalizando programa...')
        break

lista.sort(reverse=True)

print(f'Existem {qtdnum} números nesta lista!')
print(f'Lista em ordem decrescente: {lista}')
if lista.count(5) == 0:
    print('Valor 5 não existe na lista!')
if lista.count(5)>= 1:
    print('Valor 5 encontrado!')