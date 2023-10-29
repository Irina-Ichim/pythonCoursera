import re
# ejemplo básico de cómo filtrar archivos de registro utilizando expresiones regulares en Python.
# Función para filtrar archivos de registro
def filter_log_file(log_file_path, output_file_path, pattern):
    try:
        with open(log_file_path, 'r') as log_file, open(output_file_path, 'w') as output_file:
            for line in log_file:
                # Buscar el patrón en la línea de registro
                match = re.search(pattern, line)
                if match:
                    # Si se encuentra el patrón, escribir la línea en el archivo de salida
                    output_file.write(line)
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

# Ejemplo de uso
if __name__ == '__main__':
    log_file_path = 'archivo_de_registro.log'
    output_file_path = 'resultado_filtrado.log'
    
    # Define el patrón de expresión regular que deseas buscar en el archivo de registro
    pattern = r'(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}) ERROR: (.*)'
    
    # Llama a la función para filtrar el archivo de registro
    filter_log_file(log_file_path, output_file_path, pattern)
    print("Filtrado completado. El resultado se ha guardado en", output_file_path)
