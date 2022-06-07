p = str(input('Digite uma expressão: '))

pilha = []
#lista.append('Olá')
for simb in p:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está incorreta')