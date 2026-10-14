
# EJERCICIO 5 - BUSQUEDA Y FILTRADO DE PRODUCTOS

productos = [
    {"nombre": "Laptop Lenovo", "categoria": "Computo", "precio": 2500},
    {"nombre": "Mouse Gamer", "categoria": "Accesorios", "precio": 120},
    {"nombre": "Laptop HP", "categoria": "Computo", "precio": 2200},
    {"nombre": "Teclado Mecanico", "categoria": "Accesorios", "precio": 180},
    {"nombre": "Mouse Inalambrico", "categoria": "Accesorios", "precio": 80}
]

def buscar_productos(lista, termino):
    resultados = []

    for producto in lista:
        if termino.lower() in producto["nombre"].lower():
            resultados.append(producto)

    resultados.sort(key=lambda producto: producto["precio"])

    return resultados


# Buscar productos
termino = input("Ingrese el nombre del producto que desea buscar: ")

encontrados = buscar_productos(productos, termino)

# Mostrar resultados
print("\nPRODUCTOS ENCONTRADOS")

if len(encontrados) > 0:
    for producto in encontrados:
        print("Nombre:", producto["nombre"],
              "| Categoria:", producto["categoria"],
              "| Precio: S/", producto["precio"])
else:
    print("No se encontraron productos.")
