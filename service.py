def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un nuevo producto al inventario (lista de diccionarios)."""
    inventario.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})

def mostrar_inventario(inventario):
    """Imprime el inventario con un formato de tabla simple."""
    if not inventario:
        print("\nvEl inventario está vacío.")
        return
    print(f"\n{'Nombre':<15} | {'Precio':<10} | {'Stock':<8}")
    print("-" * 40)
    for p in inventario:
        print(f"{p['nombre']:<15} | ${p['precio']:<9.2f} | {p['cantidad']:<8}")

def buscar_producto(inventario, nombre):
    """Busca un producto por nombre (sin importar mayúsculas) y retorna el dict."""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio y/o cantidad de un producto si existe."""
    prod = buscar_producto(inventario, nombre)
    if prod:
        if nuevo_precio is not None: prod["precio"] = nuevo_precio
        if nueva_cantidad is not None: prod["cantidad"] = nueva_cantidad
        return True
    return False

def eliminar_producto(inventario, nombre):
    """Elimina un producto de la lista. Retorna True si tuvo éxito."""
    prod = buscar_producto(inventario, nombre)
    if prod:
        inventario.remove(prod)
        return True
    return False

def calcular_estadisticas(inventario):
    """Retorna un diccionario con métricas del negocio."""
    if not inventario: return None
    
    unidades = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    mas_caro = max(inventario, key=lambda x: x["precio"])
    mayor_stock = max(inventario, key=lambda x: x["cantidad"])
    
    return {
        "unidades": unidades,
        "valor_total": valor_total,
        "mas_caro": mas_caro,
        "mayor_stock": mayor_stock
    }