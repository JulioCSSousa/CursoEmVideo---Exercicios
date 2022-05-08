Listas pode, receber valores com o comando append()
append()
lista.insert(0,item a ser inserido) = insere um um valor entre os itens da lista
del lista[] = remove o conteudo
lista.pop() = mesma coisa, geralmente remove o ultimo valor
lista.remove('') = remove pelo indice
if item in lista:
    lista.remove(item) = remove o item caso eleestiver inserido na lista
criar uma lista
valores = list(range(4,11))
valores.sort() = organiza os valores
len.valores = conta os valores
num.sort(reverse = True) = coloca em ordem invertida
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor ')))
for c, v in enumerate(valores):
    print(f' Na posição {} encontrei o valor {} )
a [2,3,4,7]
b = a
as alterações mudarão as duas listas
a mao er q eu incluir:
b = a[:] = b receberá todos elementos de a criando uma cópia