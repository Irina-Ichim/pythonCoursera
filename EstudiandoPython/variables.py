"""
Este docstring explica los conceptos de conversión implícita y conversión explícita en Python.

- Conversión Implícita: Se refiere a la capacidad del intérprete de Python para realizar automáticamente conversiones de tipos de datos cuando se combinan datos de diferentes tipos en operaciones compatibles.

- Conversión Explícita: Implica que el programador realiza manualmente la conversión de un tipo de dato a otro utilizando funciones específicas, como la función `str()`, para controlar la representación de los datos o realizar operaciones que requieren tipos de datos compatibles.

Ejemplo de Conversión Explícita:
Antes de imprimir un número junto con texto, es necesario utilizar la función `str()` para convertir explícitamente el número en una cadena de texto. Esto permite concatenar la cadena con el número y obtener el resultado deseado.

Ejemplo de Conversión Implícita:
Cuando se realizan operaciones entre tipos de datos compatibles, como la suma de enteros y números de punto flotante, el intérprete realiza conversiones implícitas para garantizar que los tipos de datos sean compatibles y se obtenga el resultado deseado.

Ambos tipos de conversión son importantes en programación y se utilizan según las necesidades del código.

"""


base = 5
height = 3
area = (base * height)/2

print(area)
print("Es mi resultado " + str(area))