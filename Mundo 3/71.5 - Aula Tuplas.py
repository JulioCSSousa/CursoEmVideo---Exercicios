lanche = ('hamburguer', 'suco,', 'pizza', 'batata')
print(lanche[1]) #1,2, -1 -2 1:4
for cont in range(0, len(lanche)): #Essa maneira mostra a posição
    print(f'Eu vou comer {lanche[cont]}')
for comida in lanche: # para numero usar enumerate e colocar duas posições
    print(f'Vou comer {comida}')
print(sorted(lanche))
a = (5,2,1)
b = (4,6,8,7)
c = a+b
print(len(c))
print(c.count[5]) #quantas vezes aparece o numero em questao
print(c.index[2]) #mostra a posição