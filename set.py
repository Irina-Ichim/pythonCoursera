# Definir un conjunto
my_set = {1, 2, 3, 4, 5}

# Agregar un elemento al conjunto
my_set.add(6)

# Intentar agregar un elemento duplicado (no se añadirá)
my_set.add(2)

# Mostrar el conjunto (puede tener un orden diferente)
print("Conjunto:", my_set)

# Operaciones de conjunto
other_set = {4, 5, 6, 7}

# Unión
union_result = my_set.union(other_set)
print("Unión:", union_result)

# Intersección
intersection_result = my_set.intersection(other_set)
print("Intersección:", intersection_result)

# Diferencia
difference_result = my_set.difference(other_set)
print("Diferencia:", difference_result)
