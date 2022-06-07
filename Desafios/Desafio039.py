# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# -Se ele ainda vai se alistar ao serviço militar, -Se é a hora de se alistar., -Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Digite seu ano de nascimento: '))

idade = 2021 - ano

idaderest = 18 - idade
rest = idade - 18

if idade == 18:
    print('Tá na hora de se alistar!')
elif idade < 18:
    print('Ainda faltam {} anos para você se alistar'.format(idaderest))
else:
    print('Ja passou {} anos da hora de se alistar! Vá correndo!'.format(rest))

