# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = ''
while sexo in 'MF':
    sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo inválido! Digite novamente seu sexo: ')).strip().upper()
