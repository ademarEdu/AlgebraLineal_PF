# Funcionalidad CLI para el tema 6

# Importar las funciones necesarias
from src.interface.utils import validate_input

# Operaciones disponibles
operaciones = ["Determinante de una matriz", "Regresar"]

def tema_6():
    print("\nHas escogido el tema 6\n")

    # Mostrar las operaciones disponibles
    for i in range(len(operaciones)):
        print(f"{i+1}. {operaciones[i]}")

    prompt = "\nEscribe el número de la operación que deseas calcular (del 1 al 2): "
    valid_options = [str(i) for i in range(1, len(operaciones) + 1)]
    # Preguntar al usuario por la operación
    choice = validate_input(prompt, valid_options)
    choice = int(choice) - 1  # Convertir a índice de lista

    if choice == 0:
        # Llamar a la función para calcular el determinante de una matriz
        pass
    elif choice == 1:
        # Regresar al menú principal
        return True
    return False