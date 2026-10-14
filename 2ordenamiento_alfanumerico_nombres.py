
# EJERCICIO 2 - ORDENAMIENTO ALFANUMERICO DE NOMBRES

nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']

# 1. Imprimir la lista original sin modificar
print("1. Lista original:")
print(nombres)

# 2. Ordenar alfabeticamente ignorando mayusculas
nombres.sort(key=str.lower)
print("\n2. Lista ordenada ascendentemente:")
print(nombres)

# 3. Crear una nueva lista ordenada en forma descendente
nombres_descendentes = sorted(nombres, key=str.lower, reverse=True)
print("\n3. Lista ordenada descendentemente:")
print(nombres_descendentes)

# 4. Mostrar la lista original despues de usar sort()
print("\n4. Lista original despues de sort():")
print(nombres)
