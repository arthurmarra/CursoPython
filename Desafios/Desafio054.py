# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas ainda não atingiram a
# maioridade e quanta ja são maiores.

atual = 2021
maiores = 0
menores = 0
for c in range(0,7):
    ano = int(input('Digite seu ano de nascimento: '))
    if atual - ano >= 21:
        maiores += 1
    else:
        menores += 1

print('Maiores de idade {}'.format(maiores))
print('Menores de idade {}'.format(menores))
