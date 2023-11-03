import subprocess

# Comando "who" para obtener información de usuarios conectados
def who_command_example():
    print("Ejecutando el comando 'who' para obtener información de usuarios conectados...\n")
    result = subprocess.run(["who"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Capturando la salida estándar y la salida de error
    std_out = result.stdout
    std_err = result.stderr
    
    # Verificando el código de retorno (return code)
    return_code = result.returncode
    
    # Imprimiendo la salida estándar y el código de retorno
    print(f"Salida estándar (usuarios conectados):\n{std_out}")
    print(f"Código de retorno: {return_code}\n")
    
    # Verificando si hubo errores (salida de error)
    if std_err:
        print(f"Salida de error:\n{std_err}")

# Ejemplo de codificación de texto (utf-8) y decodificación
def utf8_decode_example():
    text = "¡Hola, mundo!"
    print(f"Texto original: {text}\n")
    
    # Codificación de texto a UTF-8
    encoded_text = text.encode("utf-8")
    print(f"Texto codificado en UTF-8: {encoded_text}\n")
    
    # Decodificación de UTF-8 a texto
    decoded_text = encoded_text.decode("utf-8")
    print(f"Texto decodificado: {decoded_text}\n")

# Ejemplo de la eliminación de un archivo con el comando "rm"
def rm_command_example():
    file_to_delete = "archivo_a_eliminar.txt"
    
    # Crear un archivo que se eliminará
    with open(file_to_delete, "w") as file:
        file.write("Este archivo se eliminará.")
    
    print(f"Archivo creado: {file_to_delete}\n")
    
    # Ejecutar el comando "rm" para eliminar el archivo
    subprocess.run(["rm", file_to_delete])
    print(f"Archivo {file_to_delete} eliminado con el comando 'rm'.")

if __name__ == "__main":
    who_command_example()
    utf8_decode_example()
    rm_command_example()

# Una matriz de bytes (byte array en inglés) es una secuencia de bytes, que son unidades de datos que representan información,
# como caracteres de texto, números, imágenes, sonido, o cualquier otro tipo de datos.
# Cada byte generalmente consta de 8 bits y puede representar valores en un rango de 0 a 255. 

# Las matrices de bytes son estructuras de datos utilizadas en programación para almacenar y manipular datos binarios,
# es decir, datos que no están necesariamente destinados a ser interpretados como texto o números,
# sino que pueden representar cualquier tipo de información. Algunos ejemplos de uso de matrices de bytes incluyen:

# 1. Almacenar y manipular archivos binarios, como imágenes, audio o archivos ejecutables.
# 2. Procesar datos de red, como paquetes de red.
# 3. Trabajar con datos codificados en formatos específicos, como codificación de imágenes (por ejemplo, JPEG) o formatos de archivo comprimidos (por ejemplo, ZIP).
# 4. Realizar operaciones criptográficas, ya que muchos algoritmos de cifrado operan a nivel de bytes.

# En muchos lenguajes de programación, incluido Python, existen estructuras de datos específicas para trabajar con matrices de bytes.
# En Python, puedes usar el tipo de datos `bytes` o `bytearray` para trabajar con matrices de bytes,
# dependiendo de si necesitas una matriz inmutable (bytes) o mutable (bytearray).

# En resumen, una matriz de bytes es una secuencia de datos binarios, donde cada elemento es un byte que puede representar
# cualquier tipo de información en forma de ceros y unos. Se utilizan para trabajar con datos binarios en programación.