'''
Este script demuestra el uso de diccionarios en Python.
Crea un diccionario vacío y luego realiza varias operaciones, como agregar, modificar y eliminar elementos.
'''

w = {}
print(type(w))

file_counts = {"jpeg": 10, "pdf": 5, "word": 3}
print(type(file_counts))
print(file_counts)
print(file_counts["pdf"])
print("jpeg" in file_counts)
print("html" in file_counts)
file_counts["txt"] = 8
print(file_counts)
file_counts["txt"] = 25
print(file_counts)
del file_counts["word"]
print(file_counts)
