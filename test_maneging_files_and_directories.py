# Ejercicio 1
import os

def create_python_script(filename):
    comments = "# Start of a new Python program"
    
    # Create the Python script file and write comments
    with open(filename, 'w') as file:
        file.write(comments)

    # Get the file size
    filesize = os.path.getsize(filename)
    
    return filesize

print(create_python_script("program.py"))

#Ejercicio 2 
def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)
  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, 'w') as file:
    pass
  # Return the list of files in the new directory
  return os.listdir()
print(new_directory("PythonPrograms", "script.py"))

# Ejercicio 3 
# Crear nuevo directorio usamos mk dir
# Ejercicio 4

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w') as file:
    pass
  timestamp = os.path.getmtime(filename)
 
  # Convert the timestamp into a readable format, then into a string
  date = datetime.datetime.fromtimestamp(timestamp)
  data_string= date.strftime("%Y-%m-%d")
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return data_string

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd

# Ejercicio 5
import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), os.pardir)

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())

# Importante 
# os.pardir es una cadena que representa el nombre especial del directorio padre en la mayoría de los sistemas de archivos.
# En la mayoría de los sistemas, se representa simplemente como "..". 
# Se utiliza comúnmente en programación para referirse al directorio padre de un directorio actual.