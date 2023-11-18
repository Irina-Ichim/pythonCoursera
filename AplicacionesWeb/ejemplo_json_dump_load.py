import json

# Crear una lista de personas, cada una con información de contacto
personas = [
    {
        "nombre": "Juan",
        "edad": 30,
        "contacto": {"telefono": "555-1234", "email": "juan@example.com"}
    },
    {
        "nombre": "Maria",
        "edad": 25,
        "contacto": {"telefono": "555-5678", "email": "maria@example.com"}
    },
    {
        "nombre": "Carlos",
        "edad": 35,
        "contacto": {"telefono": "555-9876", "email": "carlos@example.com"}
    }
]

# Serializar la lista de personas a JSON y escribirla en un archivo
with open('personas.json', 'w') as file:
    json.dump(personas, file, indent=2)

# Deserializar el JSON desde el archivo a una lista de personas
with open('personas.json', 'r') as file:
    personas_deserializadas = json.load(file)

# Imprimir la lista de personas deserializada
print("Personas Deserializadas:")
for persona in personas_deserializadas:
    print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Contacto: {persona['contacto']}")

# Creamos una lista llamada personas, donde cada elemento es un diccionario que representa a una persona con su información de contacto.

# Utilizamos json.dump() para serializar la lista de personas y escribirla en un archivo llamado personas.json.

# Luego, usamos json.load() para leer el contenido de personas.json y deserializarlo de nuevo a una lista de personas llamada 
# personas_deserializadas.

# Finalmente, imprimimos la lista de personas deserializada.