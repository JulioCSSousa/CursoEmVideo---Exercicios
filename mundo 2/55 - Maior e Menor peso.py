maior = 0
menor = 0
for i in range(1,6):
    p = float(input('Digite o {} peso '.format(i)))
    if i == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
            if p < menor:
                menor = p
print('O maior peso foi {}kg '.format(maior ))
print('O menor peso foi {}kg '.format(menor ))
