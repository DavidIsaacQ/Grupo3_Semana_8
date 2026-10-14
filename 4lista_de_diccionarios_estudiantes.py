
# EJERCICIO 4 - LISTA DE DICCIONARIOS DE ESTUDIANTES

estudiantes = [
    {"nombre": "Ana", "carrera": "Ingenieria de Sistemas", "promedio": 17},
    {"nombre": "Luis", "carrera": "Administracion", "promedio": 15},
    {"nombre": "Carlos", "carrera": "Ingenieria Civil", "promedio": 19},
    {"nombre": "Maria", "carrera": "Contabilidad", "promedio": 18}
]

# 1. Imprimir el nombre y promedio de cada estudiante
print("REPORTE DE ESTUDIANTES")
print("----------------------")

for estudiante in estudiantes:
    print("Nombre:", estudiante["nombre"],
          "| Promedio:", estudiante["promedio"])

# 2. Encontrar al estudiante con el promedio mas alto
mejor_estudiante = estudiantes[0]

for estudiante in estudiantes:
    if estudiante["promedio"] > mejor_estudiante["promedio"]:
        mejor_estudiante = estudiante

print("----------------------")
print("Estudiante con el promedio mas alto:")
print("Nombre:", mejor_estudiante["nombre"])
print("Promedio:", mejor_estudiante["promedio"])
