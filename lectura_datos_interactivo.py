while True:
    # funcion input
    name = input("Tu nombre: ")
    print("Hello, " + name)

    # Obtener la cantidad de horas, minutos y segundos del usuario
    horas = int(input("Ingresa la cantidad de horas: "))
    minutos = int(input("Ingresa la cantidad de minutos: "))
    segundos = int(input("Ingresa la cantidad de segundos: "))

    # Realizar la conversión a segundos
    total_segundos = (horas * 3600) + (minutos * 60) + segundos

    # Mostrar el resultado
    print(f"El total de segundos es: {total_segundos} segundos")

    continuar = input("¿Quieres continuar? (si/no): ")
    if continuar.lower() != "si":
        print("Goodbye")
        break

