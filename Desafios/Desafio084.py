pessoas = []
dados = []
qtdpessoas = maiorpeso = menorpeso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if maiorpeso < dados[1]:
            maiorpeso = dados[1]
        if menorpeso > dados[1]:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()


    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if perg == 'N':
        break

print('-='*30)
print(f'Os dados foram {pessoas}')
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas!')
print(f'O maior peso foi {maiorpeso} KGs. Peso de ', end = '')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f' de {p[0]}')
print(f'O menor peso foi {menorpeso} KGs. Peso de ', end = '')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'{p[0]} ', end='')