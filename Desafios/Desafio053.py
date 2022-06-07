# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite um frase: ')).strip().upper()

palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''

for c in range(len(juntar)-1, -1, -1):
    inverso += juntar[c]

if inverso == juntar:
    print('É UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')