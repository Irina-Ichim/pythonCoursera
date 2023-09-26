"""
Este ejemplo muestra cómo obtener el valor Unicode de un carácter en Python.

Parameters:
    char (str): El carácter del que deseas obtener el valor Unicode.

Returns:
    int: El valor Unicode del carácter.
"""
def obtener_valor_unicode(char):
    unicode_value = ord(char)
    return unicode_value


#Este ejemplo muestra cómo convertir un valor Unicode en un carácter en Python.

#Parameters:
 #   unicode_value (int): El valor Unicode que deseas convertir en un carácter.

#Returns:
 #   str: El carácter correspondiente al valor Unicode.

#def convertir_a_caracter(unicode_value):
  #  char = chr(unicode_value)
  #  return char


# Este ejemplo muestra cómo comparar cadenas alfabéticamente utilizando valores Unicode en Python.

def comparar_cadenas_alfabeticamente(str1, str2):
    if str1 < str2:
        return f"{str1} viene antes de {str2} alfabéticamente."
    else:
        return f"{str2} viene antes de {str1} alfabéticamente."

# Ejemplos de uso
char = 'A'
unicode_value = obtener_valor_unicode(char)
print(f"El valor Unicode de '{char}' es {unicode_value}")

unicode_value = 65  # El valor Unicode de 'A'
char = convertir_a_caracter(unicode_value)
print(f"El carácter correspondiente al valor Unicode {unicode_value} es '{char}'")

str1 = 'apple'
str2 = 'banana'
resultado = comparar_cadenas_alfabeticamente(str1, str2)
print(resultado)
