print('IMC = Indice de Massa Corporal ')
h = float(input('Digite sua altura [m] '))
m = float(input('Digite seu peso [kg] '))
r = m/h**2
if r < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso ideal '.format(r))
elif r >= 18.5 and r <= 24.9:
    print('Seu IMC é {:.2f} E você esta com o peso normal '.format(r))
elif r > 25 and r < 29:
    print('Seu IMC é {:.2f} e você é um gordo '.format(r))
elif r > 30:
    print('Tu vai morrer... ')



