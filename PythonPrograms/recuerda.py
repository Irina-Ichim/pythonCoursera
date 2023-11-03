"""
Este programa demuestra el uso de la función type() para determinar el tipo de dato de las variables.

- La variable 'texto' contiene una cadena de texto.
- La variable 'numero' contiene un número entero.
- La variable 'decimal' contiene un número de punto flotante.

Se utiliza la función type() para imprimir el tipo de dato de cada variable y se proporciona una descripción para cada uno de ellos.
"""
texto = "Hola"
numero = 5
decimal = 3.14

print(type(texto))    # <class 'str'> (str es para string)
print(type(numero))   # <class 'int'> (int es para integer)
print(type(decimal))  # <class 'float'> (float es para número de punto flotante)

