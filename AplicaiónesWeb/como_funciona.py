# -*- coding: utf-8 -*-

# Creamos un archivo para explicar el concepto de aplicaciones web y cómo operan.

# Abrimos un archivo en modo escritura ('w') y especificamos la codificación utf-8.
with open('explicacion_aplicaciones_web.txt', 'w', encoding='utf-8') as file:

    # Escribimos la introducción al concepto de aplicaciones web.
    file.write("Concepto de Aplicaciones Web y Cómo Operan\n\n")

    # Describimos la interacción entre el navegador web y el servidor.
    file.write("1. Interacción Navegador-Servidor:\n")
    file.write("- Cuando un usuario utiliza un sitio web, el navegador envía solicitudes HTTP al servidor.\n")
    file.write("- El servidor, a su vez, pasa estas solicitudes a la aplicación web que decide qué información mostrar.\n")
    file.write("- La aplicación web genera contenido en formato HTML y sirve cualquier otro dato necesario, como imágenes.\n\n")

    # Exploramos el concepto de servicios web y APIs.
    file.write("2. Servicios Web y APIs:\n")
    file.write("- Muchas aplicaciones web ofrecen APIs (Interfaces de Programación de Aplicaciones) para la interacción con scripts o programas.\n")
    file.write("- Estas aplicaciones web con APIs son conocidas como servicios web.\n")
    file.write("- En lugar de interactuar manualmente con una página web, se pueden enviar llamadas de API desde programas.\n\n")

    # Explicamos el papel de los puntos de acceso de API.
    file.write("3. Puntos de Acceso (Endpoints) de API:\n")
    file.write("- La parte del programa que escucha las llamadas de API se denomina punto de acceso de API.\n")
    file.write("- Es el lugar donde un programa se comunica con el servicio web.\n\n")

    # Destacamos la independencia del lenguaje en la interacción con servicios web.
    file.write("4. Interacción Independiente del Lenguaje:\n")
    file.write("- Al interactuar con un servicio web, no es necesario conocer el lenguaje de programación de la otra aplicación.\n")
    file.write("- La interacción se realiza mediante un protocolo especificado que ambas partes comprenden.\n\n")

    # Concluimos destacando la importancia de la comunicación basada en protocolos.
    file.write("5. Comunicación Basada en Protocolo:\n")
    file.write("- La interacción con servicios web se basa en un protocolo especificado, permitiendo una comunicación estandarizada.\n")
    file.write("\n¡Explora más allá para comprender cómo funciona esta interacción y cómo puedes utilizarla en tus propios proyectos!")

# Imprimimos un mensaje indicando que el archivo ha sido creado exitosamente.
print("Archivo 'explicacion_aplicaciones_web.txt' creado exitosamente.")
