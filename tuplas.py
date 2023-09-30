# Archivo: tuplas_ejemplos.py

# Definir una tupla
mi_tupla = (1, "dos", 3.0)

# Mostrar la tupla
print("Mi tupla:", mi_tupla)

# Desempaquetar una tupla
a, b, c = mi_tupla
print("Desempaquetado:", a, b, c)

# Función que devuelve una tupla
def obtener_coordenadas():
    return 10, 20, 30

# Desempaquetar el resultado de la función
x, y, z = obtener_coordenadas()
print("Coordenadas:", x, y, z)
