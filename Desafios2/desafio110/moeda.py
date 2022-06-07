def moeda(preço =0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def metade(num = 0, p = False):
    if p == True:
        return moeda(num / 2)
    else:
        return num / 2

def dobro(num= 0, p = False):
    if p == True:
        return moeda(num * 2)
    else:
        return num * 2

def aumentar(num=0, porc= 0, p = False):
    valor = porc/100
    if p == True:
        return moeda(num + (num *valor))
    else:
        return num + (num *valor)

def diminuir(num, porc =0, p = False):
    valor = porc / 100
    if p == True:
        return moeda(num - (num *valor))
    else:
        return num - (num * valor)

def resumo(num, a, b):
    valora= a/100
    valorb= b/100
    print('-'*30)
    print('      RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: {moeda(num):>15}')
    print(f'Dobro do preço: {moeda(num * 2):>15}')
    print(f'Metade do preço: {moeda(num /2):>15}')
    print(f'{a} de aumento: {moeda(num+(num*valora)):>15}')
    print(f'{b} de redução: {moeda(num-(num*valorb)):>15}')