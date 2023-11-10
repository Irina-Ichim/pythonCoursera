# script.py

def send_reminder(date, title):
    # Aquí iría la lógica para enviar el recordatorio
    # En este ejemplo, simplemente imprimimos un mensaje
    print(f"Enviando recordatorio para la reunión '{title}' el {date}")

def main():
    # Solicitar al usuario la fecha y el título de la reunión
    date = input("Ingrese la fecha de la reunión (formato MM-DD-YYYY): ")
    title = input("Ingrese el título de la reunión: ")

    # Llamar a la función para enviar el recordatorio
    send_reminder(date, title)

if __name__ == "__main__":
    main()
