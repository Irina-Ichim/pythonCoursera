import re

# Ejemplo 1: Coincidir con una palabra específica
texto = "Hola, ¿cómo estás?"
patron = r'cómo'
resultado = re.search(patron, texto)
if resultado:
    print("Ejemplo 1: Coincide con 'cómo'")
else:
    print("Ejemplo 1: No coincide")

# Ejemplo 2: Coincidir con un número de teléfono en formato (123) 456-7890
texto = "Mi número de teléfono es (123) 456-7890."
patron = r'\(\d{3}\) \d{3}-\d{4}'
resultado = re.search(patron, texto)
if resultado:
    print("Ejemplo 2: Número de teléfono encontrado:", resultado.group())
else:
    print("Ejemplo 2: Número de teléfono no encontrado")

# Ejemplo 3: Coincidir con una dirección de correo electrónico
texto = "Mi correo es ejemplo@dominio.com"
patron = r'\S+@\S+\.\S+'
resultado = re.search(patron, texto)
if resultado:
    print("Ejemplo 3: Dirección de correo electrónico encontrada:", resultado.group())
else:
    print("Ejemplo 3: Dirección de correo electrónico no encontrada")

# Ejemplo 4: Grupos de captura
texto = "Mi nombre es Juan Pérez y mi número de teléfono es (123) 456-7890."
patron = r'Mi nombre es (\w+ \w+) y mi número de teléfono es \((\d{3})\) (\d{3}-\d{4})'
resultado = re.search(patron, texto)
if resultado:
    nombre = resultado.group(1)
    area = resultado.group(2)
    numero = resultado.group(3)
    print("Ejemplo 4: Nombre:", nombre)
    print("Área:", area)
    print("Número:", numero)

# Ejemplo 5: Uso de findall para encontrar todas las coincidencias
texto = "Los números en el texto son 42, 101, 7 y 12345."
patron = r'\d+'
resultados = re.findall(patron, texto)
print("Ejemplo 5: Números encontrados:", resultados)

