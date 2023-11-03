# Explicación de la Redirección de Flujos en la Línea de Comandos

# 1. Redirección de salida (>): El operador > se utiliza para redirigir la salida estándar (stdout) hacia un archivo.
# Ejemplo:
# Este comando guarda la lista de archivos y directorios en un archivo llamado listado.txt.
print("Ejemplo 1: Redirección de salida (>)")
print("ls > listado.txt")

# 2. Redirección de salida (append) (>>): El operador >> se utiliza para agregar la salida estándar (stdout) a un archivo existente sin borrar su contenido anterior.
# Ejemplo:
# Este comando agrega "Nuevo contenido" al archivo archivo.txt sin borrar lo que ya estaba en el archivo.
print("\nEjemplo 2: Redirección de salida (append) (>>)")
print("echo 'Nuevo contenido' >> archivo.txt")

# 3. Redirección de entrada (<): El operador < se utiliza para redirigir la entrada estándar (stdin) desde un archivo.
# Ejemplo:
# Este comando ejecuta un programa llamado "programa" utilizando los datos del archivo entrada.txt como entrada.
print("\nEjemplo 3: Redirección de entrada (<)")
print("programa < entrada.txt")

# 4. Redirección de errores (2>): El operador 2> se utiliza para redirigir los mensajes de error (stderr) hacia un archivo.
# Ejemplo:
# Este comando redirige los mensajes de error generados por "comando" al archivo errores.txt.
print("\nEjemplo 4: Redirección de errores (2>)")
print("comando 2> errores.txt")

# 5. Descriptor de archivo: Los descriptores de archivo son números que identifican flujos de datos como stdin (0), stdout (1) y stderr (2).
# Ejemplo:
# Cuando se referencia el descriptor de archivo stderr (2) en una redirección, se utiliza el número "2".
print("\nEjemplo 5: Descriptor de archivo")
print("comando 2> errores.txt")

# Estos conceptos son esenciales para controlar cómo se manejan los flujos de entrada y salida en la línea de comandos.

# Recuerda que estos ejemplos son solo representaciones. Puedes ejecutar comandos similares en tu terminal.
