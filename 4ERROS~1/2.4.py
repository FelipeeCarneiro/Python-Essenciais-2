'''Exceções: continuação
Veja o código no editor. Esta é a abordagem favorita do Python.

Nota:

a keyword try inicia um bloco do código que pode ou não estar a funcionar corretamente;
a seguir, o Python tenta realizar a ação arriscada; se falhar, é levantada uma exceção e o Python começa a procurar por uma solução;
a keyword except inicia um pedaço de código que será executado se alguma coisa dentro do bloco try correr mal - se uma exceção é levantada dentro de um bloco try anterior, falhará aqui, pelo que o código localizado após a keyword except deverá fornecer uma reação adequada à exceção levantada;
retornar ao nível de nesting anterior termina a secção do try-except.
Execute o código e teste o seu comportamento.


Vamos resumir isto:

try:
    :
    :
except:
    :
    :


no primeiro passo, o Python tenta executar todas as instruções colocadas entre as try: e except: declarações;
se nada estiver errado com a execução e todas as instruções forem executadas com sucesso, a execução salta para o ponto após a última linha do bloco except: , e a execução do bloco é considerada completa;
se alguma coisa correr mal dentro do bloco try: e except: , a execução salta imediatamente para fora do bloco e para a primeira instrução localizada após a keyword except: ; isto significa que algumas das instruções do bloco podem ser silenciosamente omitidas.'''

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")

print("THE END.")
