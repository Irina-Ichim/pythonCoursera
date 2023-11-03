import re
print(re.search(r"[a-zA-Z]{5}","a ghost"))
print(re.search(r"[a-zA-Z]{5}","a scary ghost appeared"))  # se lleva la primera palabra de 5
print(re.findall(r"[a-zA-Z]{5}","a scary ghost appeared")) #encuentra todas las palabras de 5
print(re.findall(r"\b[a-zA-Z]{5}\b", " A scary ghost apparead")) #\b para delimitar una palabra
print(re.findall(r"\w{5,10}", "I really like strawberries")) #ojo, no dejes espacios entre corchetes
print(re.findall(r"\w{5,}", "I really like strawberries"))

#Dentro de los corchetes, si solo dejas un número (por ejemplo, {5,}), Python entenderá que el patrón debe coincidir con al menos 5 o más repeticiones del elemento que precede a los corchetes.
print(re.findall(r"\w{5,}", "I really like strawberries"))

#Dentro de los corchetes, si usas {,5}, Python entenderá que el patrón debe coincidir con un máximo de 5 repeticiones del elemento que precede a los corchetes. Esto establece un límite superior en la cantidad de repeticiones permitidas.
print(re.findall(r"\w{,5}", "I really like strawberries"))