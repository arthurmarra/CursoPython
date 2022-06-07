def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno.
    Função criada por Arthur Marra!
    """
    c=i
    while c<=f:
        print(f'{c} ', end='')
        c+=p
    print('FIM!')

    for v in range(i, f+1, p):
        print(f'{v} ', end='')
    print('FIM!')

help(contador)

contador(1, 10, 1)