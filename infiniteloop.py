# Ejemplo de bucle infinito y cómo salir de él

# Bucle infinito: Este bucle nunca se detendrá porque la condición siempre es True
while True:
    print("Este es un bucle infinito. Presiona Ctrl+C para detenerlo.")

# Para salir de un bucle infinito, puedes utilizar una declaración 'break' basada en una condición
contador = 0
while True:
    contador += 1
    print(f"Contador: {contador}")

    # Si la condición se cumple, salimos del bucle
    if contador >= 5:
        break

print("¡Salimos del bucle!")

# Otra forma de evitar bucles infinitos es asegurarte de que la condición cambie con el tiempo
limite = 10
numero = 1
while numero <= limite:
    print(f"Número: {numero}")
    numero += 1  # Aseguramos que la condición cambie en cada iteración

print("Fin del bucle")
