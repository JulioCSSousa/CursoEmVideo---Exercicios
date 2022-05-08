from random import randint
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
c = randint(0,2)
e = int(input('Escolha [0] pedra [1] papel [2] tesoura '))
print('JÔ ')
sleep(1)
print('KEN ')
sleep(1)
print('PORRA ')
print('Você jogou {} '.format(lista[e]))
print('O computador jogou {}'.format(lista[c]))
if c == 0 and e == 1:
    print('Vo ganhou! ')
elif c == 0 and e == 2:
    print('Você perdeu ')
elif c == 1 and e == 0:
    print('Voce perdeu ')
elif c == 1 and e == 2:
    print('Você ganhou! ')
elif c == 2 and e == 0:
    print('Você ganhou! ')
elif c == 2 and e == 1:
    print('Você perdeu ')
else:
    print('Houve um empate! ')
