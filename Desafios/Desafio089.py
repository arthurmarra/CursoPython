aluno = []
media=0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    aluno.append([nome, [nota1,nota2], media])
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if perg == 'N':
        break
print('-='*30)
print('No.  NOME        MÉDIA')
print('-'*15)

for i, v in enumerate(aluno):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')

while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(aluno)-1:
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')

