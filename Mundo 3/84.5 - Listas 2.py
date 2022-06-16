print('Listas dentro de listas')

#criou uma lista com dados de pessoas
dados = list()
dados.append('pedro')
dados.append(25)

totalpessoas = list()
totalpessoas.append(dados[:])
#se eu tentar incluir maria
dados[0] = 'Maria'
dados[1] = 21
totalpessoas.append(dados[:])
# cria-se dois cadastros, uma em cada lista
#para que isso não ocorra adciona-se [:] nos dois append criando copias das listas
print(totalpessoas)

registro = []
galera = []
for p in range(0,3):
    registro.append(str(input('Entre com um nome ')))
    registro.append((int(input('Qual a idade? '))))
    galera.append(registro[:])
    registro.clear()
print(galera)

for c in galera:
    if c[1] >= 18:
        print(f'{c[0]} é maior de idade ')
    else:
        print(f'{c[0]} não é maior de idade')
    if c[1] > 80:
        print('Ta com o pé na cova')
