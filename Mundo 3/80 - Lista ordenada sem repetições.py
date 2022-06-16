#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.l
lista = []
for c in range(0, 5):
    n = int(input('Digite um número '))
    lista.append(n)
    print(f'Posição {lista.index(n)}')
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista(pos):
                lista.insert(pos, n)
                break
            pos =+ 1
print('-'*30)
print(f'Os valores inseridos em ordem {lista}')
#Exercicio complicado, nao consegui resolvwe sozinho