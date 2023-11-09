from builder import PizzaBuilder
from director import Director

class Cliente:
    def __init__(self, director: Director):
        self.director = director

    def construir_pizza_personalizada(self, builder: PizzaBuilder):
        self.director.builder = builder
        self.director.construir_pizza()
        return self.director.builder.obtener_pizza()
