from time import sleep
def contador(inic, fim, passo):
    print('=' * 30)
    print(f'Contagem de {inic} a {fim} em {passo} em {passo}')
    print('=' * 30)
    for i in range(inic, fim, passo):
        print(i, end=' ')
        sleep(0.2)
    print('Fim')



contador(1,10,1)
contador(10,1,-2)
print('Agora é sua vez! Caso queira fazer contagem regressiva, use valor negativo no passom ex: -1,-2')
a = int(input('Numero inicial '))
b = int(input('Numero final '))
c = int(input('De quanto em quanto? [passo] '))
if c == 0:
    c = 1
if b > a and c > 0:
    c *= -1
contador(a,b,c)