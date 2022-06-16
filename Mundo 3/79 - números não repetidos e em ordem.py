#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
while True:
    n = int(input('Entre com um número inteiro: '))
    if n not in lista:
        lista.append(n)
        print('Valor adcionado com sucesso! ')
    else:
        print('Valor ja adcionado. Digite outro ')
    e = str(input('Deseja continuar [s/n]')).lower()
    print(lista)
    if e == 'n':
        break
    else:
        while e not in 'sn':
            e = str(input('Resposta inválida! Deseja continuar [s/n]')).lower()
    if e == 'n':
        break
print(f'O ordem crescente {sorted(lista)}')
print(f'Decrescente {lista.sort(reverse = True)}')


