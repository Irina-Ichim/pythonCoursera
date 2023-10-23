import re

# Ejercicio 1: Validación de direcciones de correo electrónico
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Ejercicio 2: Búsqueda de números de teléfono
def find_phone_numbers(text):
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, text)

# Otros ejercicios aquí...

# Pruebas
if __name__ == "__main__":
    # Prueba del Ejercicio 1
    email = "user@example.com"
    if validate_email(email):
        print(f"{email} es una dirección de correo electrónico válida.")
    else:
        print(f"{email} no es una dirección de correo electrónico válida.")

    # Prueba del Ejercicio 2
    text = "Contact me at (123) 456-7890 or 987-654-3210."
    phone_numbers = find_phone_numbers(text)
    print("Números de teléfono encontrados:", phone_numbers)
    
    
 
def validate_date(date):
    pattern = r"\d{2}/\d{2}/\d{4}"
    return re.match(pattern, date) is not None

date = "12/31/2022"
if validate_date(date):
    print(f"{date} es una fecha válida.")
else:
    print(f"{date} no es una fecha válida.")   
