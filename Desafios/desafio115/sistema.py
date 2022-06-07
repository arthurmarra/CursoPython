from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Listar conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho(('NOVO CADASTRO'))
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do Sistema...')
        break
    else:
        print('Opção errada, favor digitar uma oção válida!')
    sleep(1)