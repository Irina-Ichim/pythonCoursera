def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.
    
    Args:
        base (float): La longitud de la base del triángulo.
        altura (float): La altura del triángulo desde la base.
    
    Returns:
        float: El área calculada del triángulo.
    """
    area = (base * altura) / 2
    return area

# Llamamos a la función y almacenamos el resultado en una variable
area_triangulo = calcular_area_triangulo(5, 4)

# Usamos el valor de retorno en otro cálculo
area_total = area_triangulo * 2

# Imprimimos el resultado final
print("El área total es:", area_total)

def convertir_segundos_a_tiempo(segundos):
    """
    Convierte una cantidad de segundos en horas, minutos y segundos.
    
    Args:
        segundos (int): La cantidad de segundos a convertir.
    
    Returns:
        tuple: Una tupla con tres valores: (horas, minutos, segundos).
    """
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos_restantes_final = segundos_restantes % 60
    return horas, minutos, segundos_restantes_final

# Llamamos a la función y almacenamos los valores de retorno en variables separadas
horas, minutos, segundos = convertir_segundos_a_tiempo(7385)

# Imprimimos los valores convertidos
print(f"Horas: {horas}, Minutos: {minutos}, Segundos: {segundos}")

def saludar(nombre):
    """
    Saluda a una persona por su nombre.
    
    Args:
        nombre (str): El nombre de la persona a saludar.
    """
    print(f"Hola, {nombre}!")

# Llamamos a la función pero no almacenamos ningún valor de retorno
saludar("Juan")
