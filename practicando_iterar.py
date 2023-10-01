# Ejemplo 1: Calculando la longitud total y la longitud promedio de las palabras en una lista
animals = ["leon", "zebra", "pantera", "mono"]
chars = 0

# Itera sobre cada animal en la lista
for animal in animals:
    # Agrega la longitud de cada animal a la variable 'chars'
    chars += len(animal)

# Imprime la longitud total y la longitud promedio
print("Total characters: {}, Average length: {}".format(chars, chars / len(animals)))

# Ejemplo 2: Enumerando una lista de ganadores e imprimiendo el índice y el nombre
ganadores = ["Irina", "Karina", "Montse"]
for index, person in enumerate(ganadores):
    # Imprime el índice más 1 (para hacerlo más legible) y el nombre de la persona
    print("{} - {}".format(index + 1, person))

# Ejemplo 3: Enumerando una lista de frutas e imprimiendo el índice y la fruta
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
    # Imprime el índice y el nombre de la fruta
    print(indice, fruta)

