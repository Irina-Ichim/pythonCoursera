import subprocess

""" 
Este archivo Python demuestra cómo realizar la gestión avanzada de subprocesos.
Incluye ejemplos de copia de archivos utilizando "copy" en Windows, obtención del separador de ruta del sistema,
ejecución de comandos en el shell, y espera de procesos secundarios con un tiempo de espera (timeout).
Además, muestra cómo capturar la salida y el código de retorno de un proceso secundario.
"""

# Ejemplo de gestión avanzada de subprocesos
def advanced_subprocess_management():
    # Comando para copiar un archivo (utilizando "copy" en Windows)
    source_file = "archivo_origen.txt"
    destination_file = "archivo_destino.txt"
    print(f"Copiando {source_file} a {destination_file}...\n")
    
    # Usar "copy" en Windows para copiar el archivo
    subprocess.run(["copy", source_file, destination_file], shell=True)
    print(f"{source_file} copiado a {destination_file}\n")
    
    # Obtener el separador de ruta del sistema
    path_separator = subprocess.os.pathsep
    print(f"Separador de ruta del sistema: {path_separator}\n")
    
    # Ejecutar "ls" en un sistema Unix (esto puede variar en Windows)
    print("Listando archivos en el directorio actual...\n")
    subprocess.run(["ls"], shell=True, text=True)
    
    # Esperar a que un proceso secundario termine con un tiempo de espera (timeout)
    print("Ejecutando un proceso con tiempo de espera...\n")
    result = subprocess.run(["sleep", "5"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=3)
    
    # Capturando la salida y el código de retorno
    std_out = result.stdout
    return_code = result.returncode
    
    print(f"Salida estándar:\n{std_out}")
    print(f"Código de retorno: {return_code}\n")
    
if __name__ == "__main":
    advanced_subprocess_management()
