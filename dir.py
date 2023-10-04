"""dir() es una función integrada que se utiliza para obtener una lista ordenada
de nombres que están definidos actualmente en un módulo,
objeto o espacio de nombres.
"""

import math
print(dir(math))

x = "Hola, mundo"
print(dir(x))

class Ejemplo:
    def __init__(self):
        self.variable = 42
    
    def metodo(self):
        print("¡Hola, soy un método!")

# Crear una instancia de la clase
objeto_ejemplo = Ejemplo()

# Usar dir() con el objeto
print(dir(objeto_ejemplo))
