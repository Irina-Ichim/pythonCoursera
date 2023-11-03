import re
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_\s]*$"
print(re.search(pattern, "_this_is_a _variable_name"))
print(re.search(pattern, "this isn´t a valid variable"))   #Resultado none porque no hay_
print(re.search(pattern, "my_variable30"))
print(re.search(pattern, "4my_variable30")) # en nuestro patron no usamos numero al inicio asi que el resultado sera none

def check_sentence(text):
  result = re.search(r"^[A-Z].*[.!?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True