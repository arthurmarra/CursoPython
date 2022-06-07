# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitador e qual foi a soma entre eles.

qtdnum = soma = 0

n = int(input('Digite um número: '))
while n != 999:
    soma += n
    qtdnum += 1
    n = int(input('Digite um número: '))
print('A soma de todos os {} números digitados foi de: {} '.format(qtdnum, soma))