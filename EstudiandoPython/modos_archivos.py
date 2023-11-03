# Modo 'r' - Lectura
with open('ejemplo_lectura.txt', 'r') as file:
    content = file.read()
    print(f'Contenido del archivo en modo lectura:\n{content}\n')

# Modo 'w' - Escritura (crea un nuevo archivo o sobrescribe el existente)
with open('ejemplo_escritura.txt', 'w') as file:
    file.write('Hola, este es un ejemplo de escritura en modo w.\n')
    file.write('Se sobrescribirá el contenido si el archivo ya existe.\n')

# Modo 'a' - Anexar (agregar contenido al final del archivo)
with open('ejemplo_anexar.txt', 'a') as file:
    file.write('Este contenido se añade al final del archivo.\n')
    file.write('El archivo se crea si no existe.\n')

# Modo 'r+' - Lectura y escritura
with open('ejemplo_lectura_escritura.txt', 'r+') as file:
    content = file.read()
    print(f'Contenido del archivo en modo lectura y escritura:\n{content}\n')

    # Mover el puntero al principio y escribir algo nuevo
    file.seek(0)
    file.write('¡Añadiendo contenido en modo r+!\n')

# Modo 'w+' - Lectura y escritura, truncando
with open('ejemplo_lectura_escritura_truncado.txt', 'w+') as file:
    # Escribe y lee contenido
    file.write('Hola, este es un ejemplo de escritura en modo w+.\n')
    file.seek(0)
    content = file.read()
    print(f'Contenido del archivo en modo lectura y escritura (truncado):\n{content}\n')

# Modo 'a+' - Lectura y anexar
with open('ejemplo_lectura_anexar.txt', 'a+') as file:
    # Escribe y lee contenido
    file.write('Este contenido se añade al final del archivo.\n')
    file.seek(0)
    content = file.read()
    print(f'Contenido del archivo en modo lectura y anexar:\n{content}\n')
