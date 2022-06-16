#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
#cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
total = []
print('-='*30)
print('JOGO DA MEGA SENA')
print('-='*30)
jogos = int(input('Escolha quantos jogos quer sortear? '))
print('Sorteando...')
for c in range(1,jogos+1):
    lista = [randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60)]
    total.append(lista[:])
    lista.clear()
    print(f'Jogo {c}: {total}')
print('Boa Sorte!')