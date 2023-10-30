# test_calculator.py
import unittest   #  Importa el módulo unittest, que es parte de la biblioteca estándar de Python y se utiliza para escribir pruebas unitarias.
from ejercicio_para_practicar_test_unitario import add # importo la funcion que he creado en mi archivo ejercicio_para_practicar_test_unitario

class TestCalculator(unittest.TestCase):   # Define una nueva clase llamada TestCalculator que hereda de unittest.TestCase. Esta clase contendrá los métodos de prueba que verificarán el comportamiento de tu código.

    def test_add(self):                   # Define un método llamado test_add dentro de la clase TestCalculator
        self.assertEqual(add(1, 2), 3)   #  Esta línea es una aserción que verifica si la llamada a add(1, 2) es igual a 3. Si la función add no devuelve 3, la prueba fallará.
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':     # Comprueba si el script se está ejecutando como el programa principal. Esto es necesario para garantizar que las pruebas solo se ejecuten cuando ejecutes este archivo directamente.
    unittest.main()            #  Si el script se está ejecutando como el programa principal, esta línea inicia la ejecución de las pruebas unitarias definidas en la clase TestCalculator.
