def fatorial(n=1,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (OPCIONAL) Mostra ou não a conta
    :return: O valor do Fatorial de um número n
    """
    v=1

    if show==True:
        for i in range(n, 0, -1):
            v *= i
            if i == 1:
                print(f'{i} = {v}', end='')
            else:
                print(f'{i} x ', end='')
    else:
        for i in range(n, 0,-1):
            v*=i
        print(v)


fatorial(10, True)
print()
fatorial(7, True)
print()
fatorial(4)
print()
help(fatorial)