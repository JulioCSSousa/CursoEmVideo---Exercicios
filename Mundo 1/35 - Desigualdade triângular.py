print ('Informe o comprimento de 3 retas e veja se é possível formar um triângulo ')
a = float(input('Informe o lado A de um triângulo '))
b = float(input('Agora o lado B '))
c = float(input('Informe o lado C '))
if a < b+c and b < a+c and c < a+b:
    print('As retas informadas formam um triângulo! ')
else:
    print('As retas informadas não formam um triângulo ')