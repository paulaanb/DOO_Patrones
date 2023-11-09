from builders.builder import PizzaBuilder

class Director:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construir_pizza(self):
        self.builder.reset()
        self.builder.construir_tipo_masa()
        self.builder.construir_tipo_salsa()

        self.builder.construir_ingrediente("Ingrediente Principal", "Queso")
        self.builder.construir_ingrediente("Ingrediente Principal", "Tomate")

        self.builder.construir_tecnica_coccion("Horno Tradicional")
        self.builder.construir_presentacion("Clásica")
        self.builder.construir_maridaje("Vino Tinto")

        self.builder.construir_extra("Bordes Especiales")
        self.builder.construir_extra("Acabados con Trufas")

        self.builder.construir_entrega_domicilio()
        self.builder.construir_tiempo_precio_final()
