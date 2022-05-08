print('DESCUBRA SE A FRASE É UM PALINDROMO ')
nome = str(input('Entre com a frase ')).strip().upper()
p = nome.split()
j =''.join(p)
inverso = ''
print('Você digitou {} '.format(p))
for c in range(len(j)-1,-1,-1):
    inverso += j[c]
print('O inverso de {} é {} '.format(j,inverso))
if inverso == j:
    print('Temos um palíndromo ')
else:
    print('Não temos um palindromo ')

