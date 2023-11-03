# test_calculator.py
import unittest   #  Importa el módulo unittest, que es parte de la biblioteca estándar de Python y se utiliza para escribir pruebas unitarias.
from ejercicio_para_practicar_test_unitario import add # importo la funcion que he creado en mi archivo ejercicio_para_practicar_test_unitario

class TestCalculator(unittest.TestCase):   # Define una nueva clase llamada TestCalculator que hereda de unittest.TestCase. Esta clase contendrá los métodos de prueba que verificarán el comportamiento de tu código.

    def test_add(self):                   # Define un método llamado test_add dentro de la clase TestCalculator
        self.assertEqual(add(1, 2), 3)   #  Esta línea es una aserción que verifica si la llamada a add(1, 2) es igual a 3. Si la función add no devuelve 3, la prueba fallará.
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        
    
    def test_add_large_numbers(self):
        result = add(10**1000, 10**1000)
        self.assertEqual(result, 2 * (10**1000))  # La suma de dos números muy grandes debería ser el doble del número grande.
        
     # aditional test   
    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(0, -7), -7)


if __name__ == '__main__':     # Comprueba si el script se está ejecutando como el programa principal. Esto es necesario para garantizar que las pruebas solo se ejecuten cuando ejecutes este archivo directamente.
    unittest.main()            #  Si el script se está ejecutando como el programa principal, esta línea inicia la ejecución de las pruebas unitarias definidas en la clase TestCalculator.

#  Los "edge cases" son situaciones o condiciones extremas que están fuera de los escenarios normales que tu código debe ser capaz de manejar. 
#  Estos casos son importantes de probar porque a menudo revelan problemas o errores en tu código que podrían no ser evidentes 
#  en condiciones normales.
# Casos :
# Números muy grandes o muy pequeños.
# Cadenas vacías o de longitud máxima.
# Valores nulos o valores extremos.
# Situaciones en las que un cálculo podría causar un desbordamiento de memoria o errores matemáticos.
# Escenarios en los que el código debe lidiar con limitaciones de recursos, como memoria o velocidad de procesamiento.
#Los tests unitarios se enfocan en la funcionalidad principal de una unidad de código,
# los tests de casos límite evalúan situaciones excepcionales o extremas,
# y los tests adicionales amplían la cobertura de pruebas considerando diversos escenarios. 
# Es común que los tests de casos límite se incluyan como parte de los tests unitarios o de los tests adicionales.