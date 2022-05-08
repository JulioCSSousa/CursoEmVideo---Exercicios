v=float(input('Digite o valor da casa de interesse '))
s=float(input('Digite o seu salário líquido '))
a=int(input('Fale em quantos anos deseja pagar '))
print('\033[1;31m Alertamos que se as parcelas mensais excederem 30% do seu salário, seu pedido será negado')
import time
time.sleep(3)
t=v/(a*12)
if t<=0.3*s:
    print('\033[1;33m Sua compra foi permitida e o valor das parcelas serão de R${:.2f} mensais '.format(t))
else:
    print('\033[1;31m Seu pedido foi negado! As parcelas são de R${:.2f} e excedem 30% do seu salário '.format(t))
