import xml.etree.ElementTree as ET

# Estructura de datos para libros
libros = ET.Element("libros")

libro1 = ET.SubElement(libros, "libro")
ET.SubElement(libro1, "titulo").text = "Python for Beginners"
ET.SubElement(libro1, "autor").text = "John Smith"
ET.SubElement(libro1, "anio").text = "2022"

libro2 = ET.SubElement(libros, "libro")
ET.SubElement(libro2, "titulo").text = "Data Science Handbook"
ET.SubElement(libro2, "autor").text = "Jane Doe"
ET.SubElement(libro2, "anio").text = "2021"

# Serialización en XML
tree = ET.ElementTree(libros)
tree.write("libros.xml")

# Deserialización en XML
tree = ET.parse("libros.xml")
root = tree.getroot()

# Imprimir la información de cada libro
print("Información de Libros:")
for libro in root.findall("libro"):
    titulo = libro.find("titulo").text
    autor = libro.find("autor").text
    anio = libro.find("anio").text
    print(f"Libro: {titulo}, Autor: {autor}, Año: {anio}")
