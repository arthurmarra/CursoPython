galera = []
dados = []

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('idade: ')))
    galera.append(dados[:])
    dados.clear()

print(galera)