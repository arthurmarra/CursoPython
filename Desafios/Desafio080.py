numeros = []
maior = 0
for n in range(0,5):
    p = int(input('Digite um valor: '))
    if n ==0 or p > numeros[-1]:
        numeros.append(p)
        print('Adicionado no final da lista.')
    else:
        c=0
        while c < len(numeros):
            if p<= numeros[c]:
                numeros.insert(c, p)
                print(f'Número adicionado na posição {c} da lista.')
                break
            c+=1

print(numeros)