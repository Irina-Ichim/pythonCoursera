def binary_search(target, sorted_list):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == target:
            return mid  # Elemento encontrado, devolver índice
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Elemento no encontrado

def bisect_and_identify_issue(data, issue_index):
    # Simulando un problema en el conjunto de datos en el índice proporcionado
    data[issue_index] = "Problema"

    # Aplicando búsqueda binaria para identificar la causa raíz del problema
    target = "Problema"
    result = binary_search(target, data)

    if result != -1:
        print(f"Problema encontrado en el índice {result}.")
    else:
        print("El problema no fue encontrado en el conjunto de datos.")

if __name__ == "__main__":
    # Crear una lista ordenada de datos
    dataset = [str(i) for i in range(1, 101)]

    # Simular un problema en el conjunto de datos
    issue_index = 65  # Índice donde se simulará un problema

    # Aplicar búsqueda binaria para identificar la causa raíz del problema
    bisect_and_identify_issue(dataset, issue_index)

# La función binary_search realiza la búsqueda binaria en una lista ordenada. La función bisect_and_identify_issue simula un problema en el 
# conjunto de datos y luego utiliza la búsqueda binaria para identificar la causa raíz del problema.