# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa
# o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual o valor da casa a comprar? '))
sal = float(input('Qual salário do comprador da casa? '))
ano = int(input('Em quantos anos vai pagar? '))

qtdmeses = ano * 12

valorf= valor/qtdmeses

print('Valor da prestação: R${:.0f},00'.format(valorf))

if valorf > sal * 0.30:
    print('Empréstimo negado!')
else:
    print('Seu empréstimo pode ser feito')