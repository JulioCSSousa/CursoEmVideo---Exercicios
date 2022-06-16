#Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dados = {}
dados['Nome'] = str(input('Entre com o nome do aluno '))
dados['Média'] = float(input(('Entre com a média ')))
if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'
print(dados)