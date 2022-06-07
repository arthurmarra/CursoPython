# Faça um programa que jogue PAR ou ÍMPAR com o computador. O jogo só será interrompido quando o jogador, PERDER,
# mostrando o total de vitórias que ele conquistou no final do jogo.

from random import randint

ganhou = True
total = 0
cont = 0

while ganhou:
    parim = str(input('Escolha -> PAR OU ÍMPAR: ')).strip().upper()[0]
    n = int(input('Agora escolha um número: '))
    rand = randint(0, 10)
    total = rand + n
    if parim in 'P' and total % 2 == 0:
        print(f'{rand} + {n} = {total} E este número é PAR! Você venceu!')
        cont += 1
    elif parim in 'P' and total % 2 == 1:
        print(f'{rand} + {n} = {total} E este número é ÍMPAR! Você perdeu!')
        ganhou = False
        print(f'GAME OVER! Você ganhou {cont} vezes!')
    elif parim in 'I' and total % 2 == 1:
        print(f'{rand} + {n} = {total} E este número é ÍMPAR! Você venceu!')
        cont += 1
    elif parim in 'I' and total % 2 == 0:
        print(f'{rand} + {n} = {total} E este número é PAR! Você perdeu!')
        print(f'GAME OVER! Você ganhou {cont} vezes!')
        ganhou = False

