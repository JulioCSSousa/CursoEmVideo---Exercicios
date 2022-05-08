from random import choice
from time import sleep
l = [1,2,3,4,5]
e = choice(l)
print('Vou pensar em um número de 0 a 5, tente advinha ')
n = int(input('Em que número eu pensei? '))
print('\033[1;32m PROCESSANDO... ')
sleep(2)
if n < 0 or n > 5:
    print('ha! ha! Muito engraçado smart ass! Tente de novo ')
elif e == n:
    print('Ok... Pensei no número {}... Você ganhou! Vamos mais uma vez '.format(e))
else:
    print('Pensei no número {}! Você perdeu! Tente de novo '.format(e))

