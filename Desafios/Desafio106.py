def miniSistema(valor):
    print(f"Acessando o manual do comando '{valor}'")
    help(valor)

while True:
    r = ' '
    print('~'*30)
    print('   SISTEMA DE AJUDA PyHELP')
    print('~' * 30)
    r = str(input(('Função ou Biblioteca > '))).strip()


    if r.upper() != 'FIM':
       miniSistema(r)
    else:
       break
print('ATÉ LOGO')

