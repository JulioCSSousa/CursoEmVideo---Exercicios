#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

#matrix = [ ]
#matrix2 = [ ]
#matrix3 = [ ]
#for x in range(0,3):
#    matrix.append(int(input('Entre com um numero ')))
#for x in range(0,3):
#    matrix2.append(int(input('Entre com um numero ')))
#for x in range(0,3):
#    matrix3.append(int(input('Entre com um numero ')))
#print(matrix)
#print(matrix2)
#print(matrix3)

#kkkkkkkkkkkkkkk recorri ao cheat mas funcionou

#jeito certo

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
