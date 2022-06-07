# Escreva um programa que faça o computador "pensar" em um número inteiro entra 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever se o usuáro ganhou ou perdeu.

from random import randint

num = randint(1,5)


r = int(input('Digite um número de 0 a 5: '))

if r == num:
    print('O computador pensou em {}'.format(num))
    print('Você venceu!!')
else:
    print('O computador pensou em {}'.format(num))
    print('Você perdeu!!')