# Explicación de testing para errores esperados, assert y raise

# En Python, es importante realizar pruebas para manejar errores y excepciones de manera efectiva.
# Puedes hacer esto mediante el uso de las declaraciones 'assert' y 'raise' para verificar y manejar errores esperados.

# Ejemplo 1: Prueba para error esperado con 'assert'
def dividir(a, b):
    assert b != 0, "No puedes dividir entre cero"
    return a / b

try:
    resultado = dividir(5, 0)
except AssertionError as error:
    print("Error:", error)
    print("La prueba pasó porque el error fue esperado.")

# Ejemplo 2: Generar un error específico con 'raise'
def calcular_raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return numero ** 0.5

try:
    resultado = calcular_raiz_cuadrada(-9)
except ValueError as error:
    print("Error:", error)
    print("La excepción se generó correctamente porque el número era negativo.")

# Ejemplo 3: Prueba para error esperado con 'assert' en una función
def obtener_valor_por_indice(lista, indice):
    assert 0 <= indice < len(lista), "Índice fuera de rango"
    return lista[indice]

mi_lista = [10, 20, 30]

try:
    valor = obtener_valor_por_indice(mi_lista, 5)
except AssertionError as error:
    print("Error:", error)
    print("La prueba pasó porque el índice estaba fuera de rango.")

# Ejemplo 4: Generar un error específico con 'raise' en una función
def obtener_elemento_valido(lista, indice):
    if not (0 <= indice < len(lista)):
        raise IndexError("Índice fuera de rango")
    return lista[indice]

try:
    valor = obtener_elemento_valido(mi_lista, 5)
except IndexError as error:
    print("Error:", error)
    print("La excepción se generó correctamente porque el índice estaba fuera de rango.")



