print('Fucking Tabuada again ')
c = 1
num = 1
while True:
    num = int(input('Quer ver a tabuada de qual número? coloque 0 para finalizar '))
    if num == 0:
        break
    for c in range(1,11):
        print(f'{num} x {c} = {num*c} ')
        c += 1
print('FIM')
