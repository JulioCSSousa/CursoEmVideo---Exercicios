t = int(input('Digite o primeiro termo '))
r = int(input('Qual a razão? '))
s = t+r
d = ((10-1)*r)
for s in range(t,d,r):
    print('{} '.format(s), end='-> ')