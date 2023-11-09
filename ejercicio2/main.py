# En el archivo main.py

from director import Director
from cliente import Cliente
from builder import MasaBuilder, MasaFermentadaBuilder
from interfaz import InterfazUsuario

if __name__ == "__main__":
    director = Director(MasaBuilder())
    cliente = Cliente(director)  # Asegúrate de pasar el objeto Director al Cliente

    # Utilizamos la interfaz de usuario para la elección de la masa
    InterfazUsuario.mostrar_opciones(["Masa Delgada", "Masa Fermentada 48h"])
    opcion_masa = InterfazUsuario.obtener_opcion(["Masa Delgada", "Masa Fermentada 48h"])

    if opcion_masa == 1:
        director.builder = MasaBuilder()
    else:
        director.builder = MasaFermentadaBuilder()  # Cambiamos directamente el builder

    director.construir_pizza()

    # Elección de la salsa
    InterfazUsuario.mostrar_opciones(["Salsa Clásica", "Salsa de Autor", "Salsa Vegana", "Edición Limitada"])
    opcion_salsa = InterfazUsuario.obtener_opcion(["Salsa Clásica", "Salsa de Autor", "Salsa Vegana", "Edición Limitada"])

    if opcion_salsa == 1:
        director.builder.construir_salsa_clasica()
    elif opcion_salsa == 2:
        director.builder.construir_salsa_autor()
    elif opcion_salsa == 3:
        director.builder.construir_salsa_vegana()
    elif opcion_salsa == 4:
        director.builder.construir_salsa_edicion_limitada()

    # Elección de ingredientes
    InterfazUsuario.mostrar_opciones(["Queso", "Tomate", "Pepperoni", "Champiñones", "Aceitunas"])
    opcion_ingredientes = InterfazUsuario.obtener_opcion(["Queso", "Tomate", "Pepperoni", "Champiñones", "Aceitunas"], multiple=True)

    for opcion in opcion_ingredientes:
        director.builder.agregar_ingrediente(opcion)

    # Elección de la técnica de cocción
    InterfazUsuario.mostrar_opciones(["Horno Tradicional", "Cocción Molecular"])
    opcion_coccion = InterfazUsuario.obtener_opcion(["Horno Tradicional", "Cocción Molecular"])

    if opcion_coccion == 1:
        director.builder.construir_horno_tradicional()
    elif opcion_coccion == 2:
        director.builder.construir_coccion_molecular()

    # Elección de la presentación
    InterfazUsuario.mostrar_opciones(["Clásica", "Obras de Arte"])
    opcion_presentacion = InterfazUsuario.obtener_opcion(["Clásica", "Obras de Arte"])

    if opcion_presentacion == 1:
        director.builder.construir_presentacion_clasica()
    elif opcion_presentacion == 2:
        director.builder.construir_presentacion_obras_arte()

    # Elección del maridaje
    InterfazUsuario.mostrar_opciones(["Vino Tinto", "Cerveza Artesanal", "Cóctel de Frutas"])
    opcion_maridaje = InterfazUsuario.obtener_opcion(["Vino Tinto", "Cerveza Artesanal", "Cóctel de Frutas"])

    if opcion_maridaje == 1:
        director.builder.construir_maridaje_vino_tinto()
    elif opcion_maridaje == 2:
        director.builder.construir_maridaje_cerveza_artesanal()
    elif opcion_maridaje == 3:
        director.builder.construir_maridaje_coctel_frutas()

    # Elección de extras y finalizaciones
    InterfazUsuario.mostrar_opciones(["Bordes Especiales", "Acabados con Trufas", "Acabados con Caviar"])
    opcion_extras = InterfazUsuario.obtener_opcion(["Bordes Especiales", "Acabados con Trufas", "Acabados con Caviar"], multiple=True)

    for opcion in opcion_extras:
        director.builder.agregar_extra(opcion)

    # Elección de entrega a domicilio
    InterfazUsuario.mostrar_opciones(["Sí", "No"])
    opcion_entrega_domicilio = InterfazUsuario.obtener_opcion(["Sí", "No"])

    if opcion_entrega_domicilio == 1:
        director.builder.construir_entrega_domicilio()

    # Elección de tiempo y precio final
    director.builder.construir_tiempo_precio_final()

    # Al final, puedes imprimir la pizza personalizada
    pizza_personalizada = director.builder.obtener_pizza()
    print(pizza_personalizada)
