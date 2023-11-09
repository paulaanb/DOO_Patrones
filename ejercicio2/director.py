from builder import PizzaBuilder

class Director:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construir_pizza(self):
        self.builder.reset()
        self.builder.construir_tipo_masa()
        self.builder.construir_salsa()
        self.builder.construir_ingredientes()
        self.builder.construir_tecnica_coccion()
        self.builder.construir_presentacion()
        self.builder.construir_maridaje()
        self.builder.construir_extras()
        self.builder.construir_tiempo_preparacion()
        self.builder.construir_precio_final()

    def obtener_pizza(self):
        return self.builder.obtener_pizza()
