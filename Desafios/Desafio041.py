# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria de acordo com sua idade: -Até 9 anos:MIRIM, -Até 14 anos:INFANTIL, -Até 19 anos:JUNIOR, -Até 20 anos:SÊNIOR
# -Acima: MASTER


nasc = int(input('Digite o ano em que nasceu: '))

idade = 2021 - nasc

if idade <= 9:
    print('Categoria MIRIM')
elif idade <=14:
    print('Categoria INFANTIL')
elif idade <=19:
    print('Categoria JUNIOR')
elif idade <=20:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')