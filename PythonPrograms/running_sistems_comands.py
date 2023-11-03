import subprocess

# El comando "ping" en Python generalmente se refiere a la funcionalidad de enviar solicitudes de eco ICMP 
# (Protocolo de Mensajes de Control de Internet) a través de una red para verificar la conectividad y la disponibilidad de un host remoto.
# Esto se puede lograr utilizando la biblioteca ping3, que proporciona una interfaz para realizar operaciones de ping en Python.

# La biblioteca ping3 permite a los desarrolladores de Python enviar solicitudes de eco ICMP a una dirección IP o un nombre de dominio
# y recibir respuestas para determinar si el host remoto está en línea y responde a las solicitudes de ping.

# Comando "ping" para verificar la conectividad a un host
def ping_example():
    host = "example.com"
    print(f"Verificando la conectividad a {host} usando el comando 'ping'...\n")
    subprocess.run(["ping", host])    # subprocess.run() se utiliza para ejecutar un comando externo y esperar a que termine. 

# Comando "date" para obtener la fecha y hora actual
def date_example():
    print("Obteniendo la fecha y hora actual usando el comando 'date'...\n")
    result = subprocess.run(["date"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Fecha y hora actual:")
    print(result.stdout)

# Comando "sleep" para pausar la ejecución del programa
def sleep_example():
    seconds = 5
    print(f"Pausando la ejecución durante {seconds} segundos usando el comando 'sleep'...\n")
    subprocess.run(["sleep", str(seconds)])
    print(f"Continuando después de la pausa de {seconds} segundos")

if __name__ == "__main":
    # Ejemplos de uso de los comandos
    ping_example()
    date_example()
    sleep_example()
