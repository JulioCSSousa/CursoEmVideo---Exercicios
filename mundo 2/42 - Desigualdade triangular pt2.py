# a = float(input('Informe a medida do lado A de um triângulo '))
# b = float(input('Informe o lado B '))
# c = float(input('informe o C '))
# if a < b+c and b < a+c and c < a+b and a != b and b == c or b != c and a == b or c == a and a != b:
#    print('Forma um triângulo e este triângulo e Isosceles, possui dois lados iguais ')
# elif a < b+c and b < a+c and c < a+b and a == b and b == c and c == a:
#    print('Forma um triângulo e este triâgulo é equilátero, todos lados são iguais ')
# elif a < b+c and b < a+c and c < a+b and a != b != c !=a:
#    print('Forma um triângulo e este triângulo e Escaleno, possui todos lados diferentes ')
##else:
#   a > b+c or b > a+c or c > a+b
#  print('As medidas não formam um triângulo ')

# Deixando a comparação do isosceles por ultimo pouparia muito as linhas de codigo

print('Informe o comprimento de 3 retas e veja se é possível formar um triângulo ')
a = float(input('Informe o lado A de um triângulo '))
b = float(input('Agora o lado B '))
c = float(input('Informe o lado C '))
if a < b + c and b < a + c and c < a + b:
    print('As retas informadas formam um triângulo! ')
    if a == b == c:
        print('Equilátero ')
    elif a != b != c != a: \
            print('Escaleno')
    else:
        print('Isosceles ')
else:
    print('As medidas não formam um triângulo ')
