def leiaInt(num):
        while True:
            try:
                p = float(input(f'{num}'))
            except (ValueError, TypeError):
                print('ERRO! O valor digitado não é um número INTEIRO.')
            except KeyboardInterrupt:
                print('O usuário preferiu não informar os dados.')
                return 0
            else:
                return p


def leiaFloat(num):
    while True:
        try:
            p = float(input(f'{num}'))
        except (ValueError,TypeError):
            print('ERRO! O valor digitado não é um número REAL.')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados.')
        else:
            return p

i = leiaInt('Digite um INTEIRO: ')
f = leiaFloat('Digite um REAL: ')

print(f'O valor inteiro digitado foi {i} e o real foi {f}')