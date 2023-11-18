from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(output_filename, content):
    # Create a SimpleDocTemplate object
    pdf = SimpleDocTemplate(output_filename)

    # Create a list to hold the flowables (elements) of the document
    story = []

    # Use the default sample stylesheet
    styles = getSampleStyleSheet()

    # Add a title to the document
    title = Paragraph("My PDF Report", styles['h1'])
    story.append(title)

    # Add a spacer
    story.append(Spacer(1, 12))

    # Add the content to the document
    content_paragraph = Paragraph(content, styles['BodyText'])
    story.append(content_paragraph)

    # Build the PDF document
    pdf.build(story)

if __name__ == "__main__":
    # Specify the output filename
    output_filename = "output.pdf"

    # Specify the content for the PDF
    pdf_content = """
    This is a sample PDF generated using ReportLab in Python.
    You can add more content here as needed.
    """

    # Generate the PDF
    generate_pdf(output_filename, pdf_content)

    print(f"PDF generated successfully: {output_filename}")


# Ejecuta este comando para generar tu pdf : python Pdf/generate_pdf.py
