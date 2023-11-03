# Explicación de cómo generar errores (raising errors) y uso de assert

# En Python, puedes generar errores intencionales o "lanzar excepciones" cuando una condición no se cumple.
# También puedes utilizar la declaración 'assert' para verificar si una condición es verdadera.

# Ejemplo 1: Generar un error intencional
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No puedes dividir entre cero.")
    return a / b

try:
    resultado = dividir(5, 0)  # Intentamos dividir 5 por 0
except ZeroDivisionError as error:
    print("Error:", error)
    print("Se generó un error intencional.")

# Ejemplo 2: Usar la declaración 'assert'
def obtener_edad(nombre, edad):
    assert edad >= 0, "La edad no puede ser un número negativo"
    return f"{nombre} tiene {edad} años."

nombre = "Alice"
edad = -5

try:
    resultado = obtener_edad(nombre, edad)
except AssertionError as error:
    print("Error:", error)
    print("Se generó un error de aserción (assertion error).")

# Ejemplo 3: Usar 'assert' con una condición verdadera
def es_positivo(numero):
    assert numero > 0, "El número debe ser positivo"
    return f"{numero} es positivo."

try:
    resultado = es_positivo(10)  # Esto funcionará sin errores
except AssertionError as error:
    print("Error:", error)
    print("No se generó un error porque la condición de assert es verdadera.")

# Ejemplo 4: Usar 'assert' en pruebas
def prueba_division():
    resultado = dividir(8, 2)
    assert resultado == 4, "La división es incorrecta"
    print("Prueba de división pasada con éxito.")

try:
    prueba_division()  # Esta prueba pasará sin errores
except AssertionError as error:
    print("Error:", error)
    print("La prueba de división falló.")



