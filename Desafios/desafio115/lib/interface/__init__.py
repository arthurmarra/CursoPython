def leiaInt(num):
    while True:
        try:
            p = int(input(f'{num}'))
        except (ValueError, TypeError):
            print('ERRO! O valor digitado não é um número INTEIRO.')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados.')
            return 0
        else:
            return p

def linha(tam =42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lst):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lst:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc