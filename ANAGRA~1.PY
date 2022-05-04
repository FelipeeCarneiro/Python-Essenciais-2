#!/usr/bin/env python3
from time import sleep

# Essa é a maneira correta de chamar a função de um módulo em outra pasta.
from sys import path
path.append('/workspaces/62531000/Cursos Acervo/felipe/py/')    # anexando o caminho do módulo que limpará a tela
from modulos.clear import clear                                 # menos poluição visual
from modulos.precione_enter import press_enter                  # interaçãozinha kirrr
from modulos.bcolors import bcolors

def intro():
    print('''
        ______________________________________________________________________
        |---------------------        UM  ANAGRAMA        --------------------|
        |    Um anagrama é uma nova palavra formada pelo rearranjo das        |
        | letras de uma palavra, usando todas as letras originais exatamente  |
        | uma vez. Por exemplo, as frases “o bom programa” e “agarram o       |
        | pombo” são anagramas, enquanto “Eu sou” e “Você é” não são.         |
        |_____________________________________________________________________|

    ''')
#outra solução para o problema do anagrama utilizará o fato de que mesmo que txt_1 e txt_2 sejam diferentes,
#eles são anagramas somente se consistem exatament dos mesmo caracteres.

def pedir_textos():
    global txt_1, txt_2

    txt_1 = str(input('informe 1º texto: '))
    txt_2 = str(input('informe 2º texto: '))


def preparar_strings(s1, s2):
    global lista_1, lista_2

    # Então se começarmos ordenando cada string alfabericamente, de a a z, concluiremos com a mesma string se as
    # duas strings originais forem anagramas.
    lista_1 = list(s1)
    lista_2 = list(s2)

    # Em Python podemos utilizar o métoto sort em listas simplesmente convertendo cada string em uma lista.
    lista_1.sort()
    lista_2.sort()

def conferir(uma_lista_1, uma_lista_2, s1):
    posição = 0
    iguais = True
    while posição < len(s1) and iguais:
        if uma_lista_1[posição] == uma_lista_2[posição]:
            posição = posição + 1
        else:
            iguais = False
    return iguais

def main():

    clear()
    print(bcolors.ok)
    intro()
    sleep(2)

    print(bcolors.aviso)
    press_enter()
    print(bcolors.reset)

    clear()
    pedir_textos()
    preparar_strings(txt_1, txt_2)

    clear()

    print(f'Você informou "{txt_1}" e "{txt_2}.')

    if conferir(lista_1, lista_2, txt_1):
        print(f'\033[92m\tSÃO ',end='')

    else:
        print(f'\033\t[91mNÃO SÃO ',end='')

    print(f'ANAGRAMAS\033[0m')
    sleep(2)


continuar = True
txt_1 = "tem algo aqui"

while continuar:
    if txt_1 == '' or txt_1.isspace():
        print('\t+-----------------+\n\t|',end='')
        print(f'{bcolors.aviso}Você escolheu sair{bcolors.reset}',end='')
        print('|\n\t+-----------------+\n',end='')
        sleep(2)
        break

    else:
        main()
        press_enter()
        continue


#verifica se os textos introduzidos são anagramas e imprime o resultado.

