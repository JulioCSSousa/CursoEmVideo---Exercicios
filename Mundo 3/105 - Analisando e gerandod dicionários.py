#Exercício Python 105: Faça um programa que tenha uma função notas()
#que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)


def notas(*num,sit=False):
    """
    Função para calcular max, min, média e mostrar a situação [ruim,razoavel,boa] de uma turma
    :param num: notas a serem inseridas
    :param sit: situação da turma [True ou False] para aparecer
    :return: retorno em dicionário
    """
    soma = sum(num)
    media = soma / len(num)
    if soma/len(num) > 8:
        b = 'Boa'
        print('Situação Boa')
    elif 6 <= soma/len(num) <= 7:
        b = 'Razoavel'
    else:
        b = 'Ruim'
        print('Situação ruim! ')

    l = {'Total Inserido':len(num),'Nota maxima':max(num),'Nota minima':min(num),'Média da Turma':media,'Situação':b }
    if sit == False:
        del l['Situação']
    return l


resp = notas(5.5,5,7,8,0,sit=True)
help(notas)
