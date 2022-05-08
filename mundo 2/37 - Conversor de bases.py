print('Base Conversor ')
n = int(input('Enter with a entire number '))
l = ['1 Binary, 2 octagonal, 3 hexadecimal ']
for item in range(len(l)):
    print(l[item])
c = int(input('Chose the convertion '))
if c == 1:
    print('The binary convertion of {} is {} '.format(n, bin(n)))
elif c == 2:
    print('The octagonal convertion of {} is {} '.format(n, oct(n)))
elif c == 3:
    print('The exadecimal convertion of {} is {} '.format(n, hex(n)))
else:
    print('Invalid number ')
while c != 1 or c != 2 or c != 3:
    print('Base Conversor ')
    n = int(input('Enter with a entire number '))
    l = ['1 Binary, 2 octagonal, 3 hexadecimal ']
    for item in range(len(l)):
        print(l[item])
    c = int(input('Chose the convertion '))
    if c == 1:
        print('The binary convertion of {} is {} '.format(n, bin(n)))
    elif c == 2:
        print('The octagonal convertion of {} is {} '.format(n, oct(n)))
    elif c == 3:
        print('The exadecimal convertion of {} is {} '.format(n, hex(n)))
    else:
        print('Invalid number ')
