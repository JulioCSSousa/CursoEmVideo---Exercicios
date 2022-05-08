ti = 0
contid = 0
si = 0
somaid = 0
maiorid = 0
menorid = 0
nome1 = str
nome2 = str
maioridadeh = 0
nomevelho = ''
m = 'masculino '
f = 'feminino '
for c in range(1,3):
    print('{}ª pessoa '.format(c))
    n = str(input('Entre com o nome ')).capitalize()
    i = int(input('Qual a idade? '))
    s = str(input('Qual o sexo? [m/f] ')).lower()
    contid += 1
    somaid += i
    if c == 1 and s == m:
        maioridh = i
        nomevelho = n
        #menorid = i
        #nome1 = n
        #nome2 = n
    if s == m and i > maioridadeh:
        maioridadeh = i
        nomevelho = n
    else:
        if i > maiorid:
            maiorid = i
            nome1 = n
        if i < menorid:
            menorid = i
            nome2 = n


media = somaid/contid

print('A media das idade do grupo é {} '.format(media))
print('A maior idade é de {} anos e o nome é {} '.format(maiorid,nome1,))
print('A menor idade é de {} anos e o nomé é {} '.format(menorid,nome2,))
print('O homem mais velho é ')