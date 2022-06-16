#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

#print('Sistema de Cadastro de Notas')
#notas = []
#dados= []

#while True:
#    nome = str(input('Entre com o nome do aluno '))
#    dados.append(nome)
#    notas.append(nome)
#    n1 = float(input('Entre com a n1 '))
#    notas.append(n1)
#    n2 = float(input('Entre com a n2 '))
#    notas.append(n2)
#    media = (n1+n2)/2
#    dados.append(media)
#    sair = str(input(('Desejar continuar? '))).lower()
#    if sair == 'n':
#        break

#print('MEDIA ')
#for item in range(0, len(dados)):
#    if item % 2 == 0:
#        print(f'{item} {dados[item]:.<30}', end='')
#    else:
#        print(f'{dados[item]:>7.2f}')
#print('As notas de cada um são ')
#print(notas)
#Minha resolução ficou parcial

ficha = []

while True:
    nome = str(input('Entre com o nome do aluno '))
    nota1 = float(input('Entre com a n1 '))
    nota2 = float(input('Entre com a n2 '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media ])
    sair = str(input(('Desejar continuar? [s/n]'))).lower()
    if sair == 'n':
        break
print('-='*30)
print(f'{"No.":<4} {"NOME":>10}{"MEDIA":>8}')
print('-'*35)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]} ')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? [999 parar] '))
    if opc == 999:
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]} ')