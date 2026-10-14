# #Enunciado6 –Combinaciónde Arreglos y Ordenamiento
# Tienes dos arreglos paralelos: productos (strings) y ventas (enteros).
# Combínalos en una lista de diccionarios, luego:
# 1) Ordena por ventas de mayor a menor.
# 2) Imprime el ranking con posición (1°, 2°, etc.).
# 3) Calcula el promedio de ventas e indica cuáles están sobre la media

productos = ["Zapatillas" , "Polos" , "Pantalones" , "Cinturones"]
ventas = [35, 50, 24, 34]

listaProductos = []
for prod, vent in zip(productos, ventas):
    listaProductos.append({"nombre" : prod , "ventas" : vent})

ordenDesc = sorted(listaProductos, key=lambda x: x["ventas"], reverse = True)
print (ordenDesc)

print ("RANKING DE VENTAS")
for i, prod in enumerate (ordenDesc, start=1):
        print(f"{i}°: {prod['nombre']} ({prod['ventas']} ventas)")

total_ventas = sum(prod["ventas"] for prod in ordenDesc)
promedio = total_ventas / len(ordenDesc)

print(f"\nEl promedio de ventas es: {promedio:.2f}")
print("\nProductos sobre la media:")

for prod in ordenDesc:
    if prod["ventas"] > promedio:
        print(f"- {prod['nombre']} ({prod['ventas']} ventas)")
