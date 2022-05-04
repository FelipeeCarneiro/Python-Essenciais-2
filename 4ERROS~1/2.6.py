try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")

'''
Exceções: continuação
Esta abordagem tem uma desvantagem importante - se houver a possibilidade de mais do que uma exceção poder saltar para um ramo except: , poderá ter dificuldade em descobrir o que realmente aconteceu.

Tal como no nosso código no editor. Execute-o e veja o que acontece.

A mensagem: Oh dear, something went wrong... que aparece na consola nada diz sobre a razão, enquanto que existem duas causas possíveis para a exceção:

dados não inteiros inseridos pelo utilizador;
um valor inteiro igual a 0 atribuído à variável x .

Tecnicamente, existem duas maneiras de resolver o problema:

construir dois blocos consecutivos try-except , um para cada possível motivo de exceção (fácil, mas causará um crescimento do código desfavorável)
utilizar uma variante mais avançada da instrução.
É assim que se parece:

try:
    :
except exc1:
    :
except exc2:
    :
except:
    :


É assim que funciona:

se o ramo try levanta a exceção exc1 , será tratado pelo bloco except exc1: ;
da mesma forma, se o ramo try levanta a exceção exc2 , será tratado pelo bloco except exc2: ;
se o ramo try levanta qualquer outra exceção, será tratado pelo bloco não nomeado except .
Passemos à próxima parte do curso e vejamo-lo em ação.

'''