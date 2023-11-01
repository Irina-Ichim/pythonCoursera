import unittest

# Definimos una función simple que suma dos números.
def suma(a, b):
    return a + b

# Creamos una clase que hereda de unittest.TestCase para nuestras pruebas.
class TestTDD(unittest.TestCase):

    # Escribimos nuestra primera prueba para la función suma.
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)  # Probamos la suma de 2 y 3.

if __name__ == '__main__':
    unittest.main()

# Importamos la biblioteca unittest que proporciona las herramientas para crear pruebas unitarias en Python.

# Definimos una función simple llamada suma(a, b) que toma dos números y devuelve su suma.

# Creamos una clase llamada TestTDD que hereda de unittest.TestCase. Esta clase contendrá nuestras pruebas.

# Escribimos nuestra primera prueba dentro de la clase TestTDD.
# La prueba verifica si la función suma devuelve el resultado correcto cuando se le pasan los valores 2 y 3.
# Usamos self.assertEqual para verificar si el resultado de la función es igual a 5.

# Finalmente, si el archivo se ejecuta como programa principal, llamamos a unittest.main() para ejecutar todas las pruebas
# definidas en nuestra clase de prueba.