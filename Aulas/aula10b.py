n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

m = (n1+n2)/2

print('MÉDIA: {}'.format(m))

if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi baixa! ESTUDE MAIS!')