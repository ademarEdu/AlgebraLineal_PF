# Funcionalidad del CLI para el tema 2

# Importar las funciones necesarias
from src.interface.utils import validate_input, validate_int_input, validate_float_input
from src.operations.tema2.graf_funciones import graph_functions 

# Operaciones disponibles
operaciones = ["Gráfica de funciones", "Regresar"]

def tema_2():
    print("\nHas escogido el tema 2\n")

    # Mostrar las operaciones disponibles
    for i in range(len(operaciones)):
        print(f"{i+1}. {operaciones[i]}")

    prompt = "\nEscribe el número de la operación que deseas calcular (del 1 al 2): "
    valid_options = [str(i) for i in range(1, len(operaciones) + 1)]
    # Preguntar al usuario por la operación
    choice = validate_input(prompt, valid_options)
    choice = int(choice) - 1  # Convertir a índice de lista

    if choice == 0:
        functions = []  # Lista en donde se guardarán las funciones
        n = validate_int_input("\n¿Cuántas funciones quieres graficar? ")
        # Preguntar datos al usuario
        for i in range(n):
            func_str = input(f"Ingrese la función {i+1} en términos de x. Ejemplo: (x**2)**(0.5) + 3: ")
            try:
                # Crea una función lambda segura usando eval
                func = eval(f"lambda x: {func_str}")
                functions.append(func)
            except Exception as e:
                print("Función inválida:", e)
        # Graficar las funciones
        graph_functions(functions, title="Funciones")
    elif choice == 1:
        # Regresar al menú principal
        return True

    if validate_input("Quieres calcular más operaciones? (y/n): ", ["y", "n"]) == "y":
        return True
        
    return False
