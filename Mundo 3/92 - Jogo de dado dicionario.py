#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter
dados = {'Jogador 1,': randint(1,7), 'Jogador 2': randint(1,7), 'Jogador 3':  randint(1,7), 'Jogador 4': randint(1,7)}
rank = {}
for k,v in dados.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
rank = sorted(dados.items(), key=itemgetter(1), reverse=True)
print(rank)
