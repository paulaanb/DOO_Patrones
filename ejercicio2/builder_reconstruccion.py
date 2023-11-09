from builder import PizzaBuilder

class BuilderReconstruccion(PizzaBuilder):
    def construir_tipo_masa(self):
        pass  # No es necesario para la reconstrucción

    def construir_salsa(self):
        pass  # No es necesario para la reconstrucción

    def construir_ingredientes(self):
        pass  # No es necesario para la reconstrucción

    def construir_tecnica_coccion(self):
        pass  # No es necesario para la reconstrucción

    def construir_presentacion(self):
        pass  # No es necesario para la reconstrucción

    def construir_maridaje(self):
        pass  # No es necesario para la reconstrucción

    def construir_extras(self):
        pass  # No es necesario para la reconstrucción

    def construir_tiempo_preparacion(self):
        self.pizza.tiempo_preparacion = int(self.datos["Tiempo de Preparación"])

    def construir_precio_final(self):
        self.pizza.precio_final = float(self.datos["Precio Final"])
