from service import*
from csv_archive import*

def main():
    inventario = []
    ejecutando = True
    
    while ejecutando:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar | 2. Mostrar | 3. Buscar | 4. Actualizar")
        print("5. Eliminar | 6. Estadísticas | 7. Guardar | 8. Cargar | 9. Salir")
        opcion = input("Seleccione (1-9): ")

        if opcion == "1":
            try:
                nombre_producto = input("favor ingrese el nombre del producto: ")
                precio_producto = float(input("favor ingrese el precio del producto: "))
                cantidad_precio = int(input("favor ingrese la Cantidad de productos: "))
                agregar_producto(inventario, nombre_producto, precio_producto, cantidad_precio)
                print(" Agregado correctamente")
            except ValueError: print("Error: Ingrese números válidos.")

        elif opcion == "2":
            mostrar_inventario(inventario)

        
        elif opcion == "3":
            nombre = input(" Nombre del producto a buscar: ")
            prod = buscar_producto(inventario, nombre)
            if prod:
                print(f" Encontrado: {prod['nombre']} | Precio: ${prod['precio']} | Stock: {prod['cantidad']}")
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            nombre = input(" Nombre del producto a actualizar: ")
            # Primero verificamos si existe
            if buscar_producto(inventario, nombre):
                try:
                    # Dejamos vacío para no cambiar el valor actual
                    n_precio = input("Nuevo precio (deja vacío para no cambiar): ")
                    n_cant = input("Nueva cantidad (deja vacío para no cambiar): ")
                    
                    # Solo convertimos si el usuario escribió algo
                    p = float(n_precio) if n_precio.strip() != "" else None
                    c = int(n_cant) if n_cant.strip() != "" else None
                    
                    actualizar_producto(inventario, nombre, p, c)
                    print(" Producto actualizado con éxito.")
                except ValueError:
                    print(" Error: Los valores deben ser numéricos.")
            else:
                print(" El producto no existe en el inventario.")
        elif opcion == "5":
            nombre = input(" Nombre del producto a eliminar: ")
            if eliminar_producto(inventario, nombre):
                print(f" '{nombre}' ha sido eliminado.")
            else:
                print(" No se pudo eliminar: el producto no existe.")     


        elif opcion == "6":
            s = calcular_estadisticas(inventario)
            if s:
                print(f"\n TOTAL: {s['unidades']} unidades | VALOR: ${s['valor_total']:.2f}")
                print(f" Más caro: {s['mas_caro']['nombre']} | Stock: {s['mayor_stock']['nombre']}")
            else: print(" Inventario vacío.")

        elif opcion == "7":
            ruta = input("Nombre del archivo (ej: datos.csv): ")
            guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Ruta del archivo: ")
            datos, err = cargar_csv(ruta)
            if datos is not None:
                print(f"Leídos {len(datos)} productos. {err} errores omitidos.")
                modo = input("¿Sobrescribir (SI) o Fusionar (NO)? ").upper()
                if modo == "SI":
                    inventario = datos
                else:
                    # Lógica de Fusión: Sumar stock si el nombre coincide
                    for p_nuevo in datos:
                        exis = buscar_producto(inventario, p_nuevo["nombre"])
                        if exis:
                            exis["cantidad"] += p_nuevo["cantidad"]
                            exis["precio"] = p_nuevo["precio"]
                        else:
                            inventario.append(p_nuevo)
                print("Proceso completado.")

        elif opcion == "9":
            print("Saliendo...")
            ejecutando = False
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()