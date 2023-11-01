# Explicación del manejo de excepciones usando try-except

# A veces, los programas pueden encontrar errores durante la ejecución.
# En Python, podemos manejar estos errores usando bloques try-except.

# Ejemplo 1: División por cero
try:
    resultado = 5 / 0  # Intentamos dividir 5 por 0
except ZeroDivisionError as error:
    print("Error:", error)
    print("No puedes dividir entre cero.")

# Ejemplo 2: Acceder a un índice fuera de rango
mi_lista = [1, 2, 3]
try:
    elemento = mi_lista[5]  # Intentamos acceder a un índice que no existe
except IndexError as error:
    print("Error:", error)
    print("El índice está fuera de rango.")

# Ejemplo 3: Manejando múltiples tipos de excepciones
try:
    resultado = 10 / '2'  # Esto generará un TypeError
except ZeroDivisionError as error:
    print("Error de división por cero:", error)
except TypeError as error:
    print("Error de tipo:", error)
    print("Asegúrate de que los tipos de datos sean compatibles.")

# Ejemplo 4: Usando un bloque 'else' después de 'except'
try:
    num = int(input("Ingresa un número: "))
except ValueError as error:
    print("Error de valor:", error)
    print("No ingresaste un número válido.")
else:
    print("Has ingresado un número válido:", num)

# Ejemplo 5: Uso de 'finally' para la limpieza
try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError as error:
    print("Error de archivo:", error)
else:
    print("El archivo se abrió correctamente.")
finally:
    archivo.close()  # Garantizamos que el archivo se cierre, incluso si hay una excepción

# Puedes agregar más ejemplos y manejar diferentes tipos de excepciones según tus necesidades.

