import calendar

# Crear un objeto de calendario
cal = calendar.TextCalendar()

# Imprimir el calendario de un mes específico
cal_month = cal.formatmonth(2023, 11)
print(cal_month)
