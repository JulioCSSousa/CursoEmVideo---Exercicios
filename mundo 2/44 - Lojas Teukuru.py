print('{:=^40}'.format('lOJAS TEUKURU'))
p = float(input('Insira o preço do produto '))
print('''[1] À vista dinheiro (10% desconto)
[2] À vista cartão (5% desconto)
[3] Duas vezes 
[4] Três vezes ou mais (20% juros)''')
f = int(input('insira a forma de pagamento '))
if f == 1:
    print('O valor a pagar é de {:.2f}'.format (p-(p*0.1)))
elif f == 2:
    print('O valor a pagar é de {:2f} '.format(p-(p*0.05)))
elif f == 3:
    print('O valor a pagar é de {:.2f} com duas parcelas de {} '.format(p,p/2))
elif f == 4:
    f2= int(input('''Informe quantas vezes 
    [3],[4],[5],[6],[7] '''))
    print('O valor total a pagar é de {:.2f} com percelas de {:.2f} mensais '.format(p+(p*0.2),(p+(p*0.2))/f2))