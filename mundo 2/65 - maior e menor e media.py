print('Digite 2 números inciais para calcular média maior e menor ')
c = 0
soma = num = maior = menor = 0
mais = 's'or 'n'
while c <= 1:
    num = int(input('Digite um número '))
    c += 1
    soma += num
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
            if num < menor:
                menor = num
mais = str(input('Deseja continuar digitando? [s/n] '))
while mais == 's':
    num = int(input('Digite um número '))
    c += 1
    soma += num
    mais = str(input('Deseja continuar digitando? [s/n] '))
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
            if num < menor:
                menor = num
print('{} numeros foram digitados e a média é de {} '.format(c,soma/c))
print(f'maior numero é {maior} e o menor {menor} ')
print('FIM')



