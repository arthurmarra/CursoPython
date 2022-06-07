pessoas = list()
dados = dict()
somaidade = qtpessoas =0
while True:
    dados.clear()

    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('sexo [M/F]')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO, sexo deve ser M(Masculino) ou F(Feminino)')
    dados['idade'] = int(input('Idade: '))

    pessoas.append(dados.copy())

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais alguem? [S/N]')).strip().upper()[0]

    if resp == 'N':
        break


print(f'A quantidade de pessoas cadastradas é de {len(pessoas)}')
for p in pessoas:
    if p['idade']:
        somaidade+= p['idade']
media = somaidade/len(pessoas)
print(f'Média das idades: {media:.2f} ')
print(f'Lista com todas as mulheres: ', end = '')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end = '')
print()
print(f'A lista de pessoas com idade acima da média:')
for p in pessoas:
    if p['idade']>=media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v} ;', end= '')

