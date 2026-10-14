# #Enunciado7 –Extraccióncon Expresiones Regulares
# Dada una lista de strings con información mezclada como:
# ['Ana García - edad:25 - tel:987654321', 'Luis Pérez - edad:30 - tel:912345678']
# Usa expresiones regulares para extraer el nombre, la edad y el teléfono de cada registro
# y almacénalos en una lista de diccionarios

import re

lista_registros = [
    'Ana García - edad:25 - tel:987654321', 
    'Luis Pérez - edad:30 - tel:912345678'
]


patron = r"^(.*?) - edad:(\d+) - tel:(\d+)$"

lista_diccionarios = []

for registro in lista_registros:
    coincidencia = re.match(patron, registro)
    if coincidencia:
       
        nombre = coincidencia.group(1)
        edad = int(coincidencia.group(2)) 
        telefono = coincidencia.group(3)
        
        diccionario_persona = {
            "nombre": nombre,
            "edad": edad,
            "telefono": telefono
        }
        lista_diccionarios.append(diccionario_persona)

print(lista_diccionarios)
