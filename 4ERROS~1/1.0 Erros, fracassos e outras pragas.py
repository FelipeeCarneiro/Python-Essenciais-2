import math

x = float(input("Enter x: "))
y = math.sqrt(x)

print("The square root of", x, "equals to", y)


'''Erros, fracassos e outras pragas
Qualquer coisa que possa correr mal, irá correr mal.

Esta é a lei de Murphy, e funciona em todo o lado e sempre. A execução do seu código também pode correr mal. Se puder, irá.

Veja o código no editor. Há pelo menos duas formas possíveis de "correr mal". Consegue vê-las?

Como um utilizador é capaz de introduzir uma string completamente arbitrária, não há garantia de que a string possa ser convertida num valor float - esta é a primeira vulnerabilidade do código;
a segundo é que a função sqrt() falha se obtiver um argumento negativo.
Poderá receber uma das seguintes mensagens de erro.

Algo assim:

Enter x: Abracadabra

Traceback (most recent call last):

  File "sqrt.py", line 3, in <module>

    x = float(input("Enter x: "))

ValueError: could not convert string to float: 'Abracadabra'
output

Ou algo assim:

Enter x: -1

Traceback (most recent call last):

  File "sqrt.py", line 4, in <module>

    y = math.sqrt(x)

ValueError: math domain error
output

Pode proteger-se de tais surpresas? Claro que pode. Além disso, tem de o fazer para ser considerado um bom programador.'''