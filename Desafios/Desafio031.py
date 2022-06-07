# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passa, cobrando R$0,50 por
# KM para viagens até 200KM e R$0,45 para viagens mais longas.

v = float(input('Digite a distância da viagem em KM: '))

if v <= 200:
    print('O valor da viagem será R${:.0f},00 '.format(v*0.50))
else:
    print('O valor da viagem será R${:.0f},00 '.format(v*0.45))