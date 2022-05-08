a = str(input('Digite o nome do primeiro aluno '))
b = str(input('Nome do segundo aluno '))
c = str(input('Do terceiro '))
d = str(input('Do quarto '))
l = [a,b,c,d]
from random import choice
e = choice(l)
print('O aluno escolhido foi: {} '.format(e))