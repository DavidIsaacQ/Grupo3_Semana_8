
# EJERCICIO 1 - REGISTRO DE PRODUCTOS CON ARREGLOS PARALELOS

nombres = ["Arroz", "Azucar", "Leche", "Aceite"]
precios = [4.50, 3.80, 4.20, 8.50]
cantidades = [10, 15, 8, 6]

total_inventario = 0

print("REPORTE DE PRODUCTOS")
print("--------------------")

for i in range(len(nombres)):
    print("Producto:", nombres[i],
          "| Precio: S/", precios[i],
          "| Cantidad:", cantidades[i])

    total_inventario = total_inventario + (precios[i] * cantidades[i])

print("--------------------")
print("Precio total del inventario: S/", round(total_inventario, 2))
