nome = str(input('Digite seu nome: ')).strip()

#print('Letras Maiúsculas: {}\nLetras Minúsculas: {}\nSeu Nome tem {} letras\n'
 #     'Seu primeiro nome tem {} letras'.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), nome.find(' ')))

print('Nome com letras maiúsculas: {}'.format(nome.upper()))
print('Nome com letras minúsculas: {}'.format(nome.lower()))
print('Quantas letras(sem considerar espaços): {}'.format(len(nome) - nome.count(' ')))
divide = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(divide[0])))
print('Seu segundo nome é {}'.format(divide[1]))
