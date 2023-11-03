import re

result = re.search(r"(\w*), (\w*)", "Lovelace, Ada")
print(result)
print(result.groups()) # devuelve tupla con los grupos capturados
print(result[0])  # te permite acceder al texto completo
print(result[1])  # accede a la primera palabra
print(result[2])
formatted_result = "{} {}".format(result[2], result[1])
print(formatted_result)

# En el contexto de las expresiones regulares en Python el indice 0 es el texto completo
# El indice uno es la primera palabra

# def rearrange_name(name):
#     result = re.search(r"^(\w*),(\w*)$", name)
#     if result is None:
#         return name
#     return "{} {}".format(result[2], result[1])

# result_loveli = rearrange_name("Lovelace, Ada")
# print(result_loveli)
# result_irina = rearrange_name("Irina, Ichim")
# print(result_irina)



def rearrange_name(name):
  result = re.search(r"^([\w\s.-]*), ([\w\s.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)