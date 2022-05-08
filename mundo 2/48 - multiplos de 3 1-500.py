soma = 0
for n in range(1,501,2):
    if n % 3 == 0:
        soma = soma+n
print('A soma dos multiplos de 3 de 1-500 é {} '.format(soma))
