import os

# Utiliza doble barra invertida en la ruta o una barra invertida cruda
dir_path = "C:\\Users\\proye\\Desktop\\pythonCoursera"

# O bien, puedes usar una barra invertida cruda (r) al principio de la cadena
# dir_path = r"C:\Users\proye\Desktop\pythonCoursera"

# Lista los archivos y directorios en el directorio especificado
for name in os.listdir(dir_path):
    fullname = os.path.join(dir_path, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

