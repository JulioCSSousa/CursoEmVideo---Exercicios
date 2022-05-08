print('-'*10, 'Cadastro de dados ', '-'*10)
e = 'S' or 'N'
maior = 0
masc = 0
fem = 0
while True:
    idade = int(input('Entre com a idade '))
    sexo = str(input('Entre com o sexo [M/F] ')).strip().upper()
    while sexo not in 'FM':
        sexo = str(input('Resposta inválida! Entre com o sexo [M/F] ')).strip().upper()
    print('-'*30)
    if idade > 18:
        maior += 1
    if sexo in 'Mm':
        masc += 1
    if sexo in 'Ff' and idade < 20:
        fem += 1
    e = str(input('Deseja continuar? [S/N] ')).strip().upper()
    print('-'*30)
    while e not in 'SN':
        e = str(input('Resposta invalida! Deseja continuar? [S/N] ')).strip().upper()
    if e == 'N':
        break
if fem > 1 and masc > 1 and maior > 1:
    m = 'mulheres'
    h = 'homens'
    p = 'pessoas'
    f = 'foram'
    c = 'cadastradas'
    cm = 'cadastrados'
else:
    m = 'mulher'
    h = 'homem'
    p = 'pessoa'
    f = 'foi'
    c = 'cadastrada'
    cm = 'cadastrado'
print('Dados gerais ')
print('-'*30)
print(f'''{maior} {p} com mais de 18 anos {f} {c}
{masc} {h} {f} {cm}
{fem} {m} com menos de 20 anos {f} {c} ''')
