# Crie um programa que leia dois valores e mostre um menu na tela:
# 1) Somar 2) Multiplicar 3) Maior 4) Novos números 5) Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
soma = mult = op = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
maior = n1


while op != 5:
    print('=' * 20)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior número')
    print('[4] Novos números')
    print('[5] Sair do programa')
    print('=' * 20)
    op = int(input('Digite a operação desejada: '))
    if op == 1:
        soma = n1+n2
        print('Valor da soma: {}'.format(soma))
    elif op == 2:
        mult = n1 * n2
        print('Valor da multiplicação: {}'.format(mult))
    elif op == 3:
        if n2 > n1:
            maior = n2
            print('O maior número é: {}'.format(maior))
    elif op == 4:
        n1 = int(input('Digite um novo número para n1: '))
        n2 = int(input('Digite um novo número para n2: '))
        print('Novos valores: n1 = {} n2 = {}'.format(n1, n2))
    elif op == 5:
        print('Fechando o programa. Até mais...')
    sleep(2)