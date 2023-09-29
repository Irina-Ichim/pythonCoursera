"""
Este archivo de Python proporciona ejemplos de indexación y slicing de cadenas.

"""

def ejemplo_indexacion_cadenas():
    """
    Este ejemplo muestra cómo acceder a caracteres individuales en una cadena mediante indexación.

    Returns:
        str: Una cadena que resume los conceptos de indexación.
    """
    mensaje = "Python es genial!"

    primer_caracter = mensaje[0]
    ultimo_caracter = mensaje[-1]

    return f"Primer carácter: {primer_caracter}, Último carácter: {ultimo_caracter}"


def ejemplo_slicing_cadenas():
    """
    Este ejemplo muestra cómo utilizar slicing para obtener porciones de una cadena.

    Returns:
        str: Una cadena que resume los conceptos de slicing.
    """
    fruta = "ManzanaRoja"

    subcadena1 = fruta[2:6]
    subcadena2 = fruta[:6]
    subcadena3 = fruta[6:]

    return f"Subcadena 1: {subcadena1}, Subcadena 2: {subcadena2}, Subcadena 3: {subcadena3}"


if __name__ == "__main__":
    print("Ejemplo de Indexación:")
    print(ejemplo_indexacion_cadenas())

    print("\nEjemplo de Slicing:")
    print(ejemplo_slicing_cadenas())
