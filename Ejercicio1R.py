#Ejercicio 1 - Registro de productos con arreglos paralelos

nombres = ["pantalon", "polo", "zapato", "casaca"]
precios = [50 , 20 , 150 , 80]
stock = [15, 24, 10, 15]

inventario = 0

for a, b, c in zip(nombres, precios, stock):
    print(f"{a}: S/.{b} | {c} unidades")
    inventario += b*c

print(f"Precio total del inventario: S/.{inventario}")

