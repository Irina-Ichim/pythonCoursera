"""
Este archivo contiene un ejemplo de función recursiva para calcular el factorial de un número.
"""

def factorial(n):
    """
    Calcula el factorial de un número utilizando recursión.

    Parameters:
        n (int): El número para el cual calcular el factorial.

    Returns:
        int: El factorial de n.
    """
    # Caso base
    if n == 0:
        return 1
    # Caso recursivo
    else:
        return n * factorial(n - 1)

# Ejemplos de uso
resultado1 = factorial(5)
resultado2 = factorial(0)

print(f"El factorial de 5 es: {resultado1}")
print(f"El factorial de 0 es: {resultado2}")
