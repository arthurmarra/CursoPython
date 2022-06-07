# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o preograma deverá perguntar
# se o usuário quer ou não continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos. B) Quantos homens foram cadastrados. C) Quantas mulherres tem menos de 20 anos.

qtdhom = mulhernova = maiores = 0


while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    perg = ' '
    if idade > 18:
        maiores += 1
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()[0]
    if sexo in 'F' and idade < 20:
        mulhernova += 1
    if sexo in 'M':
        qtdhom += 1
    while perg not in 'SN':
        perg = str(input('Deseja cadastrar mais alguém? (S/N) ')).strip().upper()[0]
    if perg in 'N':
        break

print(f'Maiores de 18 anos: {maiores}\nTotal de homens cadastrados: {qtdhom}\nMulher com menos de 20 anos: {mulhernova}')