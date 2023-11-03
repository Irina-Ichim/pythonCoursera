#No ejecutes el archivo
# Modo 'r' - Lectura
nombre_archivo = 'mi_archivo.txt'

try:
    with open(nombre_archivo, 'r') as file:
        contenido = file.read()
        print(f'Contenido del archivo "{nombre_archivo}":\n{contenido}')
except FileNotFoundError:
    print(f'El archivo "{nombre_archivo}" no fue encontrado.')
except Exception as e:
    print(f'Ocurrió un error: {e}')

# leer y modificar
nombre_archivo = 'mi_archivo.txt'

try:
    with open(nombre_archivo, 'r+') as file:
        # Leer contenido
        contenido = file.readlines()
        print(f'Contenido actual del archivo "{nombre_archivo}":\n{contenido}')

        # Modificar la línea 3 (indexado comienza desde 0)
        if len(contenido) >= 3:
            contenido[2] = 'Esta es la nueva línea 3.\n'

        # Volver al principio y escribir el contenido modificado
        file.seek(0)
        file.writelines(contenido)

        print(f'Contenido modificado del archivo "{nombre_archivo}":\n{file.read()}')
except FileNotFoundError:
    print(f'El archivo "{nombre_archivo}" no fue encontrado.')
except Exception as e:
    print(f'Ocurrió un error: {e}')
    
#eliminar archivo

import os

nombre_archivo = 'mi_archivo.txt'

try:
    # Verificar si el archivo existe antes de intentar eliminarlo
    if os.path.exists(nombre_archivo):
        # Eliminar el archivo
        os.remove(nombre_archivo)
        print(f'El archivo "{nombre_archivo}" ha sido eliminado.')
    else:
        print(f'El archivo "{nombre_archivo}" no existe.')
except Exception as e:
    print(f'Ocurrió un error: {e}')

# Eliminar linea dentro de archivo
nombre_archivo = 'mi_archivo.txt'
linea_a_eliminar = 3  # Por ejemplo, eliminar la línea 3

try:
    with open(nombre_archivo, 'r') as file:
        # Leer todas las líneas
        lineas = file.readlines()

    # Verificar si la línea a eliminar está dentro del rango
    if 1 <= linea_a_eliminar <= len(lineas):
        # Eliminar la línea deseada
        del lineas[linea_a_eliminar - 1]

        # Escribir las líneas restantes de vuelta al archivo
        with open(nombre_archivo, 'w') as file:
            file.writelines(lineas)
        
        print(f'La línea {linea_a_eliminar} ha sido eliminada del archivo "{nombre_archivo}".')
    else:
        print(f'La línea {linea_a_eliminar} está fuera del rango de líneas en el archivo.')
except FileNotFoundError:
    print(f'El archivo "{nombre_archivo}" no fue encontrado.')
except Exception as e:
    print(f'Ocurrió un error: {e}')

