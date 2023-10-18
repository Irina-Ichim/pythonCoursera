# Ejemplos de manipulación de archivos en Python

# Método read()
with open('archivo.txt', 'r') as file:
    content = file.read()
    print(content)

# Método readline()
with open('archivo.txt', 'r') as file:
    line = file.readline()
    print(line)

# Método write()
with open('nuevo_archivo.txt', 'w') as file:
    file.write('Hola, este es un nuevo ejemplo.')

# Método seek()
with open('archivo.txt', 'r') as file:
    file.seek(5)
    data = file.read()
    print(data)

# Método tell()
with open('archivo.txt', 'r') as file:
    position = file.tell()
    print(f'Posición actual: {position}')

# Método writelines()
with open('lineas.txt', 'w') as file:
    lines = ['Línea 1\n', 'Línea 2\n', 'Línea 3\n']
    file.writelines(lines)

# Método truncate()
with open('archivo.txt', 'r+') as file:
    file.truncate(10)  # Redimensiona el archivo a 10 bytes

# Método flush()
with open('archivo.txt', 'w') as file:
    file.write('Esto se escribirá en el archivo.')
    file.flush()  # Asegura que los datos se escriban en el disco

# Método readable()
with open('archivo.txt', 'r') as file:
    print(file.readable())  # Devuelve True

# Método writable()
with open('archivo.txt', 'w') as file:
    print(file.writable())  # Devuelve True
