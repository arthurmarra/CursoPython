lista = []

maior = menor = 0

for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = lista[c]
        menor = maior
    else:
        if maior < lista[c]:
            maior = lista[c]
        if menor > lista[c]:
            menor = lista[c]

print('Lista digitada: ', end = '')
for n in lista:
    print(n, end = ' ')

print(f'\nO maior valor digitado foi {maior} nas posições ', end = '')
for i, v in enumerate(lista):
    if lista[i] == maior:
        print(f"{i+1}", end = '...')
print(f'\nO menor valor digitado foi {menor} nas posições ', end = '')
for i1, v1 in enumerate(lista):
    if lista[i1] == menor:
        print(f"{i1+1}", end = '...')

#print(f'\nO maior valor digitado foi {maior} e sua posição na lista é {lista.index(maior)+1}')
#print(f'O menor valor digitado foi {menor} e sua posição na lista é {lista.index(menor)+1}')

