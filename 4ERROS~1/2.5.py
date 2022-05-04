'''Exceções: continuação
Veja o código no editor. Ajudá-lo-á a compreender este mecanismo.

Esta é o output que produz:

1
Oh dear, something went wrong...
3
output

Nota: a instrução print("2") foi perdida no processo.'''

try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")
