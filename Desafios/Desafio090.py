dic = {}

n = str(input('Nome: '))

dic['nome'] = n

média = float(input(f'Média de {dic["nome"]}:'))


print(f'Média é igual a {média}')
if média >= 6:
    print('Situação é igual a APROVADO!')
elif média < 6:
   print('Situação é igual a REPROVADO!')