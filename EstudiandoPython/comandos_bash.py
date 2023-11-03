# Comandos en Bash
comandos = {
    'echo': 'Muestra texto o variables en la consola.',
    'cat': 'Muestra el contenido de archivos de texto o concatena archivos.',
    'ls': 'Lista archivos y directorios en el directorio actual.',
    'chmod': 'Cambia los permisos de acceso a archivos o directorios.',
    'mkdir': 'Crea un nuevo directorio.',
    'cd': 'Cambia el directorio actual al especificado.',
    'cd..': 'Retrocede un directorio en la jerarquía.',
    'pwd': 'Muestra la ruta completa del directorio actual.',
    'cp': 'Copia archivos o directorios de un lugar a otro.',
    'touch': 'Crea un nuevo archivo vacío.',
    'ls -l': 'Lista archivos y directorios en un formato largo que muestra detalles como permisos y tamaño.',
    'ls -la': 'Lista archivos y directorios, incluyendo los ocultos (los que comienzan con un punto).',
    'mv': 'Mueve o renombra archivos y directorios.',
    'rm': 'Elimina archivos o directorios.',
    'rmdir': 'Elimina directorios vacíos.',
    'man': 'Muestra el manual de uso de un comando, proporcionando información detallada sobre su funcionamiento y opciones.'
}

# Imprimir explicaciones de los comandos
for comando, descripcion in comandos.items():
    print(f'{comando}: {descripcion}')
