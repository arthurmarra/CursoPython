# Refaça o DESAFIO009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.


cont=0
n = int(input('Digite um número: '))
for c in range (1, 11):
    cont+=1
    print('{} x {:2} : {:2}'.format(n, cont, n*cont))