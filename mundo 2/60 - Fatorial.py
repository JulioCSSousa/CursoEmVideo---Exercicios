n = int(input('Entre com um número para saber seu fatorial '))
c = n+1
f = 1
while c > 1:
    c -= 1
    f *= c
    print('{}'.format(c),end='')
    print('x' if c>1 else '=', end='')
print('{} '.format(f))
