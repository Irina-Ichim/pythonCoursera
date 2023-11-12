# script.py

def cause_segmentation_fault():
    # Crear un puntero nulo y tratar de acceder a su contenido
    null_pointer = None
    value = null_pointer[0]

def main():
    try:
        cause_segmentation_fault()
    except Exception as e:
        print(f"Se produjo un error: {e}")

if __name__ == "__main__":
    main()
