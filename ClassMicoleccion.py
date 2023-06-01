from zope.interface import implementer
from ClassInterfaz import Coleccion

@implementer(Coleccion)
class Mi_coleccion:
    def __init__(self):
        self.__Lista = []

    def insertar_elemento(self, elemento, posicion):
        if posicion < 0 or posicion > len(self.__Lista):
            raise ValueError('La posición es Invalida')
        self.__Lista.insert(posicion, elemento)

    def agregar_elemento(self, elemento):
        self.__Lista.append(elemento)

    def mostrar_elemento(self, posicion):
        if posicion < 0 or posicion >= len(self.__Lista):
            raise ValueError('Posición Invalida')
        return self.__Lista[posicion]
