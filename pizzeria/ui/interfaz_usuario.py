class InterfazUsuario:
    @staticmethod
    def mostrar_opciones(opciones):
        print("Opciones:")
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")

    @staticmethod
    def obtener_opcion(opciones, multiple=False):
        if multiple:
            print("Ingresa el número de tus elecciones separadas por comas:")
            elecciones = input().split(',')
            return [opciones[int(eleccion) - 1] for eleccion in elecciones]
        else:
            print("Ingresa el número de tu elección:")
            opcion = input()
            return opciones[int(opcion) - 1]

    @staticmethod
    def obtener_input(mensaje):
        print(mensaje)
        return input()
