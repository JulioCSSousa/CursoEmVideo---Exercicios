#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista1 = []
listapar = []
listaimpar = []
while True:
    n = int(input('Entre com um número '))
    if n % 2 == 0:
        lista1.append(n)
        listapar.append(n)
        if 0 in listapar:
            listapar.remove(0)
    else:
        lista1.append(n)
        listaimpar.append(n)
    e = str(input('Deseja continuar? [s/n]' )).lower()
    if e == 'n':
        break
    else:
        if e not in 'sn':
            e = str(input('Opçao inválida! Deseja continuar? [s/n]')).lower()
print(f'Todos nuúmero digitados foram {lista1}')
print(f'Os numéros pares foram {listapar}')
print(f'Os números impares foram {listaimpar}')