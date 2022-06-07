from datetime import date
atual = date.today()

def voto(ano):
    t=0
    t = atual.year - ano
    if t>=18 and t<=65:
        print(f'Com {t} anos: voto é OBRIGATÓRIO')
    elif t<18:
        print(f'Com {t} anos: NÃO VOTA')
    elif t >= 18 and t>=65:
        print(f'Com {t} anos: voto é OPCIONAL')
voto(int(input('Em que ano você nasceu? ')))
