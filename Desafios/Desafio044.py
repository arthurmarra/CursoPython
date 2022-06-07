# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# -À vista dinheiro/cheque: 10% de desconto, -À vista no cartão: 5% de desconto, -Em até 2x no cartão: Preço normal,
# -3x ou mais no cartão: 20% de juros.

valor = float(input('Digite o valor do produto: R$'))

print('1- À vista dinheiro/cheque')
print('2- À vista no cartão')
print('3- Em até 2x no cartão')
print('4- 3x ou mais no cartão')

n = int(input('Escolha a forma de pagamento: '))

if n == 1:
    print('O valor da compra será de R${:.0f},00'.format(valor - (valor*0.10)))
elif n == 2:
    print('O valor da compra será de R${:.0f},00'.format(valor - (valor*0.05)))
elif n == 3:
    print('O valor da compra será de R${:.0f},00'.format(valor))
elif n == 4:
    p = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {} de R${:.0f},00'.format(p,(valor + (valor*0.20))/p))
    print('O valor da compra será de R${:.0f},00'.format(valor + (valor*0.20)))
else:
    print('Opção inválida! Tente novamente.')


