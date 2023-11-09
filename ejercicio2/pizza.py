class Pizza:
    def __init__(self):
        self.tipo_masa = ""
        self.salsa = ""
        self.ingredientes = []
        self.tecnica_coccion = ""
        self.presentacion = ""
        self.maridaje = ""
        self.extras = []
        self.tiempo_preparacion = 0
        self.precio_final = 0.0

    def __str__(self):
        return (
            f"Tipo de Masa: {self.tipo_masa}\n"
            f"Salsa: {self.salsa}\n"
            f"Ingredientes: {', '.join(self.ingredientes)}\n"
            f"Técnica de Cocción: {self.tecnica_coccion}\n"
            f"Presentación: {self.presentacion}\n"
            f"Maridaje: {self.maridaje}\n"
            f"Extras: {', '.join(self.extras)}\n"
            f"Tiempo de Preparación: {self.tiempo_preparacion} minutos\n"
            f"Precio Final: ${self.precio_final}"
        )
