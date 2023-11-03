numero = 1  # Inicializamos una variable con 1

while numero <= 5:  # Mientras 'numero' sea menor o igual a 5
    print(numero)   # Imprime el valor de 'numero'
    numero += 1     # Incrementa 'numero' en 1


"""
Este ejemplo muestra un bucle while simple que cuenta desde 1 hasta un número dado.

Parameters:
    None

Returns:
    None
"""
def contar_hasta():
    contador = 1
    while contador <= 5:
        print(contador)
        contador += 1

# Ejemplo de uso
contar_hasta()


"""
Este ejemplo muestra un bucle while que calcula la suma de los números naturales hasta un valor dado.

Parameters:
    n (int): El valor hasta el cual calcular la suma.

Returns:
    int: La suma de los números naturales hasta n.
"""
def suma_naturales(n):
    suma = 0
    contador = 1
    while contador <= n:
        suma += contador
        contador += 1
    return suma

# Ejemplo de uso
resultado = suma_naturales(10)
print(f"La suma de los primeros 10 números naturales es {resultado}")


"""
Este ejemplo muestra un bucle while que simula tirar un dado hasta que se obtenga un número específico.

Parameters:
    objetivo (int): El número objetivo a alcanzar.

Returns:
    int: La cantidad de intentos necesarios para alcanzar el objetivo.
"""
import random

def tirar_dado_hasta(objetivo):
    intentos = 0
    while True:
        intento = random.randint(1, 6)
        intentos += 1
        if intento == objetivo:
            return intentos

# Ejemplo de uso
objetivo = 6  # Queremos obtener un 6
intentos = tirar_dado_hasta(objetivo)
print(f"Se necesitaron {intentos} intentos para obtener un {objetivo}")

