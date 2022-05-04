import cores

def main(palavra, frase):
    achado = True
    inicio = 0
    for letra in palavra:
        pos = frase.find(letra, inicio)
        if pos < 0:
            achado = False
            break
        inicio = pos + 1
    if achado:
        return True
    else:
        return False

def aux(teste_a, teste_b):
    if main(teste_a, teste_b):
        print('Yes')
    else:
        print('No')

def testes():
    #dados para teste
    dados= ['donor','Nabucodonosor','donut','Nabucodonosor']
    res='Yes','No'
    for i in dados:
        if aux(dados[i],dados[i+1]) == res[0]:
            print('Pass.')
        elif aux(dados[i],dados[i+1]) == res[1]:
            Print('Not pass.')
        else:
            print('Erro do programa: Nenhuma resposta conhecida')

# teste_do_programa()
# find_a_word('donor','Nabucodonosor')
# find_a_word('donut','Nabucodonosor')
def main_app():
    palavra = str(input('informe uma palavra '))
    frase = str(input('informe uma frase '))

    if main(palavra,frase) == True:
        res = cores.GREEN + 'ESTÃO'
    else:
        res = cores.RED + 'NÃO ESTÃO'

    print(cores.BOLD,'Os carateres que compõem a palavra inserida', res + cores.BOLD ,'escondidos dentro da frase.',cores.RESET)

