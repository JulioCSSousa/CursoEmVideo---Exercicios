print('Lojas baratosco - Aqui os podrutos são dus bão ')
print('='*30)
total = m = cont = menor = 0
mv = ''
while True:
    nome = str(input('Insira um podruto '))
    valor = float(input('Qual o valor? R$'))
    total += valor
    if valor > 1000:
        m += 1
    cont += 1
    print(cont)
    e = str(input('Deseja continuar? [S/N] '))
    while e not in 'SsNn':
        e = str(input('Opção inválida! Tente novamente '))
    if e in 'Nn':
        break
    if cont == 1 or valor < menor:
        menor = valor
        mv = nome

print(f'O total de compra foi de R${total:.2f} ')
print(f'Temos {m} podrutos custando mais de R$1000.00 ')
print(f'O podruto mais barato foi {mv} e custa R${menor:.2f} ')

