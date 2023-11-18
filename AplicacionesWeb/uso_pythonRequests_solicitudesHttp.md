# Uso de Python Requests para Solicitudes HTTP

En este documento, exploraremos algunas operaciones útiles al utilizar la biblioteca `requests` en Python para realizar solicitudes HTTP.

## Verificar si la Solicitud fue Exitosa

Podemos utilizar el atributo `Response.ok` para verificar si la respuesta fue exitosa:

```python
>>> response.ok
True
```

Este atributo devuelve `True` si la respuesta fue exitosa y `False` si no lo fue.

## Obtener el Código de Estado HTTP

Podemos obtener el código de estado HTTP de la respuesta con `Response.status_code`:

```python
>>> response.status_code
200
```

Un código de estado `200` indica una solicitud exitosa.

## Manejo de Errores

Es importante verificar si la respuesta fue exitosa antes de procesarla. Podemos utilizar la siguiente lógica:

```python
response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))
```

Sin embargo, la biblioteca `requests` proporciona una alternativa más simple con `Response.raise_for_status()`:

```python
response = requests.get(url)
response.raise_for_status()
```

Este método genera una excepción `HTTPError` solo si la respuesta no fue exitosa.

---

Recuerda siempre verificar el estado de la respuesta antes de procesarla más a fondo para garantizar un código robusto y mantenible.

### Métodos HTTP: GET y POST

El protocolo HTTP (HyperText Transfer Protocol) admite varios métodos para interactuar con recursos web. En este resumen, nos enfocaremos en los dos métodos más comunes: GET y POST.

#### HTTP GET Method:

El método GET se utiliza para recuperar información de un servidor web. Al realizar una solicitud GET, estás solicitando que el servidor te entregue el recurso especificado. Puedes incluir parámetros en la URL para personalizar tu solicitud.

Ejemplo de solicitud GET con parámetros:

```python
p = {"search": "grey kitten", "max_results": 15}
response = requests.get("https://example.com/path/to/api", params=p)
```

En este caso, se construye una cadena de consulta en la URL con los parámetros proporcionados en el diccionario `p`.

#### HTTP POST Method:

El método POST se utiliza para enviar datos a un servidor web. Comúnmente se utiliza al enviar datos de formularios web. En una solicitud POST, los datos se envían en el cuerpo del mensaje HTTP en lugar de en la URL.

Ejemplo de solicitud POST con datos en el cuerpo del mensaje:

```python
p = {"description": "white kitten", "name": "Snowball", "age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)
```

Aquí, el diccionario `p` se envía como datos en el cuerpo de la solicitud POST.

#### JSON en Solicitudes POST:

Es común enviar y recibir datos en formato JSON. La biblioteca `requests` facilita la conversión directa utilizando el parámetro `json`.

```python
response = requests.post("https://example.com/path/to/api", json=p)
```

En este caso, los datos en formato JSON se colocan en el cuerpo del mensaje, lo que es útil al trabajar con servicios web que esperan datos en ese formato.

#### Verificación de Respuestas:

Para asegurarse de que una solicitud se completó con éxito, se pueden realizar verificaciones en la respuesta. La propiedad `response.ok` devuelve `True` si la respuesta fue exitosa, y `False` de lo contrario. También se puede revisar el código de estado HTTP con `response.status_code`.

```python
if not response.ok:
    raise Exception("GET/POST failed with status code {}".format(response.status_code))
```

Otra opción es utilizar el método `response.raise_for_status()`, que generará una excepción `HTTPError` solo si la respuesta no fue exitosa.

```python
response.raise_for_status()
```

Estos métodos son esenciales para escribir código robusto y manejar adecuadamente las respuestas de las solicitudes. Puedes explorar más sobre estas funcionalidades en la [documentación de Requests](https://docs.python-requests.org/en/latest/).

Este resumen proporciona una visión general de los métodos HTTP GET y POST con la biblioteca `requests`. Si tienes alguna pregunta específica o necesitas más detalles, no dudes en preguntar.