import re

# regex = r"(\d{2}) elephants in a (\[.+\])"
# text = "99 elephants in a [cage]"

# result = re.search(regex, text)

# if result:
#     # Acceder a los grupos de captura
#     num_elephants = result.group(1)
#     location = result.group(2)

#     print("Número de elefantes:", num_elephants)
#     print("Ubicación:", location)
# else:
#     print("No se encontró ninguna coincidencia.")
    
# def extract_pid(log_line):
#     regex = r"\[(\d+)]" 
#     result = re.search(regex, log_line)
#     if result is None:
#         return ""
#     return result[1]

# log = "Process started [12345]"
# print(extract_pid(log))
        

def extract_pid(log_line):
    regex = r"\[(\d+)]"
    result = re.search(regex, log_line)
    if result is None:
        return ""  # Si no se encuentra ningún número en corchetes, devuelve una cadena vacía.
    return result[1]  # Devuelve el número encontrado dentro de los corchetes.

# Ejemplos de líneas de registro y sus PID extraídos
log1 = "Process started [12345]"
log2 = "Error in process [9876] - Termination"
log3 = "Received request [54321] from client"

pid1 = extract_pid(log1)
pid2 = extract_pid(log2)
pid3 = extract_pid(log3)

print("PID 1:", pid1)  # Resultado: 12345
print("PID 2:", pid2)  # Resultado: 9876
print("PID 3:", pid3)  # Resultado: 54321



def extract_pids(log_line):
    regex = r"\[(\d+)]"
    pids = re.findall(regex, log_line)
    return pids

log3 = "Received request [54321] [7865] from client"   # mas de un numero y lo quiero extraer todo
pids = extract_pids(log3)
print("PIDs:", pids)  # Resultado: [54321, 7865]