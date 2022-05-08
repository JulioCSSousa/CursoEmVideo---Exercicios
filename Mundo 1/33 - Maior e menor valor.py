print('\033[0;33m Vou adivinhar qual o maior número e o menor ')
a = float(input('Entre com um número '))
b = float(input('Outro número '))
c = float(input('E outro '))
menor = a
if b<c and b<c:
    menor = b
if c<b and c<a:
    menor = c
print('\033[0;34m O menor número foi {} '.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior numero é {} '.format(maior))