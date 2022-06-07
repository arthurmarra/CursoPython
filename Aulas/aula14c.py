n = 1
pares = 0
impares = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n !=0:
        if n % 2 == 0:
            pares +=1
        elif n % 2 == 1:
            impares +=1

print('Qtd pares: {}'.format(pares))
print('Qtd impares: {}'.format(impares))