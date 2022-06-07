from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i <= f:
        print('-=' * 30)
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for k in range(i, f+1, p):
            print(f'{k} ', end='')
            sleep(0.5)
        print(' FIM!')
        print('-=' * 30)
    elif i >= f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for j in range(i, f-p, -p):
            print(f'{j} ', end='')
            sleep(0.5)
        print('FIM!')
        print('-=' * 30)


contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez de personalizar a contagem!')

início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(início, fim, passo)
