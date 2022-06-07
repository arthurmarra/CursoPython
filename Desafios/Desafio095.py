camp = dict()
jogadores = list()
gols = list()
cont = saldogols = 0

while True:
    camp.clear()
    gols.clear()
    v = qtpartidas = cont = saldogols = 0
    camp['nome'] = str(input('Nome do Jogador: '))
    qtpartidas = int(input(f'Quantas partidas {camp["nome"]} jogou? '))

    while cont <= qtpartidas-1:
        v = int(input(f'Quantos gols na partida {cont+1}:'))
        saldogols += v
        gols.append(v)
        cont+=1
    camp['total'] = saldogols
    camp['gols'] = gols.copy()
    jogadores.append(camp.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break


print('-='*30)
print('Cod   Nome   Gols       Total')

for k, j in enumerate(jogadores):
    print(f'{k}     {j["nome"]}  {j["gols"]}        {j["total"]}')


opc = 0
while opc != 999:
    opc = int(input('Mostrar dados de qual jogador? '))
    if opc <= len(jogadores)-1:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opc]["nome"]}: ')
        for k, j in enumerate(jogadores[opc]['gols']):
            print(f'=> na partida {k + 1}, fez {j} gols')
    elif opc>len(jogadores):
        print(f'ERRO! Não existe jogador com o código {opc}! Tente novamente')
print('<< VOLTE SEMPRE >>')