#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
#indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num=0,show=False):
    f = 1
    for c in range(num, 1, -1):
        f *= c
        if show == True:
            print(f'{c}x{c-1}')
    return f

print(fatorial(5,True))