# Clase Pizza que actúa como el producto final
class Pizza:
    def __init__(self):
        self.tipo_masa = None
        self.salsa = None
        self.ingredientes = []
        self.tecnica_coccion = None
        self.presentacion = None
        self.maridaje = None
        self.extras = []
        self.tiempo_preparacion = None
        self.precio_final = None

# Interfaz Builder para construir la pizza
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def construir_tipo_masa(self):
        pass

    def construir_salsa(self):
        pass

    def construir_ingredientes(self):
        pass

    def construir_tecnica_coccion(self):
        pass

    def construir_presentacion(self):
        pass

    def construir_maridaje(self):
        pass

    def construir_extras(self):
        pass

    def obtener_pizza(self):
        return self.pizza

# Director que coordina la construcción de la pizza
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_pizza(self):
        self.builder.construir_tipo_masa()
        self.builder.construir_salsa()
        self.builder.construir_ingredientes()
        self.builder.construir_tecnica_coccion()
        self.builder.construir_presentacion()
        self.builder.construir_maridaje()
        self.builder.construir_extras()

# Builder concreto para la masa
class MasaBuilder(PizzaBuilder):
    def construir_tipo_masa(self):
        print("Elige el tipo de masa:")
        print("1. Masa Delgada")
        print("2. Masa Fermentada 48h")
        opcion = input("Ingresa el número de tu elección: ")

        if opcion == "1":
            self.pizza.tipo_masa = "Masa Delgada"
        elif opcion == "2":
            self.pizza.tipo_masa = "Masa Fermentada 48h"
        else:
            print("Opción no válida. Se seleccionará Masa Delgada por defecto.")
            self.pizza.tipo_masa = "Masa Delgada"


# Builder concreto para la salsa
class SalsaBuilder(PizzaBuilder):
    def construir_salsa(self):
        print("Elige el tipo de salsa:")
        print("1. Salsa Clásica")
        print("2. Salsa de Autor")
        opcion = input("Ingresa el número de tu elección: ")

        if opcion == "1":
            self.pizza.salsa = "Salsa Clásica"
        elif opcion == "2":
            self.pizza.salsa = "Salsa de Autor"
        else:
            print("Opción no válida. Se seleccionará Salsa Clásica por defecto.")
            self.pizza.salsa = "Salsa Clásica"


# Builder concreto para los ingredientes
class IngredientesBuilder(PizzaBuilder):
    def construir_ingredientes(self):
        print("Elige los ingredientes (separados por comas):")
        ingredientes_input = input("Ingresa los ingredientes: ")
        self.pizza.ingredientes = [ingrediente.strip() for ingrediente in ingredientes_input.split(",")]


# Builder concreto para la técnica de cocción
class TecnicaCoccionBuilder(PizzaBuilder):
    def construir_tecnica_coccion(self):
        print("Elige la técnica de cocción:")
        print("1. Horno Tradicional")
        print("2. Cocina Molecular")
        opcion = input("Ingresa el número de tu elección: ")

        if opcion == "1":
            self.pizza.tecnica_coccion = "Horno Tradicional"
        elif opcion == "2":
            self.pizza.tecnica_coccion = "Cocina Molecular"
        else:
            print("Opción no válida. Se seleccionará Horno Tradicional por defecto.")
            self.pizza.tecnica_coccion = "Horno Tradicional"


# Builder concreto para la presentación
class PresentacionBuilder(PizzaBuilder):
    def construir_presentacion(self):
        print("Elige la presentación:")
        print("1. Estilo Clásico")
        print("2. Obra de Arte")
        opcion = input("Ingresa el número de tu elección: ")

        if opcion == "1":
            self.pizza.presentacion = "Estilo Clásico"
        elif opcion == "2":
            self.pizza.presentacion = "Obra de Arte"
        else:
            print("Opción no válida. Se seleccionará Estilo Clásico por defecto.")
            self.pizza.presentacion = "Estilo Clásico"


# Builder concreto para el maridaje
class MaridajeBuilder(PizzaBuilder):
    def construir_maridaje(self):
        print("Elige el maridaje:")
        print("1. Vino Tinto")
        print("2. Cerveza Artesanal")
        opcion = input("Ingresa el número de tu elección: ")

        if opcion == "1":
            self.pizza.maridaje = "Vino Tinto"
        elif opcion == "2":
            self.pizza.maridaje = "Cerveza Artesanal"
        else:
            print("Opción no válida. Se seleccionará Vino Tinto por defecto.")
            self.pizza.maridaje = "Vino Tinto"


