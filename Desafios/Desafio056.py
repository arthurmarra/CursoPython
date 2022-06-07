# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# -A média de idade do grupo. -Qual é o nome do homem mais velho. -Quantas mulheres têm menos de 20 anos.

mi = 0
somai = 0
nomev = ''
cmn = 0

for c in range(0,4):
    nome = str(input('Digite seu nome: ')).upper().strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo M/F: ')).upper().strip()
    somai += idade
    if c == 0 and sexo == 'M':
        mi = idade
        nomev = nome
    elif c != 0 and sexo == 'M' and idade > mi:
        mi = idade
        nomev = nome
    if idade < 20 and sexo == 'F':
        cmn += 1


mediai = somai /4
print('A média de idade do grupo é de {} anos'.format(mediai))
print('O nome do homem mais velho é {}'.format(nomev))
print('Existem {} mulher com menos de 20 anos'.format(cmn))