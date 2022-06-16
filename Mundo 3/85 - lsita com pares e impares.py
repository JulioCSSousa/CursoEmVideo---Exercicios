#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

numeros = []
numpares = []
numimp = []
n = 0
for c in range(1,8):
    n = int(input('Entre com um número '))
    if n % 2 == 0:
        numpares.append(n)
    else:
        numimp.append(n)
        numeros.clear()
    numpares.sort()
    numimp.sort()
numeros.append(numimp[:])
numeros.append(numpares[:])
print(numeros)

#AEEEEEEEEEEEEE ficou diferente da rsolução as funcionou