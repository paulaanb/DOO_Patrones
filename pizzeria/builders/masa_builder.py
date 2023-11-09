from builders.builder import PizzaBuilder

class MasaBuilder(PizzaBuilder):
    def construir_tipo_masa(self):
        self.pizza.tipo_masa = "Masa Delgada"

    def construir_tipo_salsa(self):
        self.pizza.tipo_salsa = "Salsa Clásica"

    def construir_ingrediente(self, categoria, nombre):
        self.pizza.ingredientes.append({"categoria": categoria, "nombre": nombre})

    def construir_tecnica_coccion(self, tecnica):
        self.pizza.tecnica_coccion = tecnica

    def construir_presentacion(self, estilo):
        self.pizza.presentacion = estilo

    def construir_maridaje(self, bebida):
        self.pizza.maridaje = bebida

    def construir_extra(self, extra):
        self.pizza.extras.append(extra)

    def construir_entrega_domicilio(self):
        self.pizza.entrega_domicilio = True

    def construir_tiempo_precio_final(self):
        self.pizza.tiempo_preparacion = "30 minutos"
        self.pizza.precio_final = "$15.00"
