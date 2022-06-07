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

