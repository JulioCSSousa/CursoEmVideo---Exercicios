print('Caixa eletrônico ')
ced50 = ced20 = ced10 = ced5 = ced1 = 0
valor = int(input('Qual valor deseja sacar? '))
total = valor
while total > 0:
    if total >= 50:
        ced50 += 1
        total -= 50
    elif total < 50 and total >= 20:
        ced20 += 1
        total -= 20
    elif total < 20 and total >= 10:
        ced10 += 1
        total -= 10
    elif total < 10 and total >= 5:
        ced5 += 1
        total -= 5
    elif total < 5:
        ced1 += 1
        total -= 1
    else:
        break
print(f'Você recebeu {ced50} notas de 50')
print(f'{ced20} notas de 20 ')
print(f'{ced10} notas de 10 ')
print(f'{ced5} notas de 5')
print(f'{ced1} notas de 1')
print('Obrigado! volte sempre ')
