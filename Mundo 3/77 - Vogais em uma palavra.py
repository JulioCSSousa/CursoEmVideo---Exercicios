palavras = ('variavel', 'desenvolvedor', 'softwares', 'cursoemvidep', 'python')
for c in palavras:
    print(f'\nNa palavras {c} temos ', end = '')
    for letra in c:
        if letra in 'a e i o u':
            print(letra, end='')