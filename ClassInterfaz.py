from zope.interface import Interface

class Coleccion(Interface):
    def insertar_elemento(self, elemento, posicion):
        pass

    def agregar_elemento(self, elemento):
        pass

    def mostrar_elemento(self, posicion):
        pass
