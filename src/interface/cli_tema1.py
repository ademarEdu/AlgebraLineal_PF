# Funcionalidad del CLI para el tema 1

# Importar las funciones necesarias
from src.interface.utils import validate_input, validate_float_input, validate_int_input, vector_input
from src.operations.tema1.prod_esc import dot_product
from src.operations.tema1.prod_vec import cross_product
from src.operations.tema1.triple_prod_esc import triple_dot_product
from src.operations.tema1.triple_prod_vec import triple_cross_product
from src.operations.utils import graph2D_vectors, graph3D_vectors
import numpy as np

# Operaciones disponibles
operaciones = ["Producto escalar",
    "Producto vectorial",
    "Triple producto escalar",
    "Triple producto vectorial",
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
        # Obtener datos del usuario
        n = validate_int_input("Escribe el número de dimensiones de tus vectores: ")
        vectores = []
        # Obten los valores de los 2 vectores
        for i in range(2):
            print(f"\nVECTOR {i+1}")
            vec = vector_input(n)
            vectores.append(vec)

        # Llamar a la función para el producto escalar
        print("\nEl producto escalar es:")
        print(np.array(dot_product(vectores)))

    elif choice == 1:
        # Llamar a la función del producto vectorial
        # Obtener datos del usuario
        # El producto cruz solo se puede obtener de vectores de 3 dimensiones
        n = 3
        vectores = []
        # Obten los valores de los 2 vectores
        for i in range(2):
            print(f"\nVECTOR {i+1}")
            vec = vector_input(n)
            vectores.append(vec)

        # Llamar a la función para el producto vectorial
        print("\nEl producto vectorial es:")
        print(np.array(cross_product(vectores)))

        # Crear una lista de los 3 vectores analizados
        vectores.append(cross_product(vectores))

        ans = validate_input("Quieres visualizar los vectores? (y/n) ", ["y", "n"])
        if ans == "y":
            graph3D_vectors(vectores, "Producto vectorial")

    elif choice == 2:
        # Llamar a la función para el triple producto escalar
        pass

    elif choice == 3:
        # Llamar a la función para el triple producto vectorial
                # El producto cruz solo se puede obtener de vectores de 3 dimensiones
        n = 3
        vectores = []

        # Obtener datos del usuario
        print("\nEl triple producto punto se calculará de la forma: V1 x (V2 x V3)")
        print("Todos los vectores deben ser tridimensionales")
        # Obten los datos del 1 vector
        print(f"\nVECTOR {1}")
        vectores.append(vector_input(n))

        # Obten los valores del 2 y 3 vector
        for i in range(2):
            print(f"\nVECTOR {i+2}")
            vec = vector_input(n)
            vectores.append(vec)

        # Llamar a la función para el triple producto vectorial
        print("\nEl triple producto vectorial es:")
        print(np.array(triple_cross_product(vectores)))

        # Crear una lista de los 3 vectores analizados
        vectores.append(triple_cross_product(vectores))

        ans = validate_input("Quieres visualizar los vectores? (y/n) ", ["y", "n"])
        if ans == "y":
            graph3D_vectors(vectores, "Triple producto vectorial")

    elif choice == 4:
        # Regresar al menú principal
        return True

    if validate_input("Quieres calcular más operaciones? (y/n): ", ["y", "n"]) == "y":
        return True

    return False