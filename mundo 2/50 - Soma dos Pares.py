s = 0
c = 0
for d in range(1,7):
    n = int(input('Digite 1 valor' ))
    if n % 2 == 0:
        s += n
        c += 1
print('Você digitou {} números pares e a soma deles é {} '.format(c,s))
