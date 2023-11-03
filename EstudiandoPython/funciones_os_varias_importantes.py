import os

# Obtener el directorio actual
directorio_actual = os.getcwd()
print("Directorio actual:", directorio_actual)

# Cambiar el directorio de trabajo
nuevo_directorio = "C:/Ruta/Al/Nuevo/Directorio"
os.chdir(nuevo_directorio)
print("Directorio actual después del cambio:", os.getcwd())

# Listar archivos y directorios en un directorio
archivos_en_directorio = os.listdir(os.getcwd())
print("Archivos y directorios en el directorio actual:", archivos_en_directorio)

# Crear un nuevo directorio
nuevo_directorio = "C:/Ruta/Al/Nuevo/Directorio2"
os.mkdir(nuevo_directorio)
print("Directorio creado:", nuevo_directorio)

# Comprobar si un directorio existe
directorio_a_verificar = "C:/Ruta/Al/Nuevo/Directorio2"
if os.path.exists(directorio_a_verificar):
    print(f"El directorio {directorio_a_verificar} existe.")
else:
    print(f"El directorio {directorio_a_verificar} no existe.")

# Eliminar un archivo
archivo_a_eliminar = "archivo_a_eliminar.txt"
if os.path.exists(archivo_a_eliminar):
    os.remove(archivo_a_eliminar)
    print(f"Archivo {archivo_a_eliminar} eliminado.")
else:
    print(f"El archivo {archivo_a_eliminar} no existe.")

# Eliminar un directorio vacío
directorio_a_eliminar = "C:/Ruta/Al/Nuevo/Directorio2"
if os.path.exists(directorio_a_eliminar):
    os.rmdir(directorio_a_eliminar)
    print(f"Directorio {directorio_a_eliminar} eliminado.")
else:
    print(f"El directorio {directorio_a_eliminar} no existe.")

# Eliminar un directorio y su contenido (recursivamente)
import shutil
directorio_a_eliminar = "C:/Ruta/Al/Nuevo/Directorio2"
if os.path.exists(directorio_a_eliminar):
    shutil.rmtree(directorio_a_eliminar)
    print(f"Directorio {directorio_a_eliminar} y su contenido eliminados.")
else:
    print(f"El directorio {directorio_a_eliminar} no existe.")
