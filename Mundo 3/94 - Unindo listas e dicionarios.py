# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

somaidade = 0
mediaid = 0
pessoas = []
dados = {}
while True:
    dados.clear()
    dados['Nome'] = nome = str(input('Escreva seu nome '))
    while True:
        dados['Sexo'] = str(input('Qual seu sexo? [m/f] ')).lower()
        if dados['Sexo'] in 'mf':
            break
        print('Digite apenas m ou f')
    dados['Idade'] = int(input('Entre com a idade '))
    somaidade = somaidade + dados['Idade']
    pessoas.append(dados.copy())
    while True:
        sair = str(input('Quer continuar? [s/n] ')).lower()
        if sair in 'sn':
            break
        print('Resposta invalidade! Digite S ou N')
    if sair == 'n':
        break
mediaid = somaidade/len(pessoas)
print(pessoas)
print(f'{len(pessoas)} cadastradas ')
print(f'A média de idade é: {mediaid:2f}')
print('As mulheres cadastradas são: ')
for dados in pessoas:
    if dados['Sexo'] == 'f':
        print({dados['Nome'], dados['Idade']})
print('A idade a cima da média é de: ')
for dados in pessoas:
    if dados['Idade'] > mediaid:
        print({dados['Nome'], dados['Idade']})

