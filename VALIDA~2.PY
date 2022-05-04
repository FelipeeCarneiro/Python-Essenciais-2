def validar(char):

#filtrar dados inválidos 1/2

        if char == '':

            print('tente espaço ao invez de dar enter apenas:')

            return False

        else:

#filtro de dados inválidos 2/2

            if len(char) > 1 :

                print('ord( ) só funciona um caraccter. tente outra vez.')

                return False

#execução final

            else:
                # print(ord(char))
                return True