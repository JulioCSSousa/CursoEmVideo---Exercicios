print('VIAGENS' )
km = float(input('Entre com a distância da viagem em km '))
if km <= 200:
    print('O valor da viagem será R${:.2f} '.format(0.5*km))
else:
    print('O valor da viagem será R${:.2f} '.format(0.45*km))
