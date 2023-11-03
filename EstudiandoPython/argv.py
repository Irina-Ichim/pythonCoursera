import sys

# La variable sys.argv es una lista que contiene los argumentos de la línea de comandos.
# El primer elemento (sys.argv[0]) es el nombre del propio script.
# Los argumentos pasados por el usuario comienzan a partir del segundo elemento en adelante.

# Mostrar el nombre del script
print("Nombre del script:", sys.argv[0])

# Mostrar todos los argumentos pasados por el usuario
print("Argumentos pasados por el usuario:", sys.argv[1:])

# En linux y mac usan el $? para verificar el estado de salida
# En windows usan el comando %errorlevel%

# El comando "wc" es una utilidad de línea de comandos que se encuentra comúnmente en sistemas tipo Unix y sistemas Unix-like, como Linux y macOS. 
# "wc" es una abreviatura de "word count" (conteo de palabras), pero su funcionalidad va más allá de contar palabras;
# se utiliza para contar líneas, palabras y caracteres en un archivo de texto o en la entrada de texto proporcionada por el usuario.
# Algunas de las opciones comunes de "wc" incluyen:

# -l: Muestra el número de líneas en el archivo.
# -w: Muestra el número de palabras en el archivo.
# -c: Muestra el número de bytes en el archivo.

# Si deseas contar líneas, palabras o caracteres en un archivo de texto en Windows,
# puedes utilizar el comando "find" junto con el comando "certutil", que está disponible en Windows. Aquí hay algunos ejemplos:
    
#     Contar líneas en un archivo:
#         find /c /v "" mi_archivo.txt

#     Contar palabras en un archivo:
#         certutil -f -i:mi_archivo.txt

#     Contar caracteres en un archivo:
#         certutil -encodehex -f mi_archivo.txt | find /c /v ""
