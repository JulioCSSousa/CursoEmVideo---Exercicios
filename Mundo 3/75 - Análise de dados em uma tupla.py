#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

cont9 = 0
numeros = (int(input('Entre com um numéro ')),
           int(input('Entre com um numéro ')),
           int(input('Entre com um numéro ')),
           int(input('Entre com um numéro ')))
print(f'Voce digitou os valores {numeros}')
print(f'O número 9 apareceu {numeros.count(9)}x ')
if 3 in numeros:
    print(f'O número 3 apareceu ma posição {numeros.index(3)+1}')
else:
    print('número 3 não digitado ')
print('Numeros par ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')