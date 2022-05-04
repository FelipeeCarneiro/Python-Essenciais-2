'''Exceções: continuação
Como se tratam (em inglês, handle) as exceções? A palavra try é fundamental para a solução.

Além disso, também é uma keyword.

A receita para o sucesso é a seguinte:

primeiro, é preciso tentar fazer alguma coisa;
a seguir, tem de verificar se tudo correu bem.
Mas não seria melhor verificar primeiro todas as circunstâncias, e depois fazer algo apenas se for seguro?

Assim como o exemplo no editor.

Assumidamente, esta forma pode parecer a mais natural e compreensível, mas na realidade este método não torna a programação mais fácil. Todas estas verificações podem tornar o seu código inchado e ilegível.

O Python prefere uma abordagem completamente diferente.'''

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if second_number != 0:
    print(first_number / second_number)
else:
    print("This operation cannot be done.")

print("THE END.")
