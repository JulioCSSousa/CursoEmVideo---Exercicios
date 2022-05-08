print('temperature Convertor ')
print('='*40)
keep = ''
r = r2 = 0
while keep in 'Yy':
    print('1 Celsius, 2 fahrenheit, 3 Kelvin')
    r = int(input('Choose the temperature do you wanna convert? '))
    while r not in (1, 2, 3):
        r = int(input('Choose the temperature do you wanna convert? Try Again '))
    t1 = float(input('What is the temperature? '))
    print('1 Celsius, 2 fahrenheit, 3 Kelvin')
    r2 = int(input('What temperature do you wanna go to? '))
    while r2 not in (1,2,3):
        r2 = int(input('What temperature do you wanna go to? Try again '))
    if r == 1 and r2 == 2:
        c = (t1 * (9 /5) + 32)
        print(f'The temperature is {c:.2f} farenheit ')
    elif r == 1 and r2 == 3:
        c2 = (t1 + 273)
        print(f'The temperature is {c2:.2f} Kelvin ')
    elif r == 2 and r2 == 1:
        c3 = (t1 - 32)*(5/9)
        print(f'The temperature is {c3:.2f} Celsius ')
    elif r == 2 and r2 == 3:
        c4 = (5 * (t1 - 32) / 9 + 273)
        print(f'The temperature is {c4:.2f} Kelvin ')
    elif r == 3 and r2 == 1:
        c5 = (t1 - 273)
        print(f'The temperature is {c5:.2f} Celsius ')
    else:
        if r == 3 and r2 == 2:
            c6 = (9 / 5 * (t1 - 273) + 32)
            print(f'The temperature is {c6:.2f} Farenheit ')
    keep = str(input('Do you wanna again? [Y/N] '))
    while keep not in 'YyNn':
        keep = str(input('Invalid anwser! Do you wanna run the program again? [Y/N] '))
    while keep in 'Nn':
        break
print('Thank you! come again')
