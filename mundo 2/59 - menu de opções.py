from time import sleep
e = 0
n1 = float(input('Digite um valor '))
n2 = float(input('Digite outro valor '))
print('O que deseja fazer? ')
while e != 5:
    e = int(input('''
[1] Soma
[2] Multiplicação 
[3] Maior 
[4] Novos Números 
[5] Terminar 
escolha: '''))
    if e == 1:
        sleep(0.5)
        print('{} + {} = {} '.format(n1,n2,n1+n2))
    elif e == 2:
        print('{} x {} = {} '.format(n1,n2,n1*n2))
    elif e == 3:
        if n1 > n2:
            print('O maior é {} '.format(n1))
        elif n2>n1:
            print('O maior é {} '.format(n2))
        else:
            print('{} e {} são iguais '.format(n1,n2))
    elif e == 4:
        n1 = float(input('Digite um valor '))
        n2 = float(input('Digite outro valor '))
    elif e == 5:
        print('\033[32m Fim! volte sempre!')
    else:
        print('Opção inválida! Tente novamente! ')
