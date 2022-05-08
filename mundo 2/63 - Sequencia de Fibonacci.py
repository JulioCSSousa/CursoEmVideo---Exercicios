print('Sequencia de Fibonacci ')
p = int(input('Digite quantos termos deseja calcular '))
t1 = 0
t2 = 1
cont = 3
print('{} -> {} '.format(t1,t2 ), end='')
while cont <= p:
    t3 = t1 + t2
    cont += 1
    t1 = t2
    t2 = t3
    print(' {} '.format(t3), end='-> ')
print('FIM ')