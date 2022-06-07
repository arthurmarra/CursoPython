def leiaInt(num):
    while True:
        v = str(input(f'{num}')).strip()
        if v.isnumeric():
            return v
        else:
            print('ERRO! O valor digitado não é um número.')


n = leiaInt('Digite um número: ')

print(f'Você acabou de digitar o número {n}')