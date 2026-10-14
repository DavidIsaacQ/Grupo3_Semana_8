#Ejercicio 2 - Ordenamiento alfanumerico de nombres

nombres = ["Carlos", "ana", "Beatriz", "david", "Elena"]

print(f"1. {nombres}")

nombres.sort(key=str.lower)
print(f"2. {nombres}")

descendente = sorted(nombres, key=str.lower, reverse=True)
print(f"3. {descendente}")