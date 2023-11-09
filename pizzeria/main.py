from director import Director
from cliente import Cliente
from builders import MasaBuilder, MasaFermentadaBuilder
from ui import InterfazUsuario

if __name__ == "__main__":
    director = Director(MasaBuilder())
    cliente = Cliente(director)

    # Utilizamos la interfaz de usuario para la elección de la masa
    InterfazUsuario.mostrar_opciones(["Masa Delgada", "Masa Fermentada 48h"])
    opcion_masa = InterfazUsuario.obtener_opcion(["Masa Delgada", "Masa Fermentada 48h"])

    if opcion_masa == "Masa Delgada":
        director.builder = MasaBuilder()
    else:
        director.builder = MasaFermentadaBuilder()

    director.construir_pizza()

    # Elección de la salsa
    InterfazUsuario.mostrar_opciones(["Salsa Clásica", "Salsa de Autor", "Salsa Vegana", "Edición Limitada"])
    opcion_salsa = InterfazUsuario.obtener_opcion(["Salsa Clásica", "Salsa de Autor", "Salsa Vegana", "Edición Limitada"])

    if opcion_salsa == "Salsa Clásica":
        director.builder.construir_salsa_clasica()
    elif opcion_salsa == "Salsa de Autor":
        director.builder.construir_salsa_autor()
    elif opcion_salsa == "Salsa Vegana":
        director.builder.construir_salsa_vegana()
    elif opcion_salsa == "Edición Limitada":
        director.builder.construir_salsa_edicion_limitada()

    # Elección de ingredientes
    InterfazUsuario.mostrar_opciones(["Queso", "Tomate", "Pepperoni", "Champiñones", "Aceitunas"])
    opcion_ingredientes = InterfazUsuario.obtener_opcion(["Queso", "Tomate", "Pepperoni", "Champiñones", "Aceitunas"], multiple=True)

    for opcion in opcion_ingredientes:
        director.builder.construir_ingrediente("Ingrediente Principal", opcion)

    # Elección de la técnica de cocción
    InterfazUsuario.mostrar_opciones(["Horno Tradicional", "Cocción Molecular"])
    opcion_coccion = InterfazUsuario.obtener_opcion(["Horno Tradicional", "Cocción Molecular"])

    if opcion_coccion == "Horno Tradicional":
        director.builder.construir_tecnica_coccion("Horno Tradicional")
    elif opcion_coccion == "Cocción Molecular":
        director.builder.construir_tecnica_coccion("Cocción Molecular")

    # Elección de la presentación
    InterfazUsuario.mostrar_opciones(["Clásica", "Obras de Arte"])
    opcion_presentacion = InterfazUsuario.obtener_opcion(["Clásica", "Obras de Arte"])

    if opcion_presentacion == "Clásica":
        director.builder.construir_presentacion("Clásica")
    elif opcion_presentacion == "Obras de Arte":
        director.builder.construir_presentacion("Obras de Arte")

    # Elección del maridaje
    InterfazUsuario.mostrar_opciones(["Vino Tinto", "Cerveza Artesanal", "Cóctel de Frutas"])
    opcion_maridaje = InterfazUsuario.obtener_opcion(["Vino Tinto", "Cerveza Artesanal", "Cóctel de Frutas"])

    if opcion_maridaje == "Vino Tinto":
        director.builder.construir_maridaje("Vino Tinto")
    elif opcion_maridaje == "Cerveza Artesanal":
        director.builder.construir_maridaje("Cerveza Artesanal")
    elif opcion_maridaje == "Cóctel de Frutas":
        director.builder.construir_maridaje("Cóctel de Frutas")

    # Elección de extras y finalizaciones
    InterfazUsuario.mostrar_opciones(["Bordes Especiales", "Acabados con Trufas", "Acabados con Caviar"])
    opcion_extras = InterfazUsuario.obtener_opcion(["Bordes Especiales", "Acabados con Trufas", "Acabados con Caviar"], multiple=True)

    for opcion in opcion_extras:
        director.builder.construir_extra(opcion)

    # Elección de entrega a domicilio
    InterfazUsuario.mostrar_opciones(["Sí", "No"])
    opcion_entrega_domicilio = InterfazUsuario.obtener_opcion(["Sí", "No"])

    if opcion_entrega_domicilio == "Sí":
        director.builder.construir_entrega_domicilio()

    # Elección de tiempo y precio final
    director.builder.construir_tiempo_precio_final()

    # Al final, puedes imprimir la pizza personalizada
    pizza_personalizada = director.builder.obtener_pizza()
    print(pizza_personalizada)
