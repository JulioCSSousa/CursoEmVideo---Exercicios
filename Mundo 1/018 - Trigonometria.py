import math
a=float(input('Digite um valor em graus '))
r=(math.radians(a))
s=(math.sin(r))
c=(math.cos(r))
t=(math.tan(r))
print('O seno de {} é {:.2f} '.format(a,s))
print('O cosseno de {} é {:.2f} '.format(a,c))
print('A tagente de {} é {:2f} '. format(a,t))