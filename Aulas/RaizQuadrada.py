from math import sqrt
def raiz(n=0, i=0):
    """
    -> Programa feito pra fazer a raíz dos valores passados nos parâmetros.
    PS: Se não for passado um valor para "i" o default é fazer RAIZ QUADRADA
    :param n: Valor a ser passado.
    :param i: Índice da raiz. (OPCIONAL)
    :return: Sem retorno
    """
    if n != 0 and i == 0:
        print(f'Raiz Quadrada: {sqrt(n)}')
    if i > 0:
        v = n ** (1/i)
        print(f'Raiz {i} de {n}: {v}')
    if n==0 and i==0:
        print('Você deve digitar ao menos algum valor!')

#help(raiz)
raiz(16)
raiz(8,3)
raiz()
