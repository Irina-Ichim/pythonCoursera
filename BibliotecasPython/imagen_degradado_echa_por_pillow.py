from PIL import Image, ImageDraw, ImageFont

def create_gradient_image():
    # Crea una nueva imagen en blanco (RGB) de 400x200 píxeles
    image = Image.new("RGB", (400, 200))

    # Obtiene un objeto para dibujar en la imagen
    draw = ImageDraw.Draw(image)

    # Define un degradado de colores horizontal
    for x in range(400):
        r = int(255 * x / 400)
        g = int(255 * (1 - x / 400))
        b = 0
        draw.line([(x, 0), (x, 200)], fill=(r, g, b))

    # Agrega texto con efecto de sombra
    font = ImageFont.load_default()  # Utiliza la fuente predeterminada

    text = "Python Pillow"
    text_bbox = draw.textbbox((0, 0), text, font=font)

    # Posición del texto
    x = (400 - text_bbox[2]) // 2
    y = (200 - text_bbox[3]) // 2

    # Color del texto y sombra
    text_color = (255, 255, 255)
    shadow_color = (50, 50, 50)

    # Agrega sombra
    draw.text((x + 2, y + 2), text, font=font, fill=shadow_color)
    
    # Agrega texto principal
    draw.text((x, y), text, font=font, fill=text_color)

    # Guarda la imagen en un archivo llamado "gradient_text.png"
    image.save("gradient_text.png")

if __name__ == "__main__":
    create_gradient_image()

