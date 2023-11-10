# Ejemplo 1: Error de Lista Fuera de Índice
"""Escenario: Tu programa arroja un error "IndexError: list index out of range"."""

# Código con Error de Lista Fuera de Índice

# def obtener_elemento(lista, indice):
#     return lista[indice]

# mi_lista = [1, 2, 3]
# resultado = obtener_elemento(mi_lista, 5)
# print(resultado)

# Solución:
# Debugging: Añadir impresiones (print statements) para rastrear los valores de las variables.
# def obtener_elemento(lista, indice):
#     print(f"Intentando acceder al índice {indice} de la lista {lista}")
#     return lista[indice]

# mi_lista = [1, 2, 3]
# resultado = obtener_elemento(mi_lista, 5)

# Solución: Verificar los límites de la lista antes de acceder al índice.
def obtener_elemento(lista, indice):
    if 0 <= indice < len(lista):
        return lista[indice]
    else:
        return None

mi_lista = [1, 2, 3]
resultado = obtener_elemento(mi_lista, 5)
print(resultado)

# Ejemplo 2: Problema de Manejo de Excepciones
# Escenario: Tu programa no maneja adecuadamente una excepción.

# Código con Problema de Manejo de Excepciones
# def dividir(a, b):
#     return a / b

# try:
#     resultado = dividir(10, 0)
#     print(resultado)
# except ZeroDivisionError as e:
#     print(f"Error: {e}")

# Solución:
# Debugging: Agregar un print dentro del bloque except para entender la excepción.
# try:
#     resultado = dividir(10, 0)
#     print(resultado)
# except ZeroDivisionError as e:
#     print(f"Error: {e}")

# Solución: Añadir lógica para manejar la excepción y evitar la división por cero.
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"

resultado = dividir(10, 0)
print(resultado)
