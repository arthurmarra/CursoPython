matriz = [[0,0,0], [0,0,0], [0,0,0]]
somapar = somaterceira = maior = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para[{l}, {c}]: '))
        if matriz[l][c] % 2 ==0:
            somapar += matriz[l][c]
        while matriz[l][2]:
            somaterceira += matriz[l][c]
            break
        if c == 0:
            maior = matriz[1][c]
        elif maior < matriz[1][c]:
            maior = matriz[1][c]
#for c in range(0, 3):
#    if c == 0:
#        maior = matriz[1][c]
#    elif maior< matriz[1][c]:
#        maior = matriz[1][c]

for l in  range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]:^5}', end = '')
    print()

print(f'A soma de todos os valores pares é: {somapar}')
print(f'A soma de todos os valores da terceira coluna é: {somaterceira}')
print(f'O maior valor da segunda linha é: {maior}')