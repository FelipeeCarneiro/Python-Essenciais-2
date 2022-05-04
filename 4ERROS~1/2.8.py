'''Exceções: continuação
Não se esqueça:

os ramos except são pesquisados na mesma ordem em que aparecem no código;
não deve utilizar mais do que um, exceto um ramo com um certo nome de exceção;
o número de diferentes ramos except é arbitrário - a única condição é que se utilizar try, deve colocar pelo menos um except (nomeado ou não) depois dele;
a keyword except não deve ser utilizada sem um precedente try;
se algum dos ramos except for executado, nenhum outro ramo será visitado;
se nenhum dos ramos except especificados correspondem à exceção levantada, a exceção permanece sem ser tratada (discutiremos isso em breve)
se um não nomeado except ramo existir (um sem nome de exceção), tem de ser especificado como o último.
try:
    :
except exc1:
    :
except exc2:
    :
except:
    :


Vamos continuar as experiências agora.


Veja o código no editor. Modificámos o programa anterior - removemos o ramo ZeroDivisionError .

O que acontece agora se o utilizador introduzir 0 como um input?

Como não há ramos dedicados para divisão por zero, a exceção levantada cai no ramo geral (sem nome); isto significa que, neste caso, o programa dirá:

Oh dear, something went wrong...
THE END.
output

Experimente você mesmo. Execute o programa.'''

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")
except:
    print("\nOh dear, something went wrong...")

print("THE END.")
