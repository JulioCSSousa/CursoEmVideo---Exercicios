#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tabela = ('lápis ', 1.75,
          'Borracha ', 2,
          'Caderno ', 14.50,
          'Estojo, ', 12.80,
          'Mochila ', 70.36, )
print('TABELA DE PREÇOS')
print('_'*35)
for item in range(0, len(tabela)):
    if item % 2 == 0:
        print(f'{tabela[item]:.<30}', end='')
    else:
        print(f'R${tabela[item]:>7.2f}')