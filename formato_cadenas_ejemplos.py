"""
Formato de Cadenas en Python

Este script demuestra el uso de especificaciones de formato en cadenas en Python.
"""

def main():
    # Entero
    integer_value = 10.5
    integer_result = '{:d}'.format(int(integer_value))
    print(f"1. Entero: '{integer_result}'")

    # Punto flotante con decimales
    float_value = 0.5
    float_result = '{:.2f}'.format(float_value)
    print(f"2. Punto flotante: '{float_result}'")

    # Cadena con caracteres
    string_value = 'Python'
    string_result = '{:.2s}'.format(string_value)
    print(f"3. Cadena: '{string_result}'")

    # Cadena alineada a la izquierda
    left_aligned_result = '{:<6s}'.format('Py')
    print(f"4. Izquierda alineada: '{left_aligned_result}'")

    # Cadena alineada a la derecha
    right_aligned_result = '{:>6s}'.format('Py')
    print(f"5. Derecha alineada: '{right_aligned_result}'")

    # Cadena centrada
    centered_result = '{:^6s}'.format('Py')
    print(f"6. Centrada: '{centered_result}'")

if __name__ == "__main__":
    main()

    tiempo = "Rainfall"
    print(tiempo[:4])
