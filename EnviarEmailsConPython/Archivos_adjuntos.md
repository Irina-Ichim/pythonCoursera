## Archivos Adjuntos y Contenido Multimedia

### Agregar Archivos Adjuntos

Recuerda, los mensajes de correo electrónico están compuestos completamente por cadenas de texto. Cuando agregas un archivo adjunto a un correo electrónico, sea cual sea el tipo de archivo, se codifica como una forma de texto. El estándar Multipurpose Internet Mail Extensions (MIME) se utiliza para codificar todo tipo de archivos como cadenas de texto que se pueden enviar por correo electrónico.

Comencemos y desglosemos cómo funciona.

Para que el destinatario de tu mensaje entienda qué hacer con un archivo adjunto, necesitas etiquetar el archivo adjunto con un tipo y subtipo MIME para decirles qué tipo de archivo estás enviando. La Internet Assigned Numbers Authority (IANA) (
iana.org
) aloja un registro de 
tipos MIME válidos
. Si conoces el tipo y subtipo correctos de los archivos que enviarás, puedes usar esos valores directamente. Si no lo sabes, ¡puedes utilizar el módulo mimetypes de Python para hacer una buena suposición!

```python
import os.path
attachment_path = "/tmp/example.png"
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
```

Finalmente, agreguemos el archivo adjunto a nuestro mensaje y veamos cómo se ve:

```python
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))
```

El mensaje completo aún se puede serializar como una cadena de texto, ¡incluyendo la imagen que adjuntamos! El mensaje de correo electrónico en su conjunto tiene el tipo MIME "multipart/mixed". Cada parte del mensaje tiene su propio tipo MIME. El cuerpo del mensaje sigue ahí como una parte "text/plain", y el archivo adjunto de la imagen es una parte "image/png". ¡Genial!

