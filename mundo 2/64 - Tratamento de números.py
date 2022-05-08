n = 0
c = -1
s = -999
while n != 999:
    n = float(input('Digite um número [999 para parar] '))
    c += 1
    s += n
print('Voce digitou {} números e a soma deles é {} '.format(c,s))

