#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
#aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use algumas dessas funções.

import moedas

num = float(input('Entre com um valor R$ '))
moedas.dobrar(num)
moedas.metade(num)
moedas.aumentar10(num)
moedas.diminuir10(num)
