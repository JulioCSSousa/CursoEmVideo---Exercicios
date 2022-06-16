#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib.request
import urllib

def siteon(site):
    try:
        site=urllib.request.urlopen('https://www.'+site+'/')
    except urllib.request.URLError:
        print(f'Site do {site} não está disponível no momento! ')
    else:
        print('Site acessado com sucesso ')
    return site

site = str(input('Entre com um URL de um site '))
siteon(site)
