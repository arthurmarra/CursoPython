lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        print('Finalizando programa...')
        break
for i, v in enumerate(lista):
    if v %2 == 0 and v not in pares:
        pares.append(v)
    elif v %2 == 1 and v not in impares:
        impares.append(v)
lista.sort()
pares.sort()
impares.sort()
print(lista)
print(pares)
print(impares)
