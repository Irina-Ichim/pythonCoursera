from PIL import Image, ImageDraw, ImageFont

def create_image():
    # Crea una nueva imagen en blanco (RGB) de 300x300 píxeles
    image = Image.new("RGB", (300, 300), "white")

    # Obtiene un objeto para dibujar en la imagen
    draw = ImageDraw.Draw(image)

    # Dibuja un rectángulo rojo en el centro de la imagen
    draw.rectangle([(100, 100), (200, 200)], fill="red")

    # Agrega texto "Irina" en la imagen
    font = ImageFont.load_default()  # Utiliza la fuente predeterminada
    draw.text((110, 150), "Irina", font=font, fill="black")

    # Guarda la imagen en un archivo llamado "output.png"
    image.save("output.png")

if __name__ == "__main__":
    create_image()
