class Pizza:
    def __init__(self):
        self.tipo_masa = ""
        self.tipo_salsa = ""
        self.ingredientes = []
        self.tecnica_coccion = ""
        self.presentacion = ""
        self.maridaje = ""
        self.extras = []
        self.entrega_domicilio = False
        self.tiempo_preparacion = ""
        self.precio_final = ""

    def __str__(self):
        return (
            f"Tipo de Masa: {self.tipo_masa}\n"
            f"Tipo de Salsa: {self.tipo_salsa}\n"
            f"Ingredientes: {', '.join([ingrediente['nombre'] for ingrediente in self.ingredientes])}\n"
            f"Técnica de Cocción: {self.tecnica_coccion}\n"
            f"Presentación: {self.presentacion}\n"
            f"Maridaje: {self.maridaje}\n"
            f"Extras: {', '.join(self.extras)}\n"
            f"Entrega a Domicilio: {'Sí' if self.entrega_domicilio else 'No'}\n"
            f"Tiempo de Preparación: {self.tiempo_preparacion}\n"
            f"Precio Final: {self.precio_final}"
        )
