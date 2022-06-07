# Melhore o DESAFIO061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
# disser que quer mostrar 0 termos.

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont=0

while cont <= 10:
    print('{} > '.format(a1), end = '')
    a1 += r
    cont += 1
    if cont == 10:
        perg = str(input('\nDeseja mostrar mais alguns termos? (S/N) ')).upper().strip()
        if perg in 'Ss':
            qtdtermos = int(input('Quantos termos a mais? '))
            termosmais = cont + qtdtermos
            if qtdtermos == 0:
                break
            else:
                while cont < termosmais:
                    print('{} > '.format(a1), end='')
                    a1 += r
                    cont+=1
        elif perg in 'Nn':
            break
print('FIM')