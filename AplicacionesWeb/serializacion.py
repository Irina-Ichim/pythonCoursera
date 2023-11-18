import json

# Datos de ejemplo: lista de diccionarios con información de estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 22, "cursos": ["Matemáticas", "Historia"]},
    {"nombre": "Carlos", "edad": 21, "cursos": ["Inglés", "Ciencias"]},
    {"nombre": "Elena", "edad": 23, "cursos": ["Programación", "Literatura"]}
]

# Función para serializar los datos en formato JSON
def serializar_datos(datos):
    return json.dumps(datos, indent=2)

# Función para deserializar los datos desde formato JSON
def deserializar_datos(datos_serializados):
    return json.loads(datos_serializados)

# Serializamos los datos y los escribimos en un archivo
datos_serializados = serializar_datos(estudiantes)
with open('estudiantes.json', 'w') as file:
    file.write(datos_serializados)

# Leemos los datos desde el archivo y los deserializamos
with open('estudiantes.json', 'r') as file:
    datos_deserializados = deserializar_datos(file.read())

# Imprimimos los datos originales y los datos deserializados para verificar
print("Datos Originales:")
print(estudiantes)

print("\nDatos Deserializados:")
print(datos_deserializados)


# En este ejercicio:

# 1. Creamos una lista de diccionarios llamada `estudiantes` con información de estudiantes.
# 2. Utilizamos la función `serializar_datos` para convertir la lista de diccionarios a una cadena JSON y escribimos esa cadena en un archivo 
# llamado `estudiantes.json`.
# 3. Luego, leemos la cadena JSON desde el archivo, utilizamos la función `deserializar_datos` para convertirla de nuevo en una lista de 
# diccionarios, y la almacenamos en la variable `datos_deserializados`.
# 4. Finalmente, imprimimos los datos originales y los datos deserializados para verificar que la información se ha mantenido.

# Este ejercicio te da práctica con la serialización y deserialización de datos utilizando el formato JSON. Puedes experimentar modificando
# la información de los estudiantes y observar cómo afecta la serialización y deserialización. ¡Hazme saber si tienes alguna pregunta!