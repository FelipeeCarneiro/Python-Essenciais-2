def validar(n):

#verificar se é int
    if n is not float:
        #verificar se é maior ou igual a 0
        if n >= 0 and n < 110000:
            # # print('Unicode encontrado!')
            # print('O caracter do code point: ',chr(n))
            # # print('Validação conlcuído.')
            return True
        else:
            print('Argumento inválido!')
            if n < 0:
                print('[ValueError] arg not in range(0-110000).\nNão pode ser um número negativo (0-110000).')
            if n > 110000:
                print('[ValueError] arg not in range(0-110000)')
            else:
                print('[TypeError] Code point inválido')

    else:
        if n == '':
            print('nenhum dado foi inserido')
            return None
        elif n == ' ' or n == '  ' or n == '   ':
            print('espaços não são dados válidos')
            return None
        else:
            print('Não é um número')
            return False

# validar(2910000)