import re

fun_split = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(fun_split)

# si queremos que nuestra lista de division incluya los elementos que estamos usando para dividir los valores

fun_split = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(fun_split)

recibir_mensaje = re.sub(r"[\w.€+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
print(recibir_mensaje)

fun_sub = re.sub(r"^([\w .-]*), ([\w .-]*$)", r"\2 \1", "Lovelace, Ada")
print(fun_sub) 

prueba = re.split(r"the|a", "One sentence. Another one? And the last one!")
print(prueba)