from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

def generate_pie_chart_report(output_file_path, fruit_inventory):
    # Crear el objeto Drawing
    drawing = Drawing(width=400, height=200)

    # Crear un objeto Pie y configurar datos y etiquetas
    report_pie = Pie(width=3*inch, height=3*inch)
    report_pie.data = list(fruit_inventory.values())
    report_pie.labels = list(fruit_inventory.keys())

    # Agregar el objeto Pie al objeto Drawing
    drawing.add(report_pie)

    # Configurar estilos y título
    styles = getSampleStyleSheet()
    report_title = Paragraph("Fruit Inventory Pie Chart", styles["h1"])

    # Crear el documento PDF y agregar elementos
    report = SimpleDocTemplate(output_file_path, pagesize=letter)
    report.build([report_title, drawing])

# Ejemplo de inventario de frutas
fruit_inventory = {
    "apples": 2,
    "bananas": 5,
    "cherries": 8,
    "durians": 3,
    "elderberries": 1,
    "figs": 1,
    "grapes": 13
}

# Generar el informe y guardar en un archivo PDF
output_file_path = "fruit_inventory_report.pdf"
generate_pie_chart_report(output_file_path, fruit_inventory)

