# Funcionalidad del CLI para el tema 4

# Importar las funciones necesarias
from src.interface.utils import validate_input

# Operaciones disponibles
operaciones = ["Conjunto generador", "Dependencia lineal", "Independencia lineal", "Regresar"]

def tema_4():
    print("\nHas escogido el tema 4\n")

    # Mostrar las operaciones disponibles
    for i in range(len(operaciones)):
        print(f"{i+1}. {operaciones[i]}")

    prompt = "\nEscribe el número de la operación que deseas calcular (del 1 al 4): "
    valid_options = [str(i) for i in range(1, len(operaciones) + 1)]
    # Preguntar al usuario por la operación
    choice = validate_input(prompt, valid_options)
    choice = int(choice) - 1  # Convertir a índice de lista

    if choice == 0:
        # Llamar a la función para el conjunto generador
        pass
    elif choice == 1:
        # Llamar a la función para la dependencia lineal
        pass
    elif choice == 2:
        # Llamar a la función para la independencia lineal
        pass
    elif choice == 3:
        # Regresar al menú principal
        return True
    return False