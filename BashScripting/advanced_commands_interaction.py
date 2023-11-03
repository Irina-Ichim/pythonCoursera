# Bash Scripting y Análisis de Registros en Linux

# Conceptos Clave:
# 1. Visualización de archivos de registro.
# 2. Extracción de información relevante con el comando 'cut'.
# 3. Identificación de eventos repetitivos con comandos 'cut', 'sort', 'uniq'.
# 4. Creación de scripts Bash para procesar múltiples archivos de registro.

# Ejemplo 1: Visualización de un archivo de registro en Bash.
# Utilizamos 'tail' para mostrar las últimas 10 líneas del archivo '/var/log/syslog'.

# Ejemplo 2: Extracción de información relevante.
# Utilizamos el comando 'cut' para dividir cada línea en campos utilizando un espacio como delimitador.
# Luego, imprimimos el campo número 5 y todo lo que le sigue.

# Ejemplo 3: Identificación de eventos repetitivos.
# Utilizamos una canalización de comandos que incluye 'cut', 'sort', 'uniq', y 'sort' nuevamente para contar y clasificar las líneas según su repetición.

# Ejemplo 4: Creación de un script Bash.
# Creamos un script Bash que procesa múltiples archivos de registro en '/var/log'.
# El script itera sobre los archivos que terminan en ".log" y muestra las cinco líneas más comunes de cada archivo.

# Observaciones:
# - Los scripts Bash son útiles para automatizar tareas y procesar registros en sistemas Linux.
# - Python también es una opción válida para tareas similares y se elige según las necesidades específicas.

# Ejemplo de script Bash para el procesamiento de registros.
# Consulta el tutorial para obtener detalles completos.

import os

# Archivo de registro de ejemplo (reemplace con su archivo de registro real)
log_file = "/var/log/syslog"

# Usamos 'tail' para mostrar las últimas 10 líneas del archivo de registro.
os.system(f"tail -n 10 {log_file}")

# Utilizamos 'cut' para extraer información relevante (campo número 5 y siguientes).
os.system(f"cut -d' ' -f5- {log_file}")

# Identificación de eventos repetitivos con 'cut', 'sort', 'uniq'.
os.system(f"cut -d' ' -f5- {log_file} | sort | uniq -c | sort -nr")

# Creación de un script Bash (consulte el tutorial para el script completo).
# Aquí mostramos un ejemplo simple.

bash_script = """
#!/bin/bash

# Nombre del archivo de registro
log_file="/var/log/syslog"

# Visualiza las últimas 10 líneas del archivo de registro
tail -n 10 "$log_file"

# Extrae información relevante
cut -d' ' -f5- "$log_file"

# Identifica eventos repetitivos
cut -d' ' -f5- "$log_file" | sort | uniq -c | sort -nr
"""

# Guardamos el script Bash en un archivo (opcional)
with open("registro_script.sh", "w") as script_file:
    script_file.write(bash_script)

# Fin del archivo Python
