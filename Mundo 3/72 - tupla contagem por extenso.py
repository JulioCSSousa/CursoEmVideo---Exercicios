tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n = -1
while n not in (0,1,2,3,4,5,6,7,8,9,10):
    n = int(input('Entre com um número de 0 a 10 '))
print(f'Você digitou {tupla[n]}')