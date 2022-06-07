# Crie um program que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre: A) Qual é o total gasto na compra. B) Quantos produtos custam mais de R$1000. C)Qual é o nome do
# produto mais barato.

totgasto = qtdprod  = menor = cont = 0
barato = ''

while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preço = float(input('Digite o valor do produto: '))
    cont += 1
    totgasto += preço
    if preço > 1000:
        qtdprod += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    resp = ' '
    while resp not in ('SN'):
        resp = str(input('Quer continuar comprando? (S/N)')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Total gasto na compra: {totgasto:.2f}\nQtd de produtos que custam mais de R$1000,00: {qtdprod}\nNome do produto mais barato: {barato}')