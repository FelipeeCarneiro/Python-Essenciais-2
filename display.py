import dadosTeste
# escrever um programa que seja capaz de simular o trabalho de um dispositivo de seven-display, embora vá utilizar LEDs individuais em vez de segmentos.

#  plano
# Cada dígito é construído a partir de 13 LEDs (uns iluminados, outros escuros, é claro)
# Nota: o número 8 mostra todas as luzes LED acesas.
# usar uma lista contendo padrões de todos os dez dígitos pode ser muito útil.
dicionário = {

    '0': (  '###',
            '# #',
            '# #',
            '# #',
            '###'),

    '1': (  '  #',
            '  #',
            '  #',
            '  #',
            '  #'),

    '2': (  '###',
            '  #',
            '###',
            '#  ',
            '###'),

    '3': (  '###',
            '  #',
            '###',
            '  #',
            '###'),

    '4': (  '# #',
            '# #',
            '###',
            '  #',
            '  #'),

    '5': (  '###',
            '#  ',
            '###',
            '  #',
            '###'),

    '6': (  '###',
            '#  ',
            '###',
            '# #',
            '###'),

    '7': (  '###',
            '  #',
            '  #',
            '  #',
            '  #'),

    '8': (  '###',
            '# #',
            '###',
            '# #',
            '###'),

    '9': (  '###',
            '# #',
            '###',
            '  #',
            '###'),

    '.': (  '   ',
            '   ',
            '   ',
            '   ',
            '  #'),
}

def led(num):
        for índice in range(5):
                digitos = [dicionário[digitos] for digitos in str(num)]
                print("   ".join(segment[índice] for segment in digitos))


def teste():
        for i in dadosTeste.lst:
                print('\n')
                led(i)

from os import system

while True:

# O seu código tem de fazer um display de qualquer número inteiro não negativo inserido pelo utilizador.
        número = input("\nPor obséquio, insira um número real: ")

        if not número.isnumeric():

                sair = input('desaja sair [s/n]?')

                if sair == 's':

                        system("clear")

                        exit('Saindo. Obrigado!')

                elif sair in ['n','não','Não','N','NÃO']:

                        print('\n'*50,'Exemplo\n')

                        número = 12.3

                else:

                        system("clear")

                        print('resposta inválida, voltando...\nExemplo de resposta:\n')

                        número = 12.3




        led(número)


#fim do app
