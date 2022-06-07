dic = {}
tempcontr = temporest = 0
while True:
    dic['nome'] = str(input('Nome: '))
    ano = int(input('Ano de Nascimento: '))
    idade = 2021 - ano
    dic['idade'] = idade
    ct = int(input('Carteira de Trabalho (0 não tem): '))
    if ct == 0:
        dic['ctps'] = 0
        break
    else:
        dic['ctps'] = ct
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salário'] = float(input('Salário: R$ '))
    tempcontr = 2021 - dic['contratação']
    temporest = 35 - tempcontr
    dic['aposentadoria'] = dic['idade'] + temporest
    break


for k,v in dic.items():
    print(f'{k} tem o valor {v}')