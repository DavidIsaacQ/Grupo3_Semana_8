
# EJERCICIO 6 - COMBINACION DE ARREGLOS Y ORDENAMIENTO

productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
ventas = [150, 300, 200, 100]

# Combinar los arreglos en una lista de diccionarios
lista_productos = []

for i in range(len(productos)):
    producto = {"nombre": productos[i], "ventas": ventas[i]}
    lista_productos.append(producto)

# Ordenar las ventas de mayor a menor
lista_productos.sort(key=lambda x: x["ventas"], reverse=True)

# Imprimir el ranking
print("RANKING DE VENTAS")

for i in range(len(lista_productos)):
    print(i + 1, "° lugar:", lista_productos[i]["nombre"],
          "- Ventas:", lista_productos[i]["ventas"])

# Calcular el promedio de ventas
promedio = sum(ventas) / len(ventas)
print("\nPromedio de ventas:", promedio)

# Mostrar productos que superan el promedio
print("Productos sobre la media:")

for producto in lista_productos:
    if producto["ventas"] > promedio:
        print(producto["nombre"], "-", producto["ventas"], "ventas")
