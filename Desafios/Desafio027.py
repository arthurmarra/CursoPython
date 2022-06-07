# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.

nome = str(input('Digite seu nome: ')).strip()

div = nome.split()

print('Seu primeiro nome é {}'.format(div[0]))
print('Seu último nome é {}'.format(div[len(div)-1]))