# Builder concreto para los extras y finalizaciones
class ExtrasBuilder(PizzaBuilder):
    def construir_extras(self):
        print("Elige los extras (separados por comas):")
        extras_input = input("Ingresa los extras: ")
        self.pizza.extras = [extra.strip() for extra in extras_input.split(",")]


# Builder concreto para la entrega a domicilio
class EntregaDomicilioBuilder(PizzaBuilder):
    def construir_entrega_domicilio(self):
        print("¿Deseas entrega a domicilio? (Sí/No): ")
        opcion = input().lower()
        self.pizza.entrega_domicilio = opcion == "si"

    def construir_monto_minimo_pedido(self):
        if self.pizza.entrega_domicilio:
            print("Ingresa el monto mínimo de pedido para entrega a domicilio:")
            monto_minimo = float(input())
            self.pizza.monto_minimo_pedido = monto_minimo

    def construir_costo_entrega(self):
        if self.pizza.entrega_domicilio:
            print("Ingresa la distancia en kilómetros para calcular el costo de entrega:")
            distancia = float(input())
            self.pizza.costo_entrega = distancia * 0.5  # Ejemplo: $0.50 por cada km


# Builder concreto para el tiempo de preparación y el precio final
class TiempoPrecioBuilder(PizzaBuilder):
    def construir_tiempo_preparacion(self):
        tiempo_base = 15  # minutos
        tiempo_adicional = 0

        if "Masa Fermentada 48h" in self.pizza.tipo_masa:
            tiempo_adicional += 10  # Ejemplo: 10 minutos adicionales para masa fermentada

        if "Cocina Molecular" in self.pizza.tecnica_coccion:
            tiempo_adicional += 5  # Ejemplo: 5 minutos adicionales para cocción molecular

        self.pizza.tiempo_preparacion = tiempo_base + tiempo_adicional

    def construir_precio_final(self):
        precio_base = 10.0  # Precio base de la pizza

        if "Ingredientes Importados" in self.pizza.ingredientes:
            precio_base += 5.0  # Ejemplo: $5.0 adicionales por ingredientes importados

        if "Acabado con Trufas" in self.pizza.extras:
            precio_base += 8.0  # Ejemplo: $8.0 adicionales por acabado con trufas

        if hasattr(self.pizza, 'entrega_domicilio') and self.pizza.entrega_domicilio:
            precio_base += self.pizza.costo_entrega  # Sumar el costo de entrega

        self.pizza.precio_final = precio_base


# Actualizamos el Cliente para utilizar el nuevo builder
class Cliente:
    def construir_pizza_personalizada(self, director):
        builder = MasaBuilder()
        director.builder = builder
        director.construir_pizza()

        # Ahora, utilizamos el nuevo builder para calcular el tiempo de preparación y el precio final
        tiempo_precio_builder = TiempoPrecioBuilder()
        director.builder = tiempo_precio_builder
        director.construir_pizza()

        pizza = tiempo_precio_builder.obtener_pizza()
        return pizza

# Ejemplo de uso
if __name__ == "__main__":
    director = Director(MasaBuilder())
    cliente = Cliente()
    pizza_personalizada = cliente.construir_pizza_personalizada(director)

    # Mostrar la pizza personalizada con detalles como tipo de masa, salsa, etc.
    print("Pizza Personalizada:")
    print(f"Tipo de Masa: {pizza_personalizada.tipo_masa}")
    print(f"Salsa: {pizza_personalizada.salsa}")
    print(f"Ingredientes: {pizza_personalizada.ingredientes}")
    print(f"Técnica de Cocción: {pizza_personalizada.tecnica_coccion}")
    print(f"Presentación: {pizza_personalizada.presentacion}")
    print(f"Maridaje: {pizza_personalizada.maridaje}")
    print(f"Extras: {pizza_personalizada.extras}")
    print(f"Tiempo de Preparación: {pizza_personalizada.tiempo_preparacion} minutos")
    print(f"Precio Final: ${pizza_personalizada.precio_final}")
