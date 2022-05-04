'''
Exceções: continuação
Veja o código no editor. A nossa solução está lá.

O código, quando executado, produz uma das quatro variantes de output seguintes:

se introduzir um valor inteiro válido, não nulo (por exemplo 5) diz:

0.2
THE END.
output

se introduzir 0, diz:

You cannot divide by zero, sorry.
THE END.
output

se introduzir qualquer string não inteira, verá:

You must enter an integer value.
THE END.
output

(localmente na sua máquina) se premir Ctrl-C enquanto o programa aguarda a entrada do utilizador (o que provoca uma exceção chamada KeyboardInterrupt), o programa diz:

Oh dear, something went wrong...
THE END.
output
'''
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")
