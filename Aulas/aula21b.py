def somar(a=0, b=0, c=0):
    """
    -> Função que retorna a soma dos parâmetros.
    PS: VALORES DE PARÂMETROS SÃO OPCIONAIS.
    :param a: Valor A
    :param b: Valor B
    :param c: Valor C
    :return: Sem returno
    """
    s = a+b+c
    print(f'A soma dos parâmetros vale: {s}')

help(somar)
somar(1,5,7)