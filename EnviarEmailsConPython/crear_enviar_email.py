import smtplib
from email.message import EmailMessage
import mimetypes
import os.path
import getpass

def create_message(sender, recipient, subject, body, attachment_path=None):
    # Crear un objeto EmailMessage
    message = EmailMessage()
    message.set_content(body)

    # Establecer remitente y destinatario
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject

    # Adjuntar archivo si se proporciona una ruta de archivo
    if attachment_path:
        attach_file(message, attachment_path)

    return message

def attach_file(message, attachment_path):
    # Obtener el tipo MIME del archivo adjunto
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    # Leer el archivo adjunto y agregarlo al mensaje
    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=os.path.basename(attachment_path))

def send_email(sender, password, recipient, message):
    # Conectar al servidor SMTP (en este caso, usamos Gmail)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # Iniciar sesión en el servidor SMTP
        server.login(sender, password)

        # Enviar el mensaje
        server.send_message(message)

if __name__ == "__main__":
    # Configuración de correo electrónico
    sender_email = "tu_correo@gmail.com"
    recipient_email = "correo_destino@example.com"
    email_subject = "Prueba de Correo desde Python"
    email_body = "¡Hola! Esto es una prueba de enviar correos desde Python."
    attachment_path = "ruta/al/archivo/adjunto.txt"  # Cambiar a la ruta de tu archivo adjunto

    # Obtener la contraseña de forma segura
    email_password = getpass.getpass("Contraseña para {}:".format(sender_email))

    # Crear el mensaje de correo electrónico
    email_message = create_message(sender_email, recipient_email, email_subject, email_body, attachment_path)

    # Enviar el correo electrónico
    send_email(sender_email, email_password, recipient_email, email_message)

    print("Correo enviado exitosamente.")
