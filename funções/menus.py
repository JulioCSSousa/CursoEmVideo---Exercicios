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


def linha(tam=42):
    return '='*tam


def menu1():
    pessoal = [{'Nome':'Julio', 'Idade':28},{'Nome':'Julio', 'Idade':28},{'Nome':'Julio', 'Idade':28},]
    pessoas = {'Nome':'Julio', 'Idade':28}
    return pessoal


def menu2():
    intro('Novo Cadastro')


def intro(txt):
    print(linha())
    print(f"{txt.center(42)}")
    print(linha())
    return txt


def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    resp = leiaInt('\033[33m Sua resposta\033[m ')
    return resp




