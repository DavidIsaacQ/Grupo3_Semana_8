# #Enunciado5 –Búsqueday Filtrado de Productos
# Tienes una lista de diccionarios de productos con 'nombre', 'categoria' y 'precio'.
# Implementa una función buscar_productos(lista, termino) que devuelva todos los productos
# cuyo nombre contenga el término de búsqueda (sin importar mayúsculas).
# Además, ordena los resultados por precio de menor a mayor

def buscar_productos (lista, termino):
    resultados = []
    termino_minuscula = termino.lower()

    for prod in lista:
        if termino_minuscula in prod['nombre'].lower():
            resultados.append(prod)

    resultados.sort(key=lambda prod: prod['precio'])
    return resultados
productos = [
    {'nombre': 'TECLADO' , 'categoria' : 'hardware' , 'precio' : 51.5},
    {'nombre': 'mouse' , 'categoria' : 'hardware' , 'precio' : 35},
    {'nombre': 'polo' , 'categoria' : 'ropa' , 'precio' : 16.60},
    {'nombre': 'ZAPATILLAS' , 'categoria' : 'calzado' , 'precio' : 80}
]
prod_encontrados = buscar_productos(productos, 't')

for prod in prod_encontrados: 
    print (f"{prod['nombre']} --> ${prod['precio']}")