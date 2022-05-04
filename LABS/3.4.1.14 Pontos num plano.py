import math

# é chamada Point
# todas as propriedades devem ser privadas;
class Point:
    def __init__(self, x=0.0, y=0.0): # aceita dois argumentos (x e y respetivamente), ambos a zero
        self.__x = x
        self.__y = y

# devolve  coordenadas x
    def getx(self):
        return self.__x

 # devolve  coordenadas y
    def gety(self):
        return self.__y

# calcula e devolve a distância entre o ponto armazenado dentro do objeto e o outro ponto dado como um par de floats
    def distance_from_xy(self, x, y):
         return math.hypot(abs(self.__x - x), abs(self.__y - y))

# que calcula a distância (como o método anterior), mas a localização do outro ponto é dada como outro Ponto objeto de classe
    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
'''LAB
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        #
        # Write code here
        #

    def getx(self):
        #
        # Write code here
        #

    def gety(self):
        #
        # Write code here
        #

    def distance_from_xy(self, x, y):
        #
        # Write code here
        #

    def distance_from_point(self, point):
        #
        # Write code here
        #


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
----------------------------------------------------------------
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        #
        # Write code here
        #

    def getx(self):
        #
        # Write code here
        #

    def gety(self):
        #
        # Write code here
        #

    def distance_from_xy(self, x, y):
        #
        # Write code here
        #

    def distance_from_point(self, point):
        #
        # Write code here
        #


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

'''