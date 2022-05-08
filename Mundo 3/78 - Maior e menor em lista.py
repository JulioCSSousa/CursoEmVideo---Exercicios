#078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
maior = 0
menor = 0
lista = []
for c in range(1,6):
    lista.append(int(input('Digite um valor ')))
for c, v in enumerate(lista):
    print(f'Na posiçao {c} tem o valor {v} ')
for i, n in enumerate(lista):
    if n == max(lista):
        maior = i
for k, l in enumerate(lista):
        if l == min(lista):
            menor = k
print(f'O maior valor na lista é {max(lista)} e sua posição é {maior}')
print(f'O menor valor na lista é {min(lista)} e sua posição é {menor}')
