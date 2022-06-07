# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a
# digitar.

media = qtdnum = soma = maior = 0
perg = ''

executar = True

while executar:
    n = int(input('Digite um número: '))
    qtdnum += 1
    soma += n
    maior = n
    menor = maior
    perg = str(input('Deseja inserir outro valor? (S/N) ')).strip().upper()
    while perg in 'Ss':
        n = int(input('Digite um número: '))
        if maior < n:
            maior = n
        else:
            menor = n
        soma += n
        qtdnum += 1
        perg = str(input('Deseja inserir outro valor? (S/N) ')).strip().upper()
    else:
        executar = False

media = soma/ qtdnum

print('Média entre os números digitados: {}\nO maior número é: {}\nO menor número é : {}'.format(media, maior, menor))
