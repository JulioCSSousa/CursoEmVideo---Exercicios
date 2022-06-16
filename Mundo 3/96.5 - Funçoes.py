#funções são rotinas que podem se torna repetitivas na programação
#def lin():
 #   print('-='*30)

#sem parametros
#lin()
#print('CADASTRO DE ALUNOS')
#lin()

#com parametros
#coisa q n se repetem podem ser incluidas como parametros

def lin2(linn):
    print('-='*30)
    print(linn)
    print('-='*30)


lin2('Cadastro de Alunos')
print()
lin2('Curso em video')


def soma(x,y):
    s = x + y
    print(s)


soma(4,5)
soma(y=5,x=5)

#empacotamento de parametro
def cont(*num):
    m = 0
    tot = len(num)
    print(f'recebi os numeros {num} ao total sao {tot} ')

    
cont(2,3,5,8,6,7)
cont(7,1,5,9)
cont(1,5,9,7,5,3)



#listas
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [1,5,9,7,5,3]
print(valores)
dobra(valores)
print('O dobro')
print(valores)