print('\033[0;35M VOCÊ GANHOU UM AUMENTO! VERIFIQUE O VALOR ')
s = float(input('Digite o valor do seu salário atual '))
if s <= 1250:
    print('\033[0;32mVocê recebeu 15% de aumento e seu salário agora passa a ser R${} '.format(s*0.15+s))
else:
    print('\033[0;32mVoce recebeu um aumento de 10% e seu salário passa a ser R${} '.format(s*0.1+s))