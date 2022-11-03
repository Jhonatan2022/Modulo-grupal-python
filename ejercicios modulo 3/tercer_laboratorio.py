#Trabajo realizado por jhonattan florez y deivid bautista

#Ficha: 2470031

#Cada punto ubicado en el plano puede describirse como un
#par de coordenadas habitualmente llamadas x y y. Queremos
#que escribas una clase en Python que almacene ambas coordenadas
#como números flotantes. Además, queremos que los objetos de
#esta clase evalúen las distancias entre cualquiera de los dos
#puntos situados en el plano.

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distancia_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distancia_point(self, point):
        return self.distancia_xy(point.getx(), point.gety())


punto1 = Point(0, 0)
punto2 = Point(1, 1)
print(punto1.distancia_point(punto2))
print(punto2.distancia_xy(2, 0))