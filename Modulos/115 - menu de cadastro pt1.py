from funções import menus
from funções.arquivos import *

arq = 'cursoemvideo.txt'

if not arquivoExite(arq):
    criarArquivo(arq)

while True:
    menus.intro('MENU PRINCIPAL')
    resp = menus.menu(['Mostrar Pessoas', 'Cadatrar Nova Pessoa', 'Finalizar'])
    try:
        if resp == 1:
            lerArquivo(arq)
        elif resp == 2:
            intro('NOVO CADASTRO')
            nome = str(input('Entre com o nome '))
            idade = leiaInt('Entre com a idade ')
            cadastrar(arq, nome, idade)
        elif resp == 3:
            menus.intro('FINALIZANDO... ATÉ LOGO ')
            break
        else:
            print('\033[31m Digite uma opção válida\033[m!')
    except (ValueError, TypeError):
        print('Digite uma opção válida! ')

