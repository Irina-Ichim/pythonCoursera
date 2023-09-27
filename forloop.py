

# Ejemplo de bucle while
def ejemplo_while():
    contador = 0
    while contador < 5:
        print(f"Contador (while): {contador}")
        contador += 1

# Ejemplo de bucle for


def ejemplo_for():
    for i in range(5):
        print(f"Índice (for): {i}")

# Ejemplo de bucle for con lista


def ejemplo_for_con_lista():
    frutas = ["manzana", "banana", "cereza"]
    for fruta in frutas:
        print(f"Fruta (for): {fruta}")


# Llamada a las funciones de ejemplo
ejemplo_while()
print("\n" + "-" * 20 + "\n")  # Separador
ejemplo_for()
print("\n" + "-" * 20 + "\n")  # Separador
ejemplo_for_con_lista()
