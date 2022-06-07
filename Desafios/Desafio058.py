# Melhore o jogo do DESAFIO028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários pra vencer.

from random import randint

num = cont = palpite = 0
num = randint(0, 11)

while num != palpite:
    num = randint(0, 11)
    palpite = int(input('Digite um número: '))
    if num != palpite:
        print('O computador pensou em {} e você em {}. Você perdeu!'.format(num,palpite))
        cont += 1

print('O computador pensou em {} e você em {}. Você ganhou!\nForam necessárias {} tentativas para vencer!'.format(num, palpite, cont))
