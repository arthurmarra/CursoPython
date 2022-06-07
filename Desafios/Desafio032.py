# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

a = int(input('Digite o ano que quer verificar: '))

if a % 4 == 0:
    print('É BISSEXTO!')
else:
    print('NÃO É BISSEXTO!')