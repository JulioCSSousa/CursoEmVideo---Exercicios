def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('Digite um número válido!')
            continue
        except (KeyboardInterrupt):
            print('Interrompido pelo usuario ')
            return 0
        else:
            return n

def leiafloat(fl):
    while True:
        try:
            f = float(input(fl))
        except (ValueError,TypeError):
            print('Digite um numero real valido! ')
            continue
        except KeyboardInterrupt:
            print('Interrompido pelo usuario ')
            break
        else:
            return f


n = leiaInt('Digite um número inteiro ')
print(f'Você digitou {n}')

f = leiafloat('Digite um número real ')
print(f'Voce digitou {f}')