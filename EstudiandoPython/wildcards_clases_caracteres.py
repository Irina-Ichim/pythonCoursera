import re
print(re.search(r"[pP]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "Whats a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9")) 

def check_punctuation (text):
  result = re.search(r"[\s\S]*[.,!?;]$", text) # simbolos
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))  # te enseña el primer espacio
# Si queremos que no se excluya el primer espacio simplemete añadimos espacio despues del Z
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces.")) #hemos excluido los espacios, nos enseña el punto

print(re.search(r"cat|dog","I like dogs."))
print(re.search(r"cat|dog","I like dogs and cats.")) # unicamente te da la primera respuesta aunque tenga varias
print(re.findall(r"cat|dog", "I like cats and dogs."))