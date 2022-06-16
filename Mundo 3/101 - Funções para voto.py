#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições

from datetime import date
def voto(ano):
    ano = date.today().year - a
    print(f'Você tem {ano} anos')
    if ano < 16:
        print('Seu voto foi negado')
    elif 16 <= ano < 18 or ano > 60:
        print('Voto opcional!')
    elif 18 >= ano < 60:
        print('Voto obrigatório! ')
    return ano


a = int(input('Ente com o seu ano de nascimento '))
voto(a)