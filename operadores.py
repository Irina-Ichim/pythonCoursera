# Ejemplo de operador AND
def ejemplo_operador_and(valor1, valor2):
    """
    Esta función demuestra el operador AND en Python.
    
    Args:
        valor1 (bool): El primer valor booleano.
        valor2 (bool): El segundo valor booleano.
        
    Returns:
        bool: El resultado de la operación AND entre valor1 y valor2.
    """
    resultado = valor1 and valor2
    return resultado

# Ejemplo de operador OR
def ejemplo_operador_or(valor1, valor2):
    """
    Esta función demuestra el operador OR en Python.
    
    Args:
        valor1 (bool): El primer valor booleano.
        valor2 (bool): El segundo valor booleano.
        
    Returns:
        bool: El resultado de la operación OR entre valor1 y valor2.
    """
    resultado = valor1 or valor2
    return resultado

# Ejemplo de operador NOT
def ejemplo_operador_not(valor):
    """
    Esta función demuestra el operador NOT en Python.
    
    Args:
        valor (bool): El valor booleano a negar.
        
    Returns:
        bool: El resultado de la operación NOT en valor.
    """
    resultado = not valor
    return resultado

# Ejemplo de operadores lógicos combinados
def ejemplo_operadores_combinados(valor1, valor2, valor3):
    """
    Esta función demuestra el uso de operadores lógicos combinados en Python.
    
    Args:
        valor1 (bool): El primer valor booleano.
        valor2 (bool): El segundo valor booleano.
        valor3 (bool): El tercer valor booleano.
        
    Returns:
        bool: El resultado de la operación (valor1 and valor2) or (not valor3).
    """
    resultado = (valor1 and valor2) or (not valor3)
    return resultado

# Ejemplo de operador mayor o igual que (>=)
def ejemplo_operador_mayor_igual(valor1, valor2):
    resultado = valor1 >= valor2
    return resultado

# Ejemplo de operador menor o igual que (<=)
def ejemplo_operador_menor_igual(valor1, valor2):
    resultado = valor1 <= valor2
    return resultado

# Ejemplo de operador igual a (==)
def ejemplo_operador_igual(valor1, valor2):
    """
    Esta función demuestra el operador igual a (==) en Python.
    
    Args:
        valor1: El primer valor a comparar.
        valor2: El segundo valor a comparar.
        
    Returns:
        bool: True si valor1 es igual a valor2, False en caso contrario.
    """
    resultado = valor1 == valor2
    return resultado

# Ejemplo de operador no igual a (!=)
def ejemplo_operador_no_igual(valor1, valor2):
    """
    Esta función demuestra el operador no igual a (!=) en Python.
    
    Args:
        valor1: El primer valor a comparar.
        valor2: El segundo valor a comparar.
        
    Returns:
        bool: True si valor1 no es igual a valor2, False en caso contrario.
    """
    resultado = valor1 != valor2
    return resultado

# Ejemplo de operador mayor que (>)
def ejemplo_operador_mayor_que(valor1, valor2):
    """
    Esta función demuestra el operador mayor que (>) en Python.
    
    Args:
        valor1: El primer valor a comparar.
        valor2: El segundo valor a comparar.
        
    Returns:
        bool: True si valor1 es mayor que valor2, False en caso contrario.
    """
    resultado = valor1 > valor2
    return resultado

# Ejemplo de operador menor que (<)
def ejemplo_operador_menor_que(valor1, valor2):
    """
    Esta función demuestra el operador menor que (<) en Python.
    
    Args:
        valor1: El primer valor a comparar.
        valor2: El segundo valor a comparar.
        
    Returns:
        bool: True si valor1 es menor que valor2, False en caso contrario.
    """
    resultado = valor1 < valor2
    return resultado
