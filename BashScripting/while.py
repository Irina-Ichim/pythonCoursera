# Explicación del bucle 'while' en Bash

# En Bash, el bucle 'while' se utiliza para repetir comandos mientras una condición sea verdadera.

# Sintaxis básica del bucle 'while' en Bash:
# while [condición]
# do
#     # Comandos a ejecutar
# done

# Ejemplo de bucle 'while' en Bash:
counter = 1
while counter <= 5:
    print(f"Iteración {counter}: Hola, mundo!")
    counter += 1

# El bucle continuará ejecutándose mientras la condición (counter <= 5) sea verdadera.
