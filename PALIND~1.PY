#!/usr/bin/env python3

# separando em blocos para evitar erros no python
def preparação():                                                   # preparar pra ter menos poluição visual
    from sys import path                                            # importando caminho do módulo sys
    path.append("/workspaces/62531000/Cursos Acervo/felipe/py/")    # anexando o caminho do módulo que limpará a tela
    from modulos.clear import clear, run, clear_alternativo         # importando as funções apontadas de sys.patha. Essa é a maneira correta de chamar a função de um módulo.
    clear()                                                         # finalmente invoca a função acima
preparação()                                                        #chama a função acima



# prepara uma apresentação
def intro():                                                                                        # explicar para o usuário o que o programa faz
    titulo = 'PROGRAMA VERIFICADOR DE PALÍNDROMO'                                                   # configura salvar um título
    div = '-'*len(titulo)+"--"                                                                      # configura imprimir uma linha tracejada do tamanho do título + 2 caracteres
    tab = '\n \t'                                                                                   # configura uma quebra de linha + recuo
    print('\t',tab,div)                                                                             # imprime quebra de linha + linha tracejada do tamanho do título
    print('\t',tab,'|',titulo.center(10),'|')                                                       # imprime o título no centro
    print('\t',tab,div)                                                                             # fecha o desenho do título imprimindo também uma quebra de linha + linha tracejada do tamanho do título
    print(tab,'\t É uma palavra que parece a mesma quando lida para,',tab,'a frente e para trás.',  # subtítulo e explicação do programa para usuário
    'Por exemplo, "rever" é um palíndromo,',tab,'enquanto "leal" não é.',tab)
intro()                                                                                             #chama a função acima


# Interação com o usuário
def frase(texto):                                                   # o usuário digita uma frase
    if texto == None:                                               # ignora esta merda, sem tempo pra tirar
        txt = str(input('digite uma frase: ')).strip(' ').upper()   # eliminei espaços antes e depois com strip (e capitalizei)
        palavras = txt.split()                                      # frase "splitadas" separadas cada palavra em uma lista/coleção
        junto = ''.join(palavras)                                   # eliminei os espaços internos da frase
    else:
        pass                                                        # sem tmepo de remover
    return junto                                                    # retorna as palavras grudadas e em capslock
# print('Você digitou a frase [{}]'.format(txt()))                  # chama e testa a função a cima



# varrendo a string de trás pra frente # essa função chama a anterior
def invertendo(frase):
    inverso = ''                                # iniciando a string, vazia no momento
    for letra in range(len(frase) - 1, -1, -1): # começa da última para a primeira letra, com passo de -1 (voltando uma letra por vez)
        inverso += frase[letra]                 # salva o resultado do for na variável
    return [frase,inverso]                       # imprime a variável
# print(invertendo(frase(None)))                  # inicia a função acima


#comparando frase invertida # essa função chama as anterioriores
def is_palindrome(frase_inversa):
    if frase_inversa[0] == frase_inversa[1]:# checa a comparação, se der certo..
        palindromo = True                   #... retorna True
    else:                                   # se não...
        palindromo = False                  # retorna False
    return palindromo                       # retorna o veredito
# print(is_palindrome(invertendo(frase(None))))  # descomente para testar o código acima


# montando as funções # esta função chama todas as outras acima
def app():
    if is_palindrome(invertendo(frase(None))):      # se forem iguais
        print('It\'s a palindrome')                 # imprime para o usuário que é um palíndromo
    else:                                           # se não..
        print('It\'s not a palindrome')             # imprime que não é palíndrome
app()                                               # roda a função acima


#módulo com testes
def testes():
    from dados_para_testes import lista                                                 # importa do módulo de testes

    for letra in range(1, len(lista), 1):                                               # um loop por todos as frases de exemplo
        txt = lista[letra].strip().upper()                                              # eliminei espaços antes e depois com strip (e capitalizei)
        palavras = txt.split()                                                          # frase "splitadas" separadas cada palavra em uma lista/coleção
        junto = ''.join(palavras)                                                       # eliminei os espaços internos da frase

        print(  '\nFrase[\033[32m',letra,'\033[m]:\t\033[32m',lista[letra],'\033[m',    # imprime o número da frase, a frase em si em cor verde lima
                '\nProcessada:\t',invertendo(junto)[0],                                 # imprime a frase processada sem espaços e em letras maiúsculas
                '\ninvertida:\t',invertendo(junto)[1],sep='',end='\n')                  # imprime a trase processada e invertida
        print('Veredito:\t'.format(),end='')                                            # imprime uma mensagem preparada para receber a próxima sem pular linha

        if is_palindrome(invertendo(junto)):                                            # se for palindrome...
            print('\033[34mIt''s a palindrome\033[m'.format(),end='\n')                 # imprime na tela de cor azul mensagem confirmando que é palindrome
        else:                                                                           # se não..
            print('\033[31mIt\'snt a palindrome\033[m',end='\n')                        # imprime na tela de cor vermelha, uma mensagem de contradição
# testes()                                                                                # esta função chama a porra toda. # desmarque se quiser testar com alguns exemplos