#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    n = int(input('Entre com um número '))
    lista.append(n)
    print(lista)
    e = str(input('Deseja continuar? [s/n]')).lower()
    if e == 'n':
        break
    elif e not in 'sn':
        e = str(input('Deseja continuar? [s/n]')).lower()
print(f'{len(lista)} números foram digitados')
lista.sort(reverse=True)
print(f'forma decrescente {lista}')
if 5 in lista:
    print('O valor 5 foi digitado e esta na lista ')
else:
    print('O valor 5 não esta na lista ')