# Modos de apertura de archivos en Python

# Modo 'b' - Binario
with open('imagen.png', 'rb') as file:
    contenido_binario = file.read()
    print(f'Contenido binario del archivo "imagen.png":\n{contenido_binario}\n')

# Modo 't' - Texto (por defecto)
with open('archivo.txt', 'rt') as file:
    contenido_texto = file.read()
    print(f'Contenido de texto del archivo "archivo.txt":\n{contenido_texto}\n')

# Modo '+' - Actualización (lectura y escritura)
with open('archivo.txt', 'r+') as file:
    contenido = file.read()
    print(f'Contenido actual del archivo "archivo.txt":\n{contenido}')

    # Agregar nueva línea al final
    file.write('\nNueva línea agregada en modo r+.\n')

    # Leer y mostrar el contenido actualizado
    file.seek(0)
    contenido_actualizado = file.read()
    print(f'Contenido actualizado del archivo "archivo.txt":\n{contenido_actualizado}\n')

# Modo 'x' - Creación exclusiva
try:
    with open('nuevo_archivo.txt', 'x') as file:
        file.write('Contenido del nuevo archivo.\n')
        print(f'Archivo "nuevo_archivo.txt" creado con éxito.')
except FileExistsError:
    print('El archivo "nuevo_archivo.txt" ya existe. No se puede crear.')

