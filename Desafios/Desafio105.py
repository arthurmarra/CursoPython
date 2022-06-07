alunos = dict()
def notas(* num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    maior = menor = soma = media =0

    for k, v in enumerate(num):
        soma += v
        if k == 0:
            maior = menor = num[k]
        else:
            if maior<num[k]:
                maior = num[k]
            if menor>num[k]:
                menor = num[k]
    media = (soma / len(num))
    alunos['total'] = len(num)
    alunos['maior'] = maior
    alunos['menor'] = menor
    alunos['média'] = media
    if sit:
        if media>=6:
            alunos['situação'] = 'APROVADO'
        else:
            alunos['situação'] = 'REPROVADO!'

    return alunos

resp = notas(6, 7, 6, sit = True)
print(resp)
print()
help(notas)