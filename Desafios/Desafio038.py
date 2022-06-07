# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior, - O segundo valor é maior ou - Não existe valor maior, os dois são iguais!

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

maior = n1

if n2 > n1:
    print('O segundo valor é maior!')
elif n2 == n1:
    print('Os dois valores são iguais!')
else:
    print('O primeiro valor é maior!')