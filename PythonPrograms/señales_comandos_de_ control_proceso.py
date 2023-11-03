# Archivo de explicación de señales y comandos de administración de procesos

# Señales (Signals)
"""
Las señales son instrucciones enviadas a procesos en sistemas Unix y Linux para notificar eventos o controlar su comportamiento.
Las señales más comunes incluyen:
- SIGINT: Enviado cuando se presiona CTRL+C en la terminal. Solicita la interrupción de un proceso.
- SIGSTOP: Detiene un proceso.
- SIGCONT: Reanuda un proceso detenido.
- SIGKILL: Termina un proceso inmediatamente.
- SIGTERM: Solicita la terminación ordenada de un proceso.

"""

# Comandos de administración de procesos
"""
- `ping`: Comando utilizado para verificar la conectividad con un host remoto a través de la red.
- `CTRL+C`: Atajo de teclado que envía la señal SIGINT a un proceso en ejecución, lo que suele resultar en la interrupción del proceso.
- `CTRL+Z`: Atajo de teclado que envía la señal SIGTSTP, deteniendo un proceso en segundo plano.
- `fg`: Comando utilizado para reanudar un proceso detenido en segundo plano en la terminal.
- `kill`: Comando para enviar una señal a un proceso, lo que puede usarse para finalizar un proceso. Utiliza el PID para identificar el proceso.
- PID (Process Identifier): Número único asignado a cada proceso en el sistema operativo. Se utiliza para identificar y controlar procesos.
- `ps`: Comando para mostrar información sobre procesos en ejecución.
- `ps aux`: Comando para listar información detallada de todos los procesos en el sistema.

"""

# Ejemplo de uso de comandos:
"""
Si deseas finalizar un proceso con el PID 1234, puedes usar el comando:
$ kill 1234

Para listar todos los procesos en ejecución, puedes usar:
$ ps

Para listar información detallada de todos los procesos en el sistema, puedes usar:
$ ps aux
"""


