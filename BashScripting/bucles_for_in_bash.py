# Explicación de los bucles for en Bash y ejemplos traducidos a Python

# Ejemplo 1: Iterar sobre una lista de elementos en Bash
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

# Ejemplo 2: Renombrar archivos en Bash
import os

# Supongamos que tenemos archivos como archivo1.txt, archivo2.txt, archivo3.txt
for numero in range(1, 4):
    archivo_original = f"archivo{numero}.txt"
    nuevo_nombre = f"archivo{numero}_nuevo.txt"
    os.rename(archivo_original, nuevo_nombre)
    print(f"Se ha renombrado {archivo_original} a {nuevo_nombre}")

# Ejemplo 3: Copiar archivos en Bash
import shutil
import glob

for archivo in glob.glob("archivo*.txt"):
    nuevo_nombre = f"copia_{archivo}"
    shutil.copy(archivo, nuevo_nombre)
    print(f"Se ha copiado {archivo} a {nuevo_nombre}")

# Ejemplo 4: Procesar archivos en un directorio en Bash
import os

directorio = "/ruta/al/directorio/"
for archivo in os.listdir(directorio):
    ruta_completa = os.path.join(directorio, archivo)
    print(f"Procesando {ruta_completa}")
    # Agrega aquí el código para procesar cada archivo

# Ejemplo 5: Usar un rango en Bash
for numero in range(1, 6):
    print(f"Número: {numero}")

# Ejemplo 6: Renombrar archivos en Bash y generar código Python
import os

# Nombre del archivo Python donde escribiremos la salida
output_file = "salida.py"

# Abre el archivo Python para escritura
with open(output_file, "w") as python_file:
    for numero in range(1, 4):
        archivo_original = f"archivo{numero}.txt"
        nuevo_nombre = f"archivo{numero}_nuevo.txt"
        
        # Renombra el archivo
        os.rename(archivo_original, nuevo_nombre)

        # Escribe la salida en el archivo Python
        python_file.write("import os\n")
        python_file.write(f"archivo_original = '{archivo_original}'\n")
        python_file.write(f"nuevo_nombre = '{nuevo_nombre}'\n")
        python_file.write(f"os.rename(archivo_original, nuevo_nombre)\n")
        python_file.write(f"print(f'Se ha renombrado {archivo_original} a {nuevo_nombre}')\n")

