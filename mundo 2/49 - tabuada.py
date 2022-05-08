n = int (input('Enter with a number '))
print ('A tabuada de ', n, 'é: ')
for i in range (1, 11):
  print ('{} x {} = {}'.format(n, i, n*i))