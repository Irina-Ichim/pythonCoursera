import calendar
import tkinter as tk
from tkinter import ttk

def mostrar_calendario():
    year = int(entry_anio.get())
    month = int(entry_mes.get())

    cal_text = calendar.TextCalendar().formatmonth(year, month)
    texto_calendario.config(state=tk.NORMAL)
    texto_calendario.delete(1.0, tk.END)
    texto_calendario.insert(tk.END, cal_text)
    texto_calendario.config(state=tk.DISABLED)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calendario")

# Etiquetas y cuadros de entrada para el año y el mes
etiqueta_anio = ttk.Label(ventana, text="Año:")
etiqueta_anio.grid(row=0, column=0, padx=5, pady=5)

entry_anio = ttk.Entry(ventana)
entry_anio.grid(row=0, column=1, padx=5, pady=5)

etiqueta_mes = ttk.Label(ventana, text="Mes:")
etiqueta_mes.grid(row=0, column=2, padx=5, pady=5)

entry_mes = ttk.Entry(ventana)
entry_mes.grid(row=0, column=3, padx=5, pady=5)

# Botón para mostrar el calendario
boton_mostrar = ttk.Button(ventana, text="Mostrar Calendario", command=mostrar_calendario)
boton_mostrar.grid(row=0, column=4, padx=5, pady=5)

# Texto para mostrar el calendario
texto_calendario = tk.Text(ventana, height=10, width=20, state=tk.DISABLED)
texto_calendario.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

# Iniciar el bucle de la aplicación
ventana.mainloop()
