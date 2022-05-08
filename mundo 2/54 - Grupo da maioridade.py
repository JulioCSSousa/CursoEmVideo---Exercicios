from datetime import date
y = date.today().year
i = int
tmaior = 0
tmenor = 0
for c in range(1,8):
    a = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    i = y-a
    if i >= 21:
        tmaior += 1
    else:
        tmenor += 1
print('O numero total de pessoas maiores de idade é {} '
      'e de pessoas menores é {} '.format(tmaior,tmenor
                                          ))



