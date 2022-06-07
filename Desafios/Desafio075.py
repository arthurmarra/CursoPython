contanove = 0
cont = 0
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

valores = [a, b, c, d]
qtd3 = 0

print(f'\nVocê digitou os valores: {valores}')
print('Os valores PARES digitados foram: ', end = '')
while cont < 4:
    if valores[cont]%2==0:
        n = valores[cont]
        print(f'{n} ', end = '')
    cont+=1

cont = 0
if 3 in valores:
    print(f'\nO valor 3 apareceu na posição: {valores.index(3)+1}')
else:
    print('\nO valor 3 não foi digitado!')

print(f'O valor 9 apareceu {valores.count(9)} vezes')
