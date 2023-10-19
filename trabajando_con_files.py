import os
import datetime

access_time = None  # Inicializamos access_time en None

# Verificar si el archivo existe
if os.path.exists("chuchy.txt"):
    print("El archivo existe.")
    
    # Obtener el tamaño del archivo
    file_size = os.path.getsize("chuchy.txt")
    print(f"Tamaño del archivo: {file_size} bytes")
    
    # Obtener la hora de acceso del archivo
    access_time = os.path.getatime("chuchy.txt")
    print(f"Hora de acceso del archivo: {access_time}")
else:
    print("El archivo no existe.")

# Acceder a access_time después del bloque condicional
if access_time is not None:
    access_time_readable = datetime.datetime.fromtimestamp(access_time)
    print(f"Hora de acceso del archivo (legible): {access_time_readable}")


file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
print("File not found")

# Obtener la ruta absoluta
ruta_absoluta = os.path.abspath("chuchy.txt")

# Imprimir la ruta absoluta
print("Ruta absoluta del archivo:", ruta_absoluta)

os.path.abspath("chuchy.txt")

