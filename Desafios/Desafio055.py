# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(0,5):
    peso = float(input('Digite seu peso: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é {:.2f}'.format(maior))
print('O menor peso é {:.2f}'.format(menor))