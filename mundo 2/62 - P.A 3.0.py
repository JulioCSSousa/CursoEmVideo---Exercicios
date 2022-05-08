print('Dez primeiros termos de uma p.a ')
p = int(input('Digite o primeiro termo '))
r = int(input('Qual a razão? '))
cont = 1
termo = p
total = 0
mais = 10
while mais !=0:
    total += mais
    while cont <= total:
        termo += r
        cont += 1
        print('{} '.format(termo), end='-> ')
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    print('Progressão finalizada com {} termos '.format(total))
print('FIM')