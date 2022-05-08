from random import randint
while True:
    jogador = int(input('Diga um valor '))
    comp = randint(0,1)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? ')).strip.upper()
    print(f'Você jogou {jogador} e o computador jogou {comp}, e a soma é {total} ')
