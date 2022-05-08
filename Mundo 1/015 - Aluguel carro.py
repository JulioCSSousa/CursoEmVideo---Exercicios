k = float(input('Quantos km rodados? '))
d = int(input('Quantos dias o carro foi alugado? [coloque numeros inteiros] '))
t = (d*60+k*0.15)
print('O valor total a pagar é de {} reais '.format(t))