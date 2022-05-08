p = int(input('Digite o primeiro termo '))
r = int(input('Qual a razão? '))
c = 1
termo = p
while c <= 10:
    termo += r
    c += 1
    print('{} '.format(termo), end='-> ')