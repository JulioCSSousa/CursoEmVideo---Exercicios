#interactive help
help(print)
print(input.__doc__)
#docString
def contador(i, f, p):
    """
    :param i: inicio
    :param f: final da contagem
    :param p: passo, de quanto e quanto
    :return:
    """
    c = 1
    while c <= f:
        print(f'{c}',end=' ')
        c += p
contador(0,100,10)

print()

#argumentos opcionais
def somar(a=0,b=0,c=0):#como os paramentros valem 0, n retornara erro caso n seja digitado nada
    s = a+b+c
    print(f'A soma vale {s}')

somar(5,8)
#escopo de variaveis
#Variaveis de uma função só funcionam dentro da função a n ser que torne ela global
def exemplo():
    global a
    a = int
exemplo()
a = 0
#funçoes com retorno
def fatorial(num=0):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
n = int(input('Entre com um número '))
print(f'O fatorial de {n} é {fatorial(n)}')