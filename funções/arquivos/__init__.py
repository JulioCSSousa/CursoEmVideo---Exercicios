from funções.menus import *
def arquivoExite(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo ')
    else:
        intro('PESSOAS CADASTRADAS')
        for linhas in a:
            dado = linhas.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao ler o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao registrar os dados')
        else:
            print('Novo registro adicionado com sucesso')
            a.close()

