import json

# Crear un diccionario que represente información sobre una persona
persona = {
    "nombre": "Juan",
    "edad": 25,
    "direccion": {"calle": "123 Main St", "ciudad": "Ciudad Ejemplo"}
}

# Serialización en JSON
with open('persona.json', 'w') as file:
    json.dump(persona, file, indent=2)

# Deserialización en JSON
with open('persona.json', 'r') as file:
    persona_deserializada = json.load(file)

# Imprimir el diccionario deserializado
print("Persona Deserializada:")
print(persona_deserializada)
