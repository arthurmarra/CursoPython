# Refaça o DESAFIO051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura while.


a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont=0

while cont <= 10:
    print('{} > '.format(a1), end = '')
    a1 += r
    cont += 1
print('FIM')