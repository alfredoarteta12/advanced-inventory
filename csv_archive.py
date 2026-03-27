import csv

def guardar_csv(inventario, ruta):
    """Guarda la lista de diccionarios en un archivo CSV."""
    if not inventario:
        print(" Error: No hay datos para guardar.")
        return
    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
            writer.writeheader()
            writer.writerows(inventario)
        print(f" Inventario guardado exitosamente en: {ruta}")
    except Exception as e:
        print(f" Error al escribir el archivo: {e}")

def cargar_csv(ruta):
    """Carga datos de un CSV, valida tipos y cuenta filas corruptas."""
    productos_validos = []
    errores = 0
    try:
        with open(ruta, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                try:
                    # Validar que existan las columnas y sean números positivos
                    nombre = fila['nombre'].strip()
                    precio = float(fila['precio'])
                    cantidad = int(fila['cantidad'])
                    if precio < 0 or cantidad < 0: raise ValueError
                    
                    productos_validos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except (ValueError, KeyError, TypeError):
                    errores += 1
        return productos_validos, errores
    except FileNotFoundError:
        print("Error: El archivo no existe.")
        return None, 0
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None, 0