# Archivo: ejemplo_help.py

# Ejemplo con un objeto
x = "Hola, mundo"
print("=== Ayuda para el objeto ===")
help(x)

# Ejemplo con un módulo
import math
print("\n=== Ayuda para el módulo math ===")
help(math)

# Ejemplo con una función
def saludar():
    """Esta función saluda."""
    print("¡Hola!")

print("\n=== Ayuda para la función saludar ===")
help(saludar)
