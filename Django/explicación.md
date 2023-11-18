# Django: Un Vistazo Rápido

En este artículo, exploraremos brevemente el marco web Django, que se utilizará en el proyecto de laboratorio al final de este módulo. Django es un marco web de pila completa escrito en Python. Aunque en este proyecto solo interactuarás con él a través de solicitudes HTTP, es fundamental comprender qué es y cuándo sería una buena herramienta para tu aplicación.

## Marco de Pila Completa

Un marco de pila completa maneja diferentes componentes típicos al crear una aplicación web. Contiene bibliotecas que te ayudan a manejar cada una de las piezas: escribir la lógica de tu aplicación, almacenar y recuperar datos, recibir solicitudes web y responder a ellas. Si necesitas construir una aplicación con un frontend web, el uso de un marco web como Django puede ahorrarte mucho tiempo y esfuerzo, ya que muchos desafíos ya están resueltos.

Los marcos web suelen dividirse en tres componentes básicos: (1) el código de la aplicación, donde agregarás toda la lógica de tu aplicación; (2) el almacenamiento de datos, donde configurarás qué datos deseas almacenar y cómo los estás almacenando; y (3) el servidor web, donde establecerás qué páginas son servidas por qué lógica.

Esta división ayuda a escribir código más modular, fomenta la reutilización de código y permite flexibilidad al ver y acceder a los datos.

## Decisiones y Características

Cuando escribes una aplicación web, debes tomar muchas decisiones. Confiar en un marco como Django es similar a usar bibliotecas externas para tu código. Hay muchas características que puedes usar fácilmente en lugar de escribir todo desde cero y volver a cometer los mismos errores que todos cometemos al escribir una aplicación web por primera vez.

Django tiene una gran cantidad de componentes útiles para construir sitios web. En el proyecto de laboratorio, Django se utilizará para servir el sitio web de la empresa, incluidas las opiniones de los clientes. Lo hace tomando la solicitud de una URL y analizándola mediante el módulo `urlresolver`. Este módulo interpreta las solicitudes de URL y las compara con una lista de patrones definidos. Si una URL coincide con un patrón, la solicitud se pasa a la función asociada, llamada vista. Esto te permite servir diferentes páginas según la URL solicitada.

## Interactuando con la Base de Datos

Django también puede manejar la lectura y escritura de datos desde una base de datos, lo que te permite almacenar y recuperar datos utilizados por tu aplicación. En el laboratorio, la base de datos contiene las opiniones de los clientes para la empresa. Cuando un usuario carga el sitio web, la lógica solicitará a la base de datos todas las opiniones de los clientes disponibles. Estas se recuperan y se formatean en una página web, que se sirve como respuesta a la solicitud de URL. Django facilita la interacción con datos almacenados en una base de datos mediante el uso de un mapeador objeto-relacional, o ORM.

## Manipulación de Datos con Django

Además, la aplicación Django en el laboratorio incluye un punto final que se puede utilizar para agregar nuevas opiniones de clientes a la base de datos. Este punto final está configurado para recibir datos en formato JSON, enviados a través de una solicitud HTTP POST. Los datos transmitidos se almacenarán en la base de datos y se agregarán a la lista de todas las opiniones. El marco incluso genera un formulario web interactivo que nos permite interactuar directamente con el punto final usando nuestro navegador, lo que puede ser muy útil para pruebas y depuración.

## Alternativas a Django

Django es solo uno de los muchos marcos web populares. Alternativas basadas en Python similares a Django incluyen Flask, Bottle, CherryPy y CubicWeb. También existen numerosos marcos escritos en otros lenguajes, no solo en Python.