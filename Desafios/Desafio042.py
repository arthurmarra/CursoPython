# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# -Equilátero: todos os lados iguais, -Isósceles: dois lados iguais, -Escaleno: todos os lados diferentes

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

triangulo = False

if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1+r2:
    triangulo = True
else:
    print('Não dá para formar um triângulo.')

if triangulo and r1 == r2 and r2 == r3 :
    print('Triângulo equilátero.')
elif triangulo and r1 == r2 or triangulo and r1 == r3 or triangulo and r2 == r3:
    print('Triângulo isósceles')
elif triangulo and r1 != r2 or triangulo and r1 != r3 or triangulo and r2 != r3:
    print('Triângulo escaleno')

