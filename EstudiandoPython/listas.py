# Listas en Python
# En Python, las listas son secuencias de datos definidas con corchetes cuadrados.

# Definición de una lista
mi_lista = ["This", "is", "a", "list"]

# Longitud de una lista
longitud_lista = len(mi_lista)  # Devuelve 4
print(f"Longitud de la lista: {longitud_lista}")

# Verificación de elementos en la lista
elemento_presente = "This" in mi_lista  # Devuelve True
print(f"¿El elemento 'This' está en la lista? {elemento_presente}")

# Indexación de listas
primer_elemento = mi_lista[0]  # Devuelve "This"
print(f"Primer elemento de la lista: {primer_elemento}")

# Similitudes entre listas y cadenas
# Las listas y las cadenas comparten propiedades como la iteración, la indexación, la longitud, la concatenación y la verificación de elementos.

# Ejemplo práctico
frutas = ["manzana", "naranja", "plátano"]
frutas.append("uva")  # Agrega "uva" a la lista de frutas
print(f"Lista de frutas actualizada: {frutas}")
