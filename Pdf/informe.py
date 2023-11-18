from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Datos de la colección de frutas
fruits = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

# Crear el archivo PDF
pdf_path = "/tmp/report.pdf"
report = SimpleDocTemplate(pdf_path)
styles = getSampleStyleSheet()

# Crear título del informe
title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

# Crear contenido del informe con datos de frutas
content = []
content.append(title)
content.append(Spacer(1, 12))  # Espaciador

for fruit, quantity in fruits.items():
    fruit_info = Paragraph(f"{fruit}: {quantity} units", styles["BodyText"])
    content.append(fruit_info)

# Construir el PDF
report.build(content)

print(f"Se ha generado el informe PDF en: {pdf_path}")

# Usa este comando para ver tu archivo  python Pdf/informe.py   
