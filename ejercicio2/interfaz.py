class InterfazUsuario:
    @staticmethod
    def mostrar_opciones(opciones):
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")

    @staticmethod
    def obtener_opcion(opciones):
        while True:
            try:
                seleccion = int(input("Ingresa el número de tu elección: "))
                if 1 <= seleccion <= len(opciones):
                    return seleccion
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
