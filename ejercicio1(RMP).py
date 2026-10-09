# #Enunciado1 –Registro de Productos con Arreglos Paralelos
# Crea tres arreglos paralelos para almacenar información de 4 productos: 
# nombres, precios y cantidades en stock.
# Imprime un reporte que muestre cada producto con su precio y cantidad
#  en una sola línea por producto.
# Además, calcula e imprime el precio total del 
# inventario (precio × cantidad para todos)

nombre = ["Monitor Gaming", "Tarjeta de video Rtx3060", "Mouse", "Teclado"]
precios = [1560.5, 1000.4, 205.5, 50.3]
cantidad = [10, 15, 50, 35]

inventario = 0

for n,p,c in zip(nombre, precios, cantidad):
    inventario += p * c
    print (f"Producto: {n}, Precio: ${p}, Stock: {cantidad}")

print (f"Inventario: ${inventario}")