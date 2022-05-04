'''LAB

Tempo estimado
30-60 minutos

Nível de dificuldade
Fácil/Médio

Objetivos
melhorar as competências do aluno na definição das classes a partir do zero;
definir e utilizar variáveis de instância;
definir e utilizar métodos.
Cenário
Precisamos de uma classe capaz de contar segundos. Fácil? Não tanto quanto se possa pensar, pois vamos ter algumas expectativas específicas.

Leia-os cuidadosamente, pois a classe sobre a qual está a escrever será usada para lançar foguetes que realizam missões internacionais a Marte. É uma grande responsabilidade. Contamos consigo!

A sua classe será chamada Timer. O seu construtor aceita três argumentos representando horas (um valor a partir do intervalo [0...23] - vamos utilizar o tempo militar), minutos (a partir do intervalo [0...59]) e segundos (a partir do intervalo [0...59]).

Zero é o valor padrão para todos os parâmetros acima. Não há necessidade de efetuar quaisquer verificações de validação.

A própria classe deve fornecer as seguintes facilidades:

objetos da classe devem ser "imprimíveis", ou seja, devem ser capazes de se converter implicitamente em strings da seguinte forma: "hh:mm:ss", com zeros iniciais adicionados quando qualquer um dos valores for inferior a 10;
a classe deve ser equipada com métodos sem parâmetros chamados next_second() e previous_second(), incrementando o tempo armazenado dentro dos objetos em +1/-1 segundo, respetivamente.
Use as seguintes dicas:

todas as propriedades do objeto devem ser privadas;
considere escrever uma função separada (não um método!) para formatar a string de tempo.
Complete o template que lhe fornecemos no editor. Execute o seu código e verifique se o output tem o mesmo aspeto que o nosso.

Output esperado
23:59:59
00:00:00
23:59:59

###--

class Timer:
    def __init__( ??? ):
        #
        # Write code here
        #

    def __str__(self):
        #
        # Write code here
        #

    def next_second(self):
        #
        # Write code here
        #

    def prev_second(self):
        #
        # Write code here
        #


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
'''

# não utilizar um método, e sim uma função separada para formatar a string de tempo
def dois_digitos(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s

# A Classe começa aqui
class Timer:
# O seu construtor aceita três argumentos, zero é o valor padrão de todos
    def __init__(self, horas = 0, minutos = 0, segundos = 0):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos
# imprimir HH:MM:SS com zeros iniciais adicionados caso seja menor que 10 e não seja digitado
    def __str__(self):
        return  dois_digitos(self.__horas)  + ":" + \
                dois_digitos(self.__minutos)+ ":" +\
                dois_digitos(self.__segundos)
# incrementando o tempo armazenado dentro dos objetos em +1
    def next_second(self):
        self.__segundos += 1
        if self.__segundos > 59:
            self.__segundos = 0
            self.__minutos += 1
            if self.__minutos > 59:
                self.__minutos = 0
                self.__horas += 1
                if self.__horas > 23:
                    self.__horas = 0
# decrementando o tempo armazenado dentro dos objetos em -1
    def prev_second(self):
        self.__segundos -= 1
        if self.__segundos < 0:
                self.__segundos = 59
                self.__minutos -= 1
                if self.__minutos < 0:
                    self.__minutos = 59
                    self.__horas -= 1
                    if self.__horas < 0:
                        self.__horas = 23

# fim da classe


# template
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
# Output esperado do template
# 23:59:59
# 00:00:00
# 23:59:59