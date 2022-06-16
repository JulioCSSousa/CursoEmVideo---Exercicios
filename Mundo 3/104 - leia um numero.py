#Exercício Python 104: Crie um programa que tenha a função leiaInt(),
#que vai funcionar de forma semelhante ‘a função input() do Python,
#só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(txt):
    valor = True
    ok = False
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro! Digite um número!\033[m ')
        if ok:
            break
    return valor


n = leiaInt('Digite um número ')
print(f'Você digitou {n}')