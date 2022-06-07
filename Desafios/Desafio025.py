# Crie um programa que pergunte o nome da pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite seu nome: ')).strip().upper()

#divide = nome.split()
#print(divide.count('SILVA'))
if 'SILVA' in nome:
    print('Seu nome tem SILVA!!')
else:
    print('Seu nome não tem SILVA!!')



