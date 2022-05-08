n = c = s = 0
while True:
        n = float(input('Digite um número [999 para parar] '))
        if n == 999:
            break
        c += 1
        s += n
print(f'Voce digitou {c} números e a soma deles é {s} ')