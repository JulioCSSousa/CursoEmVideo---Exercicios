#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
pilha = []
op = str(input('''Entre com uma expresão algébrica que use parênteses, que vou verificar se existem parênteses em aberto.
É eu sei... Sou um programa inútil '''))
for simb in op:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta correta')
else:
    print('Sua expressão esta errada')

#Questao dificil! demorei e nao conegui sem ajuda

