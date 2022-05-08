from random import choice
from time import sleep
c = 1
l = [1,2,3,4,5,6,7,8,9,10]
e = choice(l)
print('Vou pensar em um número inteiro de 0 a 10, tente advinhar ')
n = int(input('Em que número eu pensei? '))
if n < 0 or n > 10:
    print('ha! ha! Muito engraçado smart ass! Tente de novo ')
while n < e:
    n = int(input('\033[31m hmm... Um pouco mais espartano! Tente de novo '))
    c += 1
while n > e:
    n = int(input('\033[32m hmm... Menos! tente de novo! '))
    c += 1
if n == e:
    print('\033[33m Ok! Você Acertou em {} tentativas! Eu pensei no número {}!  '.format(c,e))