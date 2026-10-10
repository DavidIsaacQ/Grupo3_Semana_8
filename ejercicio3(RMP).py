# #Enunciado3 –BúsquedaSimple enunaLista de Emails
# Tienes la lista: 
# emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']
# 1) Imprime cuántos emails son de Gmail.
# 2) Muestra solo los emails que terminan en '.com'.
# 3) Verifica si 'luis@outlook.com' está en la lista (usa 'in')

emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']

contador = 0
for correo in emails:
    gmail = correo.split('@')
    if 'gmail.com' in correo:
        contador += 1
        print (f"Usuario: {correo}")
print (f"hay {contador} correos de gmail.com")
print (" ")
for correo in emails:
    if correo.endswith ('.com'):
        print (f"Termina en .com: {correo}")
print (" ")
for correo in emails:
    if 'luis@outlook.com' in correo:
        print (f"Encontrado! {correo}")



    
    