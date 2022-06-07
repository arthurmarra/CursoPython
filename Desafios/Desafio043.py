# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo: -Abaixo de 18.5: ABAIXO DO PESO, -Entre 18.5 e 25: PESO IDEAL, -25 até 30: SOBREPESO, -30 até 40:
# OBESIDADE, -Acima de 40: OBESIDADE MÓRBIDA.

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / pow(altura,2)

if imc < 18.5:
    print('Abaixo do peso!')
elif imc >=18.5 and imc < 25:
    print('Peso ideal!')
elif imc >=25 and imc < 30:
    print('Sobrepeso!')
elif imc >=30 and imc < 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida! CUIDADO!')