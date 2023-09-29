"""
Nuevos strings para modificar un string mal escrito

El operador "in" verifica si una subcadena está presente en otra cadena.
El operador "not" se utiliza para negar esa condición.
"""

Message = "Me gustan las risas"
# message[13] = "o"
# print(message) # Los strings son inmutables, así que debes crear otra variable
New_message = Message[:15] + "o" + Message[16:]
print(New_message)

pets = "Cats @ dogs"
print(pets.index("@"))

print("dragons" in pets) #in lo usamos como metodo para los booleans

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
