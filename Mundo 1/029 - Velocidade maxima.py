print('MULTA DE TRÂNSITO ')
print('A velocidade máxima é de 80hm/h, o valor cobrado seráde 7 reais cada km excedido  ')
v = float(input('Entre com a velocidade do carro [km/h] '))
if v > 80:
    print('\033[0;31m Você foi multado! O preço a pagar e de {} '.format((v-80)*7))
else:
    print('\033[0;34m A velocidade corresponde à norma de trânsito ')