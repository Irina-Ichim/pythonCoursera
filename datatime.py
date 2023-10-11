# Importar el módulo datetime
import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()

# Imprimir la fecha y hora actual
print("Fecha y hora actual:", fecha_hora_actual)

# Calcular la fecha y hora de mañana
delta_un_dia = datetime.timedelta(days=1)
fecha_hora_mañana = fecha_hora_actual + delta_un_dia

# Imprimir la fecha y hora de mañana
print("Fecha y hora de mañana:", fecha_hora_mañana)
