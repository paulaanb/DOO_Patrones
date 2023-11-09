from pizza import Pizza

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def reset(self):
        self.pizza = Pizza()

    def obtener_pizza(self):
        return self.pizza

    def construir_tipo_masa(self):
        pass

    def construir_tipo_salsa(self):
        pass

    def construir_ingrediente(self, categoria, nombre):
        pass

    def construir_tecnica_coccion(self, tecnica):
        pass

    def construir_presentacion(self, estilo):
        pass

    def construir_maridaje(self, bebida):
        pass

    def construir_extra(self, extra):
        pass

    def construir_entrega_domicilio(self):
        pass

    def construir_tiempo_precio_final(self):
        pass
