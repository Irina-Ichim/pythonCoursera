file_counts = {"jpeg": 20, "txt": 5, "pdf": 7, "js": 14}

# Iterar sobre las claves
print("Iterar sobre las claves:")
for extension in file_counts:
    print(extension)

# Iterar sobre claves y valores utilizando items()
print("\nIterar sobre claves y valores:")
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))

# Obtener una vista de las claves y valores
print("\nObtener vistas de claves y valores:")
keys_view = file_counts.keys()
values_view = file_counts.values()

# Convertir las vistas a listas si es necesario
keys_list = list(keys_view)
values_list = list(values_view)

print("Keys:", keys_list)
print("Values:", values_list)
