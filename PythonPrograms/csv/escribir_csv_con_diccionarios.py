import csv

# Datos a escribir en el archivo CSV
data = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 30, "Ciudad": "Barcelona"},
    {"Nombre": "Carlos", "Edad": 22, "Ciudad": "Valencia"}
]

# Nombre del archivo CSV
file_name = "datos_dict.csv"

# Nombres de las columnas (encabezados)
fieldnames = ["Nombre", "Edad", "Ciudad"]

# Abre el archivo CSV para escritura
with open(file_name, mode='w', newline='') as file:
    # Crea un escritor de CSV que interpreta los diccionarios
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Escribe los encabezados
    writer.writeheader()
    
    # Escribe los datos desde la lista de diccionarios
    for row in data:
        writer.writerow(row)

# Abre el archivo CSV para lectura y muestra su contenido
with open(file_name, mode='r') as file:
    # Crea un lector de CSV
    reader = csv.DictReader(file)
    
    # Imprime los encabezados
    print(reader.fieldnames)
    
    # Lee y muestra cada fila de datos
    for row in reader:
        print(row)

