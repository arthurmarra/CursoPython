from math import sqrt

cad = int(input('Digite o valor do cateto adjacente: '))
cop = int(input('Digite o valor do cateto oposto: '))

hip = sqrt(pow(cad,2) + pow(cop,2))


print('O valor da hipotenusa é {} .'.format(hip))