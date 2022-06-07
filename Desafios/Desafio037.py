# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1- para binário, 2- para octal, 3- para hexadecimal

print('==='*15)

num = int(input('Digite o número que quer converter: '))

print('1- Binário')
print('2- Octal')
print('3- Hexadecimal')

n = int(input('Digite a opção desejada: '))



if n == 1:
    print('Seu número convertido pra binário é: {}'.format(bin(num)[2:]))
elif n == 2:
    print('Seu número convertido pra octal é: {}'.format(oct(num)[2:]))
elif n == 3:
    print('Seu número convertido pra hexadecimal é: {}'.format(hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente!')

print('==='*15)
