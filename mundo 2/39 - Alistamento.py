from datetime import date
y = date.today().year
print('\033[0;32mAlistamento Militar ')
n = int(input('Informe o ano de nascimento '))
i = (y-n)
print('Você tem {} anos '.format (i))
if i < 18:
    print('Faltam {} anos para se alistar '.format(18-i))
elif i > 18:
    print('Você já deveria ter se alistado há {} anos '.format(i-18))
else:
    print('Você se alista esse ano, corre filho da puta ')
