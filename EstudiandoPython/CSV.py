import csv

# Datos a escribir en el archivo CSV
data = [
    ["Nombre", "Edad", "Ciudad"],
    ["Juan", 25, "Madrid"],
    ["Ana", 30, "Barcelona"],
    ["Carlos", 22, "Valencia"]
]

# Nombre del archivo CSV
file_name = "datos.csv"

# Abrir el archivo CSV en modo escritura
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Escribe los datos en el archivo
    for row in data:
        writer.writerow(row)

print(f'Se ha creado el archivo "{file_name}" con éxito.')
# Datos a escribir en el archivo CSV
new_data = [
    ["Sara", 28, "Sevilla"],
    ["Pedro", 35, "Málaga"]
]

# Abrir el archivo CSV en modo escritura y añadir datos
with open(file_name, mode='a', newline='') as file:  # Usamos 'a' para agregar (append)
    writer = csv.writer(file)

    # Escribe los nuevos datos en el archivo
    for row in new_data:
        writer.writerow(row)

print(f'Se han agregado nuevos datos al archivo "{file_name}" con éxito.')

# file.close() En este caso no es necesario por que se cierra cuando sale del with