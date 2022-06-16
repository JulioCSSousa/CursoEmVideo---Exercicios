#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = []
pessoas = []
pessoaG = []
pessoap = []
while True:
    dados.append(str(input('Entre com o nome ')))
    dados.append(float(input('Entre com o peso ')))
    sair = str(input('Desejar continuar? [s/n] '))
    pessoas.append(dados[:])
    dados.clear()
    if sair == 'nN':
        break
    else:
        if sair not in 'sSnN':
            sair = str(input('Resposta invalida! Desejar continuar? [s/n] '))
        if sair == 'n':
            break
print(pessoas)
print(f'{len(pessoas)} foram cadastradas ')

for c in pessoas:
    if c[1] >= 80:
        pessoaG.append(c[:])
        print(f'Pessoas pesadas {pessoaG}')

    else:
        pessoap.append(c[:])
        print(f'pessoas leves {pessoap}' )
        pessoas.clear()