from random import randint
numeros = list()

def sorteia(lista):
    cont = 0
    while cont<5:
        sort = randint(1, 10)
        lista.append(sort)
        cont +=1
    print(f'Sorteando 5 valores da lista: ', end='')
    for k in numeros:
        print(f'{k} ', end='')
    print('PRONTO!')
def somaPar(lista):
    soma = continha = 0
    for v in lista:
        if lista[continha]%2 == 0:
            soma+=v
        continha+=1
    print('Somando os valores pares de ', end='')
    for l in numeros:
        print(f'{l} ', end ='')
    print(f', temos {soma}')

sorteia(numeros)
somaPar(numeros)
