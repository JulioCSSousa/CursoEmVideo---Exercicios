#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='', gols=0):
    print(f'O nome do jogador é {nome} e ele fez {gols} gols')



n = str(input('Entre com o nome do jogador '))
g = str(input('Quantos gols ele fez? '))
if g.isnumeric():
    g = g
else:
    g = 0
if n.strip() == '':
    n = 'desconhecido'
else:
    ficha(n,g)
ficha(n,g)