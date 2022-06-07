camp = {}
gols = []
cont = saldogols = 0

camp['nome'] = str(input('Nome do Jogador: '))
qtpartidas = int(input(f'Quantas partidas {camp["nome"]} jogou? '))

while cont <= qtpartidas-1:
    v = int(input(f'Quantos gols na partida {cont+1}:'))
    saldogols += v
    gols.append(v)
    cont+=1
    v=0
camp['total'] = saldogols
camp['gols'] = gols
for k, j in camp.items():
    print(f'O campo {k} tem valor {j}')

print('-='*30)
print(f'O jogador {camp["nome"]} jogou {qtpartidas} partidas')
for k, j in enumerate(gols):
    print(f'=> na partida {k+1}, fez {j} gols')
print(f'Totalizando um saldo de {camp["total"]} gols')