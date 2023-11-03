import sys

# Leer datos del usuario
user_input = input("Ingrese un valor: ")
print("Has ingresado:", user_input, file=sys.stdout)

# Simular un error
print("Esto es un mensaje de error", file=sys.stderr)

# sys.stdin: Representa el flujo de entrada estándar. Puedes usar sys.stdin para leer datos del usuario o de otro flujo de entrada.
# sys.stdout: Representa el flujo de salida estándar. Puedes usar sys.stdout para imprimir datos y resultados.
# sys.stderr: Representa el flujo de error estándar. Se utiliza para imprimir mensajes de error y advertencias.
