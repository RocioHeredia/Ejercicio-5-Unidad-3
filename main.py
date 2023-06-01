from ClassMicoleccion import Mi_coleccion


if __name__ == '__main__':
    coleccion = Mi_coleccion()

    # Inserta elementos a la coleccion
    try:
        coleccion.insertar_elemento(4, 0)  # Insertamos un elemento
    except ValueError as e:
        print(f'Error:{e}')
    # Agregar elementos a la coleccion
    coleccion.agregar_elemento(10)  # Agregamos un nuevo elemento

    # Mostrar elementos
    try:
        elemento = coleccion.mostrar_elemento(1)  # Obtenemos el elemento en la posición 2
        print(elemento)  # Se imprime el valor
    except ValueError as e:
        print(f'Error:{e}')

