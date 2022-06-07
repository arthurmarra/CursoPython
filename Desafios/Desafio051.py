# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
# desta progressão.

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
décimo = a1 + (10 - 1) * r

for c in range(a1, décimo + r, r):
    print('{}'.format(c), end=' > ')
print('ACABOU')