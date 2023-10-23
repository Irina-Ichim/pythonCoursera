import re

# Expresiones regulares para buscar patrones específicos en cadenas de texto

print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))

def check_aei(text):
    result = re.search(r"a.e.i", text)
    return result is not None

print(check_aei("academia"))   # True
print(check_aei("aerial"))     # False
print(check_aei("paramedic"))  # True

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))  # Uso de re.IGNORECASE para hacer la búsqueda insensible a mayúsculas y minúsculas
