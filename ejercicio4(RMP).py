# #Enunciado4 –Lista de Diccionario de Estudiantes
# Crea una lista de diccionarios para 4 estudiantes con 
# los campos: 'nombre', 'carrera' y 'promedio'.
# Imprime el nombre y promedio de cada estudiante.
# Luego muestra el nombre del estudiante con el promedio más alto

Estudiantes = [
    {"Nombre": "Rodolfo", "Carrera" : "Ing. de Sistemas", "Promedio" : 17},
    {"Nombre": "Grace", "Carrera" : "Medicina", "Promedio" : 15},
    {"Nombre": "Elvis", "Carrera" : "Arquitectura", "Promedio" : 19},
    {"Nombre": "Pancracio", "Carrera" : "Tiktoker", "Promedio" : 14}
]
mayor_nota = Estudiantes[0]
for students in Estudiantes:
    print(students['Nombre'],':',students['Promedio'])
    if students['Promedio'] > mayor_nota['Promedio']:
        mayor_nota = students
print (f"El alumno con mayor calificacion es {mayor_nota['Nombre']}, nota: {mayor_nota['Promedio']}")
