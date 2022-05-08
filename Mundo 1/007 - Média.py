print('digite 1 para media aritmética ')
print('digite 2 para media geométrica ')
print('digite 3 para media harmônica ')
r = int(input('digite '))
n1 = float(input('Digite a nota da n1: '))
n2 = float(input('Digite a nota da n2: '))
if (r == 1):
    m = float((n1 + n2) / 2)
    print('A media é: ', m)
elif (r == 2):
    m = (n1 * n2) ** (1 / 2)
    print('A media é: ', m)
else:
    (r == 3)
    m = float(2 / (1 / n1 + 1 / n2))
    print('A media é: ', m)