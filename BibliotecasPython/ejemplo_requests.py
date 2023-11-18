import requests

# URL de la API de JSONPlaceholder para obtener la lista de posts
url = 'https://jsonplaceholder.typicode.com/posts'

# Realizar una solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Analizar la respuesta JSON
    posts = response.json()

    # Mostrar los primeros tres posts como ejemplo
    print("Primeros tres posts:")
    for post in posts[:3]:
        print(f"ID: {post['id']}, Título: {post['title']}")
else:
    # Mostrar un mensaje si la solicitud no fue exitosa
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
    
    
# ejemplo simple para realizar una solicitud HTTP utilizando la biblioteca requests en Python. En este caso, haremos una solicitud GET a la 
# API pública de JSONPlaceholder, que es una API de prueba gratuita para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en 
# recursos de tipo "posts".
