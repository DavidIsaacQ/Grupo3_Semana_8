# #Enunciado8 –Sistema de Calificaciones con Estructuras Combinadas
# Crea un sistema que maneje un diccionario de listas donde las claves son materias
# y los valores son listas de notas de estudiantes (arreglos paralelos con lista de nombres).
# Implementa funciones para: calcular el promedio por materia, encontrar al mejor estudiante
# de cada materia y generar un reporte ordenado por promedio general de mayor a menor

estudiantes = ["Ana", "Carlos", "Luis", "Sofía"]

calificaciones = {
    "Matemáticas":[11, 8, 20, 14],
    "Historia": [10, 16, 17, 13],
    "Ciencias": [15, 18, 12, 11]
}


def calcular_promedio_materia(calificaciones, materia):
    """Calcula el promedio de notas de una materia específica."""
    if materia not in calificaciones or not calificaciones[materia]:
        return 0.0
    notas = calificaciones[materia]
    return sum(notas) / len(notas)

def encontrar_mejor_estudiante(calificaciones, estudiantes, materia):
    """Encuentra al estudiante con la nota más alta en una materia."""
    if materia not in calificaciones or not calificaciones[materia]:
        return None, 0
    
    notas = calificaciones[materia]
    nota_maxima = max(notas)
    indice_mejor = notas.index(nota_maxima)
    mejor_estudiante = estudiantes[indice_mejor]
    
    return mejor_estudiante, nota_maxima

def generar_reporte_ordenado(calificaciones):
   
    promedios_materias = {}

    for materia in calificaciones:
        promedios_materias[materia] = calcular_promedio_materia(calificaciones, materia)

    reporte_ordenado = sorted(promedios_materias.items(), key=lambda x: x[1], reverse=True)
    return reporte_ordenado

print("--- Promedios por Materia ---")
for materia in calificaciones:
    promedio = calcular_promedio_materia(calificaciones, materia)
    print(f"{materia}: {promedio:.2f}")

print("\n--- Mejor Estudiante por Materia ---")
for materia in calificaciones:
    mejor, nota = encontrar_mejor_estudiante(calificaciones, estudiantes, materia)
    print(f"En {materia}: {mejor} con una nota de {nota}")

print("\n--- Reporte de Materias (Mayor a Menor Promedio) ---")
reporte = generar_reporte_ordenado(calificaciones)
for materia, promedio in reporte:
    print(f"Materia: {materia:<12} | Promedio General: {promedio:.2f}")
