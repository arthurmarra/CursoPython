# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%
# Para inferiores ou igual, o aumento é de 15%.

sal = float(input('Digite o seu salário: '))

if sal> 1250:
    print('O seu salário recebeu aumento de R${:.0f},00'.format(sal*0.10))
else:
    print('O seu salário recebeu aumento de R${:.0f},00'.format(sal*0.15))