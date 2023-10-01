# Listas de idiomas y longitud de caracteres
languages = ["Python", "JavaScript", "Kotlin", "Svelte", "SvelteKit"]

# List comprehension para obtener la longitud de cada idioma
lengths = [len(language) for language in languages]
print("Longitudes de idiomas:", lengths)

# List comprehension para obtener múltiplos de 3 hasta 100
z = [x for x in range(0, 101) if x % 3 == 0]
print("Múltiplos de 3 hasta 100:", z)

# Función que devuelve números impares hasta n utilizando list comprehension
def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]

# Ejemplos de la función odd_numbers
print("Números impares hasta 5:", odd_numbers(5))   # Debería imprimir [1, 3, 5]
print("Números impares hasta 10:", odd_numbers(10))  # Debería imprimir [1, 3, 5, 7, 9]
print("Números impares hasta 11:", odd_numbers(11))  # Debería imprimir [1, 3, 5, 7, 9, 11]
print("Números impares hasta 1:", odd_numbers(1))    # Debería imprimir [1]
print("Números impares hasta -1:", odd_numbers(-1))  # Debería imprimir [] 
