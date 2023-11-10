"""Busqueda lineal"""

def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i  # Devuelve la posición si se encuentra el elemento
    return -1  # Retorna -1 si el elemento no está en la lista

# Ejemplo de uso
mi_lista = [1, 3, 5, 7, 9, 11, 13, 15]
elemento_objetivo = 7

resultado = busqueda_lineal(mi_lista, elemento_objetivo)

if resultado != -1:
    print(f"El elemento {elemento_objetivo} está en la posición {resultado}.")
else:
    print(f"El elemento {elemento_objetivo} no está en la lista.")

# Busqueda binaria

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio  # Devuelve la posición si se encuentra el elemento
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # Retorna -1 si el elemento no está en la lista

# Asegurémonos de que la lista esté ordenada para la búsqueda binaria
mi_lista_ordenada = sorted([15, 7, 3, 1, 11, 5, 13, 9])
elemento_objetivo = 11

resultado = busqueda_binaria(mi_lista_ordenada, elemento_objetivo)

if resultado != -1:
    print(f"El elemento {elemento_objetivo} está en la posición {resultado}.")
else:
    print(f"El elemento {elemento_objetivo} no está en la lista.")
