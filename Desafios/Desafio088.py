from random import randint
from time import sleep
nj = int(input('Quantos jogos você quer que eu sorteie? '))
tot =0
aux = []
jogos = []
while tot<=nj-1:
    cont = 0
    while True:
        c = randint(1, 60)
        if c not in aux:
            aux.append(c)
            cont+=1
        if cont>=6:
            break
    aux.sort()
    jogos.append(aux[:])
    aux.clear()
    tot+=1

print(f'Os números sorteados foram:')
for i,v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}' )
    sleep(1)

print('BOA SORTE!!')