'''
Exceções: continuação
Vamos estragar o código mais uma vez.

Olhe para o programa no editor. Desta vez, retirámos o ramo não nomeado.

O utilizador insere 0 mais uma vez, e:

a exceção levantada não será tratada por ValueError - não tem nada a ver com isso;
uma vez que não há outro ramo, deve ver esta mensagem:

Traceback (most recent call last):
File "exc.py", line 3, in
y = 1 / x
ZeroDivisionError: division by zero
output


Aprendeu bastante sobre o tratamento de exceções em Python. Na secção seguinte, centrar-nos-emos nas exceções incorporadas em Python e nas suas hierarquias.


'''
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")

print("THE END.")

