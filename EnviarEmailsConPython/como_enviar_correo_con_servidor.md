## Enviando el Correo Electrónico a través de un Servidor SMTP

Como mencionamos, para enviar correos electrónicos, nuestras computadoras utilizan el 
Protocolo Simple de Transferencia de Correo (SMTP)
. Este protocolo especifica cómo las computadoras pueden entregar correos electrónicos entre sí. Hay ciertos pasos que deben seguirse para hacer esto correctamente. Pero, como de costumbre, no lo haremos manualmente; enviaremos el mensaje usando el 
módulo smtplib de Python
. Comencemos importando el módulo.

```python
import smtplib
```

Con `smtplib`, crearemos un objeto que representará nuestro servidor de correo y manejará el envío de mensajes a ese servidor. Si estás utilizando una computadora Linux, es posible que ya tengas un servidor SMTP configurado como postfix o sendmail. Pero tal vez no. Creemos un objeto `smtplib.SMTP` y tratemos de conectarnos a la máquina local.

```python
mail_server = smtplib.SMTP('localhost')
```

Oops, ¡error! Esto significa que no hay un servidor SMTP local configurado. Pero no te preocupes, aún puedes conectarte al servidor SMTP de tu correo electrónico personal. La mayoría de los servicios de correo electrónico personal tienen instrucciones para enviar correo electrónico a través de SMTP; simplemente busca el nombre de tu servicio de correo electrónico y "configuración de conexión SMTP".

Cuando configuras esto, hay algunas cosas que probablemente necesitarás hacer: utilizar un nivel de transporte seguro y autenticarte en el servicio utilizando un nombre de usuario y una contraseña. Veamos qué significa esto en la práctica.

Puedes conectarte a un servidor SMTP remoto utilizando Transport Layer Security (TLS). Una versión anterior del protocolo TLS se llamaba Secure Sockets Layer (SSL), y a veces verás TLS y SSL usados indistintamente. Este SSL/TLS es el mismo protocolo que se utiliza para agregar una capa de transmisión segura a HTTP, convirtiéndolo en HTTPS. Dentro de `smtplib`, hay dos clases para realizar conexiones con un servidor SMTP: La 
clase SMTP
 hará una conexión directa de SMTP, y la 
clase SMTP_SSL
 realizará una conexión de SMTP sobre SSL/TLS. Así:

```python
mail_server = smtplib.SMTP_SSL('smtp.example.com')
```

Si deseas ver los mensajes SMTP que se envían y reciben en segundo plano por el módulo `smtplib`, puedes configurar el nivel de depuración en el objeto SMTP o SMTP_SSL. Los ejemplos en esta lección no mostrarán la salida de depuración, ¡pero podría resultar interesante!

```python
mail_server.set_debuglevel(1)
```

Ahora que hemos establecido una conexión con el servidor SMTP, lo siguiente que debemos hacer es autenticarnos en el servidor SMTP. Por lo general, los proveedores de correo electrónico quieren que proporcionemos un nombre de usuario y una contraseña para conectarnos. Coloquemos la contraseña en una variable para que no sea visible en la pantalla.

```python
import getpass
mail_pass = getpass.getpass('Contraseña? ')
```

El ejemplo anterior utiliza el 
módulo getpass
 para que los transeúntes no vean la contraseña en la pantalla. ¡Ten cuidado! Sin embargo, la variable `mail_pass` sigue siendo simplemente una cadena común.

```python
print(mail_pass)
```

Ahora que tenemos el usuario y la contraseña de correo electrónico configurados, podemos autenticarnos en el servidor de correo electrónico utilizando el método 
`login`
 del objeto SMTP.

```python
mail_server.login(sender, mail_pass)
```

Si el intento de inicio de sesión tiene éxito, el método `login` devolverá una tupla con el 
código de estado SMTP
 y un mensaje que explica la razón del estado. Si el intento de inicio de sesión falla, el módulo generará una excepción 
SMTPAuthenticationError
.

¡Envío de tu mensaje!
¡Bien! Estamos conectados y autenticados en el servidor SMTP. Ahora, ¿cómo enviamos el mensaje?

```python
mail_server.send_message(message)
```

¡Bien, esa última parte fue bastante fácil! ¡Hicimos la parte difícil primero! El método 
`send_message`
 devuelve un diccionario de cualquier destinatario que no pudo recibir el mensaje. Nuestro mensaje se entregó correctamente, así que `send_message` devolvió un diccionario vacío. Finalmente, ahora que se envió el correo electrónico, cerremos la conexión con el servidor de correo.

```python
mail_server.quit()
```

¡Y ahí lo tienes! Hemos cubierto mucho en esta lección, así que hagamos un resumen. Primero, construimos un mensaje de correo electrónico utilizando el 
módulo de correo electrónico incorporado
 con la 
clase EmailMessage
. Luego, agregamos un archivo adjunto a nuestro mensaje con la ayuda del 
módulo incorporado mimetypes
. Finalmente, nos conectamos a un servidor SMTP y enviamos el correo electrónico utilizando la clase 
SMTP_SSL
 del módulo `smtplib`.

¿Tenías idea de que todo esto estaba sucediendo detrás de un simple mensaje de correo electrónico?
```
