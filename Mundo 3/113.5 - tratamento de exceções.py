try:
    #Operação
    a = int(input('Numerador '))
    b = int(input('Denominador '))
    r = a/b
except Exception as erro: # <- (ValueError, TypeError):
    #print('tivemos um erro no tipo de dados digitado')
    print(f'Infelizmente ocorreu um erro {erro.__class__}')
    #falhou

except ZeroDivisionError:
    print('Impossivel divisão por zero')
except KeyboardInterrupt:
    print('Sem digitação')

else:
    #Deu Certo
    print(r)
finally:
    #Certo/Falha
    print('Volte Sempre!')