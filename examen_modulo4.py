car_make = "Lamborghini"
print(car_make[3:-5])
print(car_make[-4:])
print(car_make[:7])

music_genres = ["rock", "pop", "country"]
music_genres.append("blues")
print(music_genres)

speed_limits = {"street":35 , "highway": 65, "school": 15}
print(speed_limits["highway"])

# Primer problema 
def format_address(address_string):
  
    house_number = ""
    street_name = ""

# Separate the house number from the street name.
    address_parts = address_string.split()
    
    for address_part in address_parts:
       # Complete the if-statement with a string method.  
       if address_part.isdigit():
         house_number = address_part
       else:
         street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.strip()
 
    # Use a string method to return the required formatted string.
    return "House number {} on a street named {}".format(house_number, street_name)
print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"


print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"


print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"

# Problema 2
def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for character in string: 
        # Complete the if-statement using a string method. 
        if character.isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21

#Problema 3

def combine_lists(list1, list2):


  combined_list = []  # Initialize an empty list variable
  list1.reverse() # Reverse the order of "list1"
  combined_list = list2 + list1 # Combine the two lists 
  return combined_list  
  
Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]


print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']

#Problema 4
def squares(start, end):
    return [ x**2 for x in range(start, end + 1) ] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Problema 5
def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for animal, count in animal_dict.items():
        # Use a string method to format the required string.
        result += f"{animal}\n"    # \n salto de linea en python
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger

# Problema 6

def combine_guests(guests1, guests2):
  guests2.update(guests1) # Use a dictionary method to combine the dictionaries.
  return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}

# Problema 7
def contar_letras(texto):
    # Inicializar un nuevo diccionario.
    diccionario = {}
    # Completar el bucle for para iterar a través de cada carácter de "texto" y
    # utilizar un método de cadena para asegurarse de que todas las letras estén en minúsculas.
    for char in texto.lower():  
        # Completar la declaración if usando un método de cadena para verificar si
        # el carácter es una letra.
        if char.isalpha():
            # Completar la declaración if usando un operador lógico para verificar si 
            # la letra aún no está en el diccionario.
            if char not in diccionario:
                # Utilizar una operación de diccionario para agregar la letra como clave
                # y establecer el valor de conteo inicial en cero.
                diccionario[char] = 0 
            # Utilizar una operación de diccionario para incrementar el valor de conteo de la letra
            # para la clave existente.
            diccionario[char] += 1 # Incrementar el contador de letras. 
    return diccionario

print(contar_letras("AaBbCc"))
# Debería ser {'a': 2, 'b': 2, 'c': 2}

print(contar_letras("Math is fun! 2+2=4"))
# Debería ser {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(contar_letras("This is a sentence."))
# Debería ser {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


