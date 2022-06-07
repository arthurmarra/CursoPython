# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1=120



n = int(input('Digite um número: '))
cont = n
fat = 1
while cont > 0:
    fat *= cont
    cont -= 1

print('O fatorial do número digitado é {}.'.format(fat))

