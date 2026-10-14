
# EJERCICIO 3 - BUSQUEDA SIMPLE EN UNA LISTA DE EMAILS

emails = ['ana@gmail.com', 'luis@outlook.com',
          'mia@gmail.com', 'juan@yahoo.com']

# 1. Contar cuantos emails son de Gmail
contador = 0

for email in emails:
    if email.endswith("@gmail.com"):
        contador = contador + 1

print("1. Cantidad de emails de Gmail:", contador)

# 2. Mostrar los emails que terminan en '.com'
print("\n2. Emails que terminan en .com:")

for email in emails:
    if email.endswith(".com"):
        print(email)

# 3. Verificar si un email esta en la lista
print("\n3. Verificar si luis@outlook.com esta en la lista:")

if 'luis@outlook.com' in emails:
    print("El email si esta en la lista")
else:
    print("El email no esta en la lista")
