# Funcionalidad del CLI para el tema 5

# Importar las funciones necesarias
from src.interface.utils import validate_input

# Operaciones disponibles
operaciones = ["Suma de matrices",
    "Resta de matrices",
    "Producto de matriz por escalar",
    "Multiplicación de matrices",
    "Inversa de matrices",
    "Transposición de matrices",
    "Matriz de una transformación lineal",
    "Regresar"
    ]

def tema_5():
    print("\nHas escogido el tema 5\n")

    # Mostrar las operaciones disponibles
    for i in range(len(operaciones)):
        print(f"{i+1}. {operaciones[i]}")

    prompt = "\nEscribe el número de la operación que deseas calcular (del 1 al 8): "
    valid_options = [str(i) for i in range(1, len(operaciones) + 1)]
    # Preguntar al usuario por la operación
    choice = validate_input(prompt, valid_options)
    choice = int(choice) - 1  # Convertir a índice de lista

    if choice == 0:
        # Llamar a la función para la suma de matrices
        pass
    elif choice == 1:
        # Llamar a la función para la resta de matrices
        pass
    elif choice == 2:
        # Llamar a la función para el producto de matriz por escalar
        pass
    elif choice == 3:
        # Llamar a la función para la multiplicación de matrices
        pass
    elif choice == 4:
        # Llamar a la función para la inversa de matrices
        pass
    elif choice == 5:
        # Llamar a la función para la transposición de matrices
        pass
    elif choice == 6:
        # Llamar a la función para la matriz de una transformación lineal
        pass
    elif choice == 7:
        # Regresar al menú principal
        return True
    return False