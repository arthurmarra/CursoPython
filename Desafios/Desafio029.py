# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo
# que ele foi multado. A multa deve custar R$7,00 por cada km acima do limite.

vel = int(input('Velocidade atual do carro: '))

if vel <= 80:
    print('Está no limite permitido de velocidade!')
else:
    print('A multa que deverá pagar é de R${},00'.format(((vel-80)*7)))