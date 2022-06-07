# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no
# intervalo de 1 até 500.

s = 0
cont = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        s += c
        cont += 1

print('Existem {} números que são divizíveis por 3 e a soma deles vale {}.'.format(cont,s))