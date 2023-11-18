# Generación de Informes PDF con ReportLab en Python

En este tutorial, exploramos cómo utilizar la biblioteca ReportLab en Python para generar informes en formato PDF. Vamos a resumir los puntos clave que cubrimos:

## 1. Introducción a ReportLab

ReportLab es una biblioteca de Python que facilita la creación de documentos en formato PDF. En este caso, exploramos cómo crear un informe sobre una colección de frutas.

## 2. Uso de SimpleDocTemplate

Utilizamos la clase SimpleDocTemplate para construir nuestro informe PDF. Creamos un objeto `report` que actuará como generador del PDF con un nombre de archivo específico.

```python
from reportlab.platypus import SimpleDocTemplate

report = SimpleDocTemplate("/tmp/report.pdf")
```

## 3. Creación de Contenido del Informe

Introducimos los "Flowables", que son elementos individuales del informe que ReportLab organiza para formar el documento completo. Importamos las clases Paragraph, Spacer, Table e Image como ejemplos de Flowables.

```python
from reportlab.platypus import Paragraph, Spacer, Table, Image
```

## 4. Estilos del Informe

Obtenemos estilos de muestra utilizando getSampleStyleSheet para aplicar estilos a diferentes partes del informe.

```python
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()
```

## 5. Título del Informe

Creamos un título para el informe utilizando la clase Paragraph con el estilo de encabezado h1.

```python
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
```

## 6. Generación del Informe

Usamos el método build del objeto `report` para generar el PDF con el título del informe.

```python
report.build([report_title])
```

## 7. Visualización del Resultado

Finalmente, mencionamos que el PDF generado puede ser visualizado.

## Instalar

Para generar un PDF utilizando la biblioteca reportlab en Python, necesitarás tenerla instalada. Puedes instalarla usando el siguiente comando:

```
pip install reportlab

```
