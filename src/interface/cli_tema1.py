# Funcionalidad del CLI para el tema 1

# Importar las funciones necesarias
from src.interface.utils import validate_input

# Operaciones disponibles
operaciones = ["Producto escalar",
    "Producto vectorial",
    "Triple producto escalar",
    "Triple producto punto",
    "Regresar"
    ]

def tema_1():
    print("\nHas escogido el tema 1\n")

    #Mostrar las operaciones disponibles
    for i in range(len(operaciones)):
        print(f"{i+1}. {operaciones[i]}")

    prompt = "\nEscribe el número de la operación que deseas calcular (del 1 al 5): "
    valid_options = [str(i) for i in range(1, len(operaciones) + 1)]
    # Preguntar al usuario por la operación
    choice = validate_input(prompt, valid_options)
    choice = int(choice) - 1  # Convertir a índice de lista

    if choice == 0:
        # Llamar a la función para el producto escalar
        pass
    elif choice == 1:
        # Llamar a la función para el producto vectorial
        pass
    elif choice == 2:
        # Llamar a la función para el triple producto escalar
        pass
    elif choice == 3:
        # Llamar a la función para el triple producto punto
        pass
    elif choice == 4:
        # Regresar al menú principal
        return True
    return False