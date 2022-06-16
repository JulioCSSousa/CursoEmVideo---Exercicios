from random import randint as ran
def maior(*num):
    a = max(num)
    print(num)
    print(f'O maior número é {a} ')

maior(ran(0,100),ran(0,100),ran(0,100),ran(0,100),ran(0,100))