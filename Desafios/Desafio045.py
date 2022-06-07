# Crie um programa que faça o computador jogar JOKENPO com você.
from random import choice

lista = ['PEDRA', 'PAPEL', 'TESOURA']

escolha = choice(lista)

e = str(input('Escolha entre PEDRA,PAPEL OU TESOURA: ')).strip().upper()

print('O computador escolheu: {}'.format(escolha))

if e == 'TESOURA' and escolha == 'PAPEL' or e == 'PEDRA' and escolha == 'TESOURA' or e == 'PAPEL' and escolha == 'PEDRA':
    print('VOCÊ GANHOU!!')
elif e == 'TESOURA' and escolha == 'TESOURA' or e == 'PAPEL' and escolha == 'PAPEL' or e == 'PEDRA' and escolha == 'PEDRA':
    print('EMPATE!!')
elif e == 'TESOURA' and escolha == 'PEDRA' or e == 'PAPEL' and escolha == 'TESOURA' or e == 'PEDRA' and escolha == 'PAPEL':
    print('VOCê PERDEU!!')

