import re
print(re.search(r".com", "Welcome"))
print(re.search(r"\.com", "Welcome"))
print(re.search(r"\.com", "mydomain.com"))

# Ojo no confundas
# \n   no las confundas, esta significa nueva linea
# \t significa nueva pesataña 
# \w significa cualquier caracter alfanumerico, incluyendo letras, numeros y guiones bajos

print(re.search(r"\w*","This is an example "))  # comienza a buscar desde el inicio del string
print(re.search(r"\w*","And_this_is_another "))

# \d _ significa digitos
# \s significa espacios en blanco, tabulacion o nueva linea
# \b limites de palabras y algunos otros

def check_character_groups(text):
  result = re.search(r"\w+\s+\w+", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False