# Funcionalidad del CLI para el tema 3

# Importar las funciones necesarias
import numpy as np
from src.interface.utils import validate_input, validate_float_input, validate_int_input
from src.operations.tema3.sistema_ecuaciones import gauss_jordan_solve

# Operaciones disponibles
operaciones = ["Sistemas de ecuaciones lineales", "Regresar"]

def tema_3():
    print("\nHas escogido el tema 3\n")

    # Mostrar las operaciones disponibles
    for i in range(len(operaciones)):
        print(f"{i+1}. {operaciones[i]}")

    prompt = "\nEscribe el número de la operación que deseas calcular (del 1 al 2): "
    valid_options = [str(i) for i in range(1, len(operaciones) + 1)]
    # Preguntar al usuario por la operación
    choice = validate_input(prompt, valid_options)
    choice = int(choice) - 1  # Convertir a índice de lista

    if choice == 0:
        # Llamar a la función para resolver sistemas de ecuaciones lineales
        print("\nEsta calculadora necesita sistemas de ecuaciones lineales con n número de variables y n ecuaciones.")

        # Obtener los datos del usuario
        n = validate_int_input("\n¿Cuántas variables contiene el sistema que quieres resolver? ")
        #Definir la lista en la que estarán las ecuaciones
        equations = []
        # Obtener las ecuaciones del usuario
        for i in range(n):
            print(f"\nEcuación {i+1}:")
            coefficients = []
            for j in range(n):
                coeff = validate_float_input(f"Escribe el coeficiente de la variable x{j+1}: ")
                coefficients.append(coeff)
            # Agregar el término independiente
            constant = validate_float_input(f"Escribe el valor de la ecuación {i+1}.\nEjemplo: si x1 + 2x2 = 3, escribe 3: ")
            coefficients.append(constant)
            equations.append(coefficients)
        equations = np.array(equations)
        # Solucionar el sistema de ecuaciones mediante el método de Gauss Jordan
        solutions = gauss_jordan_solve(equations)
        for i in range(n):
            print(f"\nx{i+1} = {solutions[i]}")
        return False

    elif choice == 1:
        # Regresar al menú principal
        return True

    if validate_input("Quieres calcular más operaciones? (y/n): ", ["y", "n"]) == "y":
        return True
        
    return False