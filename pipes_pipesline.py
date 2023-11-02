# Conceptos de Pipes y Pipelines en la Línea de Comandos

# Los pipes (|) y las pipelines se utilizan para conectar comandos en la línea de comandos de Unix y Linux.

# Comando Pipe (|):
# El símbolo | se utiliza para conectar dos comandos, de modo que la salida del primero se convierte en la entrada del segundo.
# Ejemplo: comando1 | comando2

# Comandos Relevantes:

# 1. tr: Transformación de Texto
#    - El comando "tr" se utiliza para realizar transformaciones en texto, como cambiar o eliminar caracteres.
#    - Ejemplo: tr 'a' 'A' convertirá todas las letras minúsculas 'a' en mayúsculas 'A'.

# 2. sort: Ordenar Líneas
#    - El comando "sort" se utiliza para ordenar líneas de texto en orden alfabético o numérico.
#    - Puede ordenar líneas de texto en orden ascendente o descendente.

# 3. uniq: Filtrar Líneas Únicas
#    - El comando "uniq" se utiliza para filtrar o eliminar líneas duplicadas consecutivas en un flujo de texto.
#    - Puede mostrar líneas únicas o contar la cantidad de veces que aparece cada línea con la opción "-c".

# 4. head: Mostrar las Primeras Líneas
#    - El comando "head" se utiliza para mostrar las primeras líneas de un flujo de texto.
#    - Con la opción "-n", puedes especificar cuántas líneas deseas mostrar.

# 5. grep: Búsqueda de Patrones
#    - El comando "grep" se utiliza para buscar patrones en un flujo de texto y filtrar líneas que coincidan con el patrón.

# Uso de un Pipeline:
# En un pipeline, puedes combinar estos comandos para realizar tareas específicas.
# Por ejemplo, para contar cuántas veces aparece cada palabra en un archivo de texto:
# cat archivo.txt | tr ' ' '\n' | sort | uniq -c | sort -nr

# En este ejemplo, se lee el archivo de texto con "cat", se divide el texto en palabras con "tr", se ordenan alfabéticamente con "sort",
# se cuentan las ocurrencias con "uniq -c" y se ordenan en orden numérico inverso con "sort -nr".

# Los pipes y pipelines son fundamentales en la programación de scripts de shell y el procesamiento de datos en sistemas Unix y Linux.
