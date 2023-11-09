import csv

class CSVManager:
    @staticmethod
    def guardar_pizza_csv(pizza, archivo="pizzas_personalizadas.csv"):
        try:
            with open(archivo, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    pizza.tipo_masa,
                    pizza.salsa,
                    ",".join(pizza.ingredientes),
                    pizza.tecnica_coccion,
                    pizza.presentacion,
                    pizza.maridaje,
                    ",".join(pizza.extras),
                    pizza.tiempo_preparacion,
                    pizza.precio_final,
                ])
            print("Pizza guardada exitosamente en el archivo CSV.")
        except Exception as e:
            print(f"Error al guardar la pizza en el archivo CSV: {str(e)}")

    @staticmethod
    def leer_pizzas_csv(archivo="pizzas_personalizadas.csv"):
        pizzas = []
        try:
            with open(archivo, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Saltar la fila de encabezado
                for row in reader:
                    pizzas.append({
                        "Tipo de Masa": row[0],
                        "Salsa": row[1],
                        "Ingredientes": row[2].split(","),
                        "Técnica de Cocción": row[3],
                        "Presentación": row[4],
                        "Maridaje": row[5],
                        "Extras": row[6].split(","),
                        "Tiempo de Preparación": row[7],
                        "Precio Final": row[8],
                    })
            print("Pizzas cargadas exitosamente desde el archivo CSV.")
        except FileNotFoundError:
            print("No se encontró el archivo CSV. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al leer las pizzas desde el archivo CSV: {str(e)}")

        return pizzas
    @staticmethod
    def reconstruir_pizza(descripcion_pizza):
        director_reconstruccion = Director(BuilderReconstruccion())
        cliente_reconstruccion = Cliente()
        director_reconstruccion.builder.datos = descripcion_pizza
        director_reconstruccion.construir_pizza()
        return director_reconstruccion.builder.obtener_pizza()