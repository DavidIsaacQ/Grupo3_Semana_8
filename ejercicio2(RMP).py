# #Enunciado2 –OrdenamientoAlfanumérico de Nombres
# Dada la lista de nombres: ['Carlos','ana','Beatriz','david','Elena']
# 1) Imprímela sin modificar.
# 2) Ordénala alfabéticamente ignorando mayúsculas con sort().
# 3) Crea una nueva lista ordenada en orden descendente usando sorted().
# 4) Muestra los resultados de cada paso

nombres = ['Carlos', 'Ana', 'Beatriz', 'david', 'Elena']

sinModificar = nombres.copy()
nombres.sort(key=str.lower)

nueva_lista = sorted(nombres, key=str.lower, reverse = True)
print (f"Lista original: {sinModificar}")
print (f"Lista ordenada: {nombres}")
print (f"Lista descendente: {nueva_lista}")