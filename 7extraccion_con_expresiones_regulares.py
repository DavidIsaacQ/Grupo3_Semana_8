
# EJERCICIO 7 - EXTRACCION CON EXPRESIONES REGULARES

import re

registros = [
    'Ana García - edad:25 - tel:987654321',
    'Luis Pérez - edad:30 - tel:912345678'
]

estudiantes = []

for registro in registros:
    resultado = re.search(r'(.+?) - edad:(\d+) - tel:(\d+)', registro)

    if resultado:
        estudiante = {
            "nombre": resultado.group(1),
            "edad": int(resultado.group(2)),
            "telefono": resultado.group(3)
        }
        estudiantes.append(estudiante)

print(estudiantes)